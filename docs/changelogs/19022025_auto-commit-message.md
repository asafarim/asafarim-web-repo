---
title: Python script as a mini project to automatically generate commit messages using OpenAI's GPT model.
slug: 19022025_auto-commit-message
date: 19/02/2024
categories: ["Python", "Git", "OpenAI"]
tags: ["automation", "commit message", "OpenAI GPT"]
---
# Python script as a mini project to automatically generate commit messages using OpenAI's GPT model.

### Project Overview

**Objective**: Create a Python script that automatically generates a Git commit message based on the staged changes (using `git diff`) and uses OpenAI's GPT model to create a meaningful commit message.

### Key Components

1. **Environment Setup**: Use the `dotenv` library to load environment variables (like the OpenAI API key).
2. **Subprocess Module**: Use Python's `subprocess` module to interact with Git commands.
3. **OpenAI API**: Utilize the OpenAI API to generate commit messages.
4. **Error Handling & Logging**: Implement robust error handling and logging mechanisms to ensure the script runs smoothly.

### Detailed Explanation

1. **Environment Setup**
   - **Load Environment Variables**: Load the OpenAI organization ID and API key from a `.env` file. This keeps sensitive information secure.
   
   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()
   ```

2. **Initialize OpenAI Client**
   - **OpenAI Client Initialization**: Set up the OpenAI client using the environment variables.
   
   ```python
   from openai import OpenAI, OpenAIError, RateLimitError

   try:
       client = OpenAI(
           organization=os.getenv("OPENAI_ORG_ID"), api_key=os.getenv("OPENAI_API_KEY")
       )
   except Exception as e:
       logging.error(f"Failed to initialize OpenAI client: {e}")
       raise SystemExit(e)
   ```

3. **Get Git Diff**
   - **Get the Git Diff Output**: Use the subprocess module to get the output of `git diff --cached`, which shows the staged changes.
   
   ```python
   import subprocess

   def get_git_diff():
       try:
           diff_output = subprocess.check_output(
               ["git", "diff", "--cached"], encoding="utf-8"
           )
           return diff_output
       except subprocess.CalledProcessError as e:
           logging.error(f"Error getting git diff: {e}")
           return None
   ```

4. **Generate Commit Message**
   - **Prompt OpenAI GPT Model**: Send the Git diff output to OpenAI's GPT model to generate a commit message.
   - **Retry Mechanism**: Include a retry mechanism with exponential backoff to handle transient errors.

   ```python
   def generate_commit_message(diff):
       prompt = f"Generate a concise commit message for the following changes:\n\n{diff}"
       retries = 3

       for i in range(retries):
           try:
               response = client.chat.completions.create(
                   model=gpt_engine, messages=[{"role": "user", "content": prompt}]
               )
               return response.choices[-1].message.content
           except (OpenAIError, RateLimitError) as e:
               logging.warning(f"Attempt {i + 1}: Error generating commit message using GPT {gpt_engine}: {e}")
               time.sleep(2 ** i)  # Exponential backoff
           except Exception as e:
               logging.error(f"Unexpected error: {e}")
               break
       return None
   ```

5. **Main Function**
   - **Fetch Git Diff**: Get the diff output using the `get_git_diff` function.
   - **Generate Commit Message**: Generate a commit message using the `generate_commit_message` function.
   - **Create Git Commit**: Use the generated commit message to create a Git commit.

   ```python
   def main():
       diff = get_git_diff()
       if diff:
           commit_message = generate_commit_message(diff)
           if commit_message:
               logging.info("Generated Commit Message:")
               logging.info(commit_message)

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
   ```

### Summary

This mini project demonstrates how to integrate OpenAI's GPT model into a practical workflow—automating the process of generating commit messages for your Git repository. Key practices include:

- **Environment management**: Safely handling API keys.
- **Subprocess management**: Interacting with Git.
- **Error handling**: Providing informative error messages and retrying failed API calls.
- **Logging**: Keeping track of events and errors for easier debugging.
