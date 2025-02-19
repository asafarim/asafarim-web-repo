# ASafariM - Full Stack Clean Architecture Solution

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![.NET](https://img.shields.io/badge/.NET-9.0-blue) ![React](https://img.shields.io/badge/React-Typescript-blue)

Welcome to the ASafariM Full Stack Clean Architecture Solution! 🚀

A modern, enterprise-grade full-stack web application built with the latest technologies to showcase my skills as a Full Stack Developer. This project leverages .NET 9 and React TypeScript, following Clean Architecture principles to ensure scalability, maintainability, and high performance.

## 🏗️ Architectural Overview

The project is structured into distinct layers to promote a clear separation of concerns:
- **Presentation**: The UI layer built with React and TypeScript.
- **Application**: The application layer containing business logic.
- **Domain**: The core domain layer with domain entities and services.
- **Infrastructure**: The infrastructure layer handling data access and external services.

## ⚙️ Key Features

- **Dynamic Portfolio**: An interactive portfolio that fetches project data from a custom API.
- **Real-Time Features**: Live data communication using SignalR.
- **Advanced Authentication**: Secure authentication and authorization with JWT tokens.
- **DevOps Integration**: Continuous Integration/Continuous Deployment (CI/CD) with Azure DevOps.
- **Comprehensive Testing**: Full unit and integration test suites for reliable code.

## 🌟 Highlights

### Dependency Injection
Implementing dependency injection makes the codebase more testable and maintainable.

### State Management
Efficient state management using Redux and Context API to handle complex state logic.

### Performance Optimization
Leveraging techniques like lazy loading and code splitting for an optimized user experience.

### Cloud Integration
Serverless functions with Azure Functions for scalable and cost-effective backend services.

### Microservices Architecture
Designing parts of the backend as microservices for enhanced scalability.

### Containerization
Deploying the application with Docker and Kubernetes for seamless container orchestration.

## ✨ User Experience

- **Responsive Design**: Fully responsive layout for a great user experience on any device.
- **SEO Best Practices**: Server-side rendering with Next.js for better SEO and performance.

## 🚀 Getting Started

### Prerequisites
- [.NET 9](https://dotnet.microsoft.com/download/dotnet/9.0)
- [Node.js](https://nodejs.org/)
- [Docker](https://www.docker.com/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/asafarim/asafarim-web-repo.git
   cd asafarim-web-repo
   ```

2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Install backend dependencies:
   ```bash
   cd ../backend
   dotnet restore
   ```

### Running the Application
1. Start the backend server:
   ```bash
   cd backend
   dotnet run
   ```

2. Start the frontend server:
   ```bash
   cd ../frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`.

## 📚 Documentation

For more details, please refer to the [Project Wiki](https://github.com/asafarim/asafarim-web-repo/wiki).

## 🤝 Contributing

Contributions are welcome! Please check out the [contributing guidelines](CONTRIBUTING.md).

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 😊
