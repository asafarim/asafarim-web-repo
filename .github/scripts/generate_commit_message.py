import subprocess
import logging
from openai import OpenAI, OpenAIError, RateLimitError
from dotenv import load_dotenv
import os
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
try:
    client = OpenAI(
        organization=os.getenv("OPENAI_ORG_ID"), api_key=os.getenv("OPENAI_API_KEY")
    )
except Exception as e:
    logging.error(f"Failed to initialize OpenAI client: {e}")
    raise SystemExit(e)


def get_git_diff():
    """Get the output of git diff."""
    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "--cached"], encoding="utf-8"
        )
        return diff_output
    except subprocess.CalledProcessError as e:
        logging.error(f"Error getting git diff: {e}")
        return None


# Define a list of GPT engines to use
gpt_engines = [
    "o1-mini",
    "gpt-3.5-turbo",
    "o1-preview",
    "gpt-4o",
    "gpt-4",
    "gpt-4o-mini-realtime-preview",
    "gpt-4o-realtime-preview",
    "gpt-4-turbo",
    "gpt-4o-mini",
    "chatgpt-4o-latest",
]

gpt_engine = gpt_engines[-1]


def generate_commit_message(diff):
    """Generate a commit message using OpenAI's GPT model."""
    prompt = f"Generate a concise commit message for the following changes:\n\n{diff}"

    retries = 3
    for i in range(retries):
        try:
            response = client.chat.completions.create(
                model=gpt_engine, messages=[{"role": "user", "content": prompt}]
            )
            message = response.choices[-1].message.content
            # Remove backticks and 'commit message:' prefix if present
            message = message.strip('`').replace('commit message:', '').strip()
            return message
        except (OpenAIError, RateLimitError) as e:
            logging.warning(f"Attempt {i + 1}: Error generating commit message using GPT {gpt_engine}: {e}")
            time.sleep(2 ** i)  # Exponential backoff
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            break
    return None


def main():
    diff = get_git_diff()
    if diff:
        commit_message = generate_commit_message(diff)
        if commit_message:
            logging.info("Generated Commit Message:")
            logging.info(commit_message)

            # Create the commit with the generated message
            try:
                subprocess.run(["git", "commit", "-m", commit_message], check=True)
                logging.info("Commit created successfully!")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error creating commit: {e}")
        else:
            logging.warning("Failed to generate commit message.")
    else:
        logging.info("No changes to commit.")


if __name__ == "__main__":
    main()
