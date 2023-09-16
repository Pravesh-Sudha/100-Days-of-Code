# Day 26 of 100DaysofCode

Feeling excited to start Day 26 of 100 DaysOfCode, today, I built a Dockerfile for a Django To-do list Program and deployed it on AWS Ec2 Instance, also I watched [Flask Tutorial](https://youtu.be/Z1RJmh_OqeA?si=eHFkzl4qqZUKChnS) by <b>FreeCodeCamp</b>. This video contains beginner guide to flask functionalities, how flask projects works and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-26
```

# Django To-Do List App

This is a simple To-Do List web application built using Django. You can use this README.md file as a guide to clone the project, create a Docker image, and deploy it on an AWS EC2 instance.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run Migrations](#run-migrations)
  - [Start the Development Server](#start-the-development-server)
- [Dockerize the Application](#dockerize-the-application)
  - [Create a Dockerfile](#create-a-dockerfile)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Deploy on AWS EC2](#deploy-on-aws-ec2)
  - [Launch an EC2 Instance](#launch-an-ec2-instance)
  - [Connect to EC2](#connect-to-ec2)
  - [Install Docker on EC2](#install-docker-on-ec2)
  - [Copy Your Docker Image](#copy-your-docker-image)
  - [Run the Docker Container on EC2](#run-the-docker-container-on-ec2)

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python 3.x
- Django (Latest Version)
- Docker (if you plan to containerize the app)
- AWS Account (for deploying on EC2)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/shreys7/django-todo.git
cd django-todo
```

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to isolate your project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### Run Migrations

Apply the database migrations:

```bash
cd django-todo
python manage.py makemigrations
```

### Start the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application should now be running at `http://localhost:8000`.

## Dockerize the Application

### Create a Dockerfile

Create a `Dockerfile` in your project directory:

```Dockerfile
FROM python:3

RUN pip install django==3.2

COPY . .

RUN python manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]

```

### Build the Docker Image

Build the Docker image:

```bash
docker build -t django-todo-list-app .
```

### Run the Docker Container

Run the Docker container:

```bash
docker run -d -p 8000:8000 django-todo-list-app
```

The application should now be accessible at `http://localhost:8000`.

## Deploy on AWS EC2

### Launch an EC2 Instance

1. Log in to your AWS Management Console.
2. Navigate to the EC2 dashboard.
3. Launch a new EC2 instance, selecting an appropriate Amazon Machine Image (AMI) and instance type.

### Connect to EC2

Use SSH to connect to your EC2 instance:

```bash
ssh -i "your-ec2-key.pem" ec2-user@your-ec2-instance-ip
```

### Install Docker on EC2

Install Docker on your EC2 instance:

```bash
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```

### Copy Your Docker Image

Copy your Docker image to the EC2 instance. You can use `scp` or other methods to transfer the image.

### Run the Docker Container on EC2

Run the Docker container on your EC2 instance:

```bash
docker run -d -p 80:8000 your-django-todo-list-app-image
```





