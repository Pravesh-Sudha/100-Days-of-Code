# Day 74 of 100DaysOfCode

Feeling excited to start Day 74 of 100 DaysOfCode, today, I dived deep into AWS, jenkins and docker by building a Complete CICD project with guidance of [TrainWithShubhum](https://youtu.be/KvL_FGs--a0?si=BcgHU5G650_2Heor). In the project, I get to revise my basics of AWS, jenkins, docker and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-74
```

# Django Todo DevOps Project

This repository contains a Django Todo application that can be used as a starting point for your projects. Additionally, it includes a Dockerfile for containerization, and a Jenkins CI/CD pipeline for automating the build and deployment process.

## Getting Started

### Prerequisites
- Docker installed on your machine.
- Jenkins server set up and running.
- DockerHub account for pushing Docker images.

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Pravesh-Sudha/django-todo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-todo
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Dockerfile

A Dockerfile is included in the project to facilitate containerization. Build and run the Docker image with the following commands:

```bash
docker build -t django-todo-app .
docker run -p 8000:8000 django-todo-app
```

### Jenkins CI/CD Pipeline

This project includes a Jenkinsfile that defines a CI/CD pipeline. Make sure you have a Jenkins server set up, and create a new pipeline job with the following configuration:

1. Connect Jenkins to your version control system (GitHub).
2. Set up credentials for DockerHub (username and password) in Jenkins.
3. Add the pipeline script from the `Jenkinsfile` in this repository.

The pipeline includes the following stages:

- **Checkout**: Clone the repository.
- **Build**: Build the Docker image.
- **Push to DockerHub**: Push the built Docker image to DockerHub.
- **Deploy**: Deploy the application (you may need additional configurations for your specific deployment environment).

Adjust the Jenkinsfile according to your requirements, such as environment variables and deployment steps.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.