# Day 72 of 100DaysOfCode

Feeling excited to start Day 72 of 100 DaysOfCode, today, I learned about Gitlab CI in a amazing tutorial video by [CloudChamp](https://youtu.be/JWXVijJfnHc?si=fKMk3fULmH_ak7f4). In this video, I get to know about basics of Gitlab CI, its runner, artifacts, CICD for NodeJS and python application and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-72
```

## Introduction

GitLab CI/CD is a robust and integrated continuous integration and continuous delivery platform provided by GitLab. It allows developers to automate the building, testing, and deployment of their applications, ensuring a consistent and reliable software delivery process.

## Table of Contents

1. [What is GitLab CI/CD?](#what-is-gitlab-cicd)
2. [Creating a Pipeline in GitLab](#creating-a-pipeline-in-gitlab)
3. [Stages in GitLab](#stages-in-gitlab)
4. [GitLab Artifacts](#gitlab-artifacts)
5. [Runner](#runner)
6. [Variables and Environment Variables in GitLab](#variables-and-environment-variables-in-gitlab)
7. [CI Lint in GitLab](#ci-lint-in-gitlab)
8. [CI/CD for Node.js App](#cicd-for-nodejs-app)
9. [CI/CD for Python App](#cicd-for-python-app)

## What is GitLab CI/CD?

GitLab CI/CD is a part of the GitLab platform that provides a powerful and flexible continuous integration and continuous delivery solution. It allows developers to define and automate their software delivery pipelines, enabling them to streamline the process of building, testing, and deploying applications.

## Creating a Pipeline in GitLab

To create a pipeline in GitLab, you need to define a `.gitlab-ci.yml` file in the root of your project. This file specifies the stages, jobs, and scripts needed for your CI/CD pipeline. GitLab automatically detects changes to this file and triggers the pipeline accordingly.

Example `.gitlab-ci.yml`:

```yaml
stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  script:
    - echo "Building the application"

test_job:
  stage: test
  script:
    - echo "Running tests"

deploy_job:
  stage: deploy
  script:
    - echo "Deploying the application"
```

## Stages in GitLab

Stages in GitLab represent different phases in your CI/CD pipeline. Common stages include:

- **Build**: Compile and package the application.
- **Test**: Run automated tests to ensure code quality.
- **Deploy**: Deploy the application to a staging or production environment.

## GitLab Artifacts

Artifacts are files or directories created by jobs in a pipeline that you want to pass to the next stages. They can include build artifacts, test reports, or any other files generated during the pipeline. Artifacts can be used for debugging or as inputs for subsequent jobs.

Example:

```yaml
build_job:
  script:
    - make build
  artifacts:
    paths:
      - binaries/
```

## Runner

GitLab Runner is an agent that runs jobs defined in your CI/CD pipeline. Runners can be shared among projects and are responsible for executing the commands specified in each job. GitLab offers shared runners or you can register your own custom runner.

## Variables and Environment Variables in GitLab

Variables in GitLab CI/CD allow you to define parameters that can be used in your pipeline configuration. Environment variables can be set globally or per job, providing a way to customize the behavior of your pipeline.

Example:

```yaml
variables:
  DATABASE_URL: "postgres://user:password@localhost/db"

test_job:
  script:
    - echo $DATABASE_URL
```

## CI Lint in GitLab

GitLab provides a CI Lint tool that allows you to validate your `.gitlab-ci.yml` file before committing it. This ensures that your pipeline configuration is correct and avoids unexpected issues during execution.

## CI/CD for Node.js App

For a Node.js application, your CI/CD pipeline may include stages such as:

- Installing dependencies
- Running tests with tools like Jest
- Building the application
- Deploying to a server or container registry

Example pipeline stages for Node.js:

```yaml
stages:
  - install
  - test
  - build
  - deploy
```

## CI/CD for Python App

For a Python application, your CI/CD pipeline may include stages such as:

- Setting up a virtual environment
- Installing dependencies using pip
- Running tests with tools like pytest
- Building and packaging the application
- Deploying to a server or container registry

Example pipeline stages for Python:

```yaml
stages:
  - setup
  - test
  - build
  - deploy
```