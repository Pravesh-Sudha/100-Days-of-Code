# Day 75 of 100DaysOfCode

Feeling excited to start Day 75 of 100 DaysOfCode, today, I dived deep into AWS, jenkins and docker by building a Complete CICD project with guidance of [TrainWithShubhum](https://www.youtube.com/live/nplH3BzKHPk?si=9JYwgIldcWRX0eWd). In the project, I get to revise my basics of AWS, jenkins, docker and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-75
```

Certainly! Below is a template for your README.md file:

---

# Jenkins CI/CD Pipeline for Node.js Todo Application

## Overview

This repository contains a Jenkins pipeline that automates the Continuous Integration and Continuous Deployment (CI/CD) process for a Node.js Todo application. The pipeline performs the following steps:

1. Clones the code from the GitHub repository: [https://github.com/Pravesh-Sudha/node-todo-cicd.git](https://github.com/Pravesh-Sudha/node-todo-cicd.git).
2. Builds a Docker image using the provided Dockerfile.
3. Tags the Docker image as `pravesh2003/node-app`.
4. Pushes the Docker image to the Docker Hub account: [pravesh2003](https://hub.docker.com/u/pravesh2003).
5. Runs the Docker container.

## Prerequisites

Before running the Jenkins pipeline, ensure that the following prerequisites are met:

- Jenkins is installed and configured.
- Docker is installed on the Jenkins server.
- Docker Hub account is created ([pravesh2003](https://hub.docker.com/u/pravesh2003)).
- Jenkins is configured with necessary credentials for GitHub and Docker Hub.

## Jenkins Pipeline Configuration

The Jenkins pipeline is defined in the `Jenkinsfile` at the root of this repository. The pipeline script is designed to be run on a Jenkins server.

## Dockerfile

The Dockerfile used in the project is as follows:

```Dockerfile
FROM node:12.2.0-alpine

WORKDIR /app

COPY . .

RUN npm install
RUN npm run test

EXPOSE 8000

CMD ["node", "app.js"]
```

This Dockerfile sets up a Node.js environment, copies the application code, installs dependencies, runs tests, exposes port 8000, and defines the command to start the application.

## Running the Pipeline

To run the Jenkins pipeline:

1. Configure the Jenkins pipeline job with the appropriate settings and credentials which can be seen in [Jenkinsfile](Jenkinsfile).
2. Trigger the pipeline manually or set up a webhook for automatic triggering on code changes.

The pipeline will automatically clone the code, build the Docker image, tag it, push it to Docker Hub, and run the Docker container.
