# Web API Demo

This repository contains a demo project for showcasing a Web API implementation, specifically focusing on the `WeatherForecast` API.

## Features

- RESTful API design
- WeatherForecast API testing
- JSON serialization
- Error handling
- Docker support
- Azure Pipeline integration
- Helm charts for Kubernetes deployment

## Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) (version X.X or later)
- Docker
- Kubernetes CLI (kubectl)
- Helm CLI
- Any IDE or text editor (e.g., Visual Studio, VS Code)

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/webapidemo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd webapidemo
    ```
3. Build the project:
    ```bash
    dotnet build
    ```
4. Run the application:
    ```bash
    dotnet run
    ```

## Testing the WeatherForecast API

Use the following endpoint to test the `WeatherForecast` API:

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | /WeatherForecast     | Retrieve weather forecasts   |

You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API.

## Docker Support

A `Dockerfile` is included in the repository to containerize the application. To build and run the Docker container:

1. Build the Docker image:
    ```bash
    docker build -t webapidemo:latest .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 80:8080 webapidemo:latest
    ```

## Azure Pipeline

The repository includes an Azure Pipeline configuration file (`azure-pipelines.yml`) for CI/CD. To set up the pipeline:

1. Navigate to your Azure DevOps project.
2. Create a new pipeline and point it to this repository.
3. The pipeline will build, test, and deploy the application.

## Helm Charts

Helm charts are provided in the `helm/` directory for deploying the application to a Kubernetes cluster. To deploy using Helm:

1. Install the Helm chart:
    ```bash
    helm install webapidemo ./helm
    ```
2. Verify the deployment:
    ```bash
    kubectl get all
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
