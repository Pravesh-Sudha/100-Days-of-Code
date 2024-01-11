# Day 85 of 100DaysOfCode

Feeling excited to start Day 85 of 100 DaysOfCode, today, I dived deep into AWS and docker by  deploying a NodeJS Application on AWS EC2 inctance, So I create an IAM user and ec2 instance and deploy the application on the instance with guidance of [Abhishek Veeramalla](https://youtu.be/NLmF64KdLN0?si=ZbHuMuTQPze8tMiK).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-85
```

# AWS NodeJS Application Deployment

This guide outlines the steps to deploy a NodeJS application on an EC2 instance using AWS services. The process involves creating an IAM user, launching an EC2 instance, cloning a GitHub repository, installing Docker, building a Docker image, tagging it, pushing it to DockerHub, and finally exposing the application port in the security group.

## Prerequisites
1. AWS account with appropriate access.
2. AWS CLI installed and configured.
3. GitHub account.
4. Docker installed on your local machine.

## Step 1: IAM User Setup

Create an IAM user with the following policy attached:
- AmazonEC2FullAccess

Save the access key and secret key generated for the user.

## Step 2: Launch EC2 Instance

Launch an EC2 instance with the following specifications:
- AMI: Ubuntu
- Security Group: Allow inbound traffic on port 22 (SSH) and port 3000 (for the application)

SSH into the instance using the generated key pair.

## Step 3: Clone the GitHub Repository

Clone the GitHub repository containing the NodeJS application:
```bash
git clone https://github.com/verma-kunal/AWS-Session
cd AWS-Session
```

## Step 4: Install Docker

Install Docker on the EC2 instance:
```bash
sudo apt update
sudo apt install docker.io
```

Start and enable Docker:
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

## Step 5: Build and Push Docker Image

Build the Docker image using the provided Dockerfile:
```bash
sudo docker build -t your-dockerhub-username/nodejs-app .
```

Tag the Docker image:
```bash
sudo docker tag your-dockerhub-username/nodejs-app:latest your-dockerhub-username/nodejs-app:1.0
```

Login to DockerHub:
```bash
sudo docker login
```

Push the Docker image to DockerHub:
```bash
sudo docker push your-dockerhub-username/nodejs-app:1.0
```

## Step 6: Expose Port in Security Group

Go to the AWS Management Console, navigate to the EC2 Dashboard, and find the Security Group associated with your EC2 instance.

Edit the inbound rules to allow traffic on port 3000.

## Conclusion

Your NodeJS application is now deployed on an EC2 instance with Docker. The application is accessible at `http://<ec2-public-ip>:3000`. Make sure to replace `<ec2-public-ip>` with the actual public IP address of your EC2 instance.

Note: Keep your AWS credentials and DockerHub credentials secure. This readme assumes a simple setup and may need adjustments based on your specific requirements and security considerations.