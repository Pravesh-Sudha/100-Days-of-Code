# Day 83 of 100DaysOfCode

Feeling excited to start Day 83 of 100 DaysOfCode, today, I dived deep into Docker and Kubernetes by deploying a reddit clone project, So I wrote a dockerfile and Manifest for the kubernetes minikube that would deploy the Project to minikube Cluster with guidance of [TrainWithShubham](https://youtu.be/9tl0A_rwgu4?si=D2wBrRAYSUxuNsZH).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-83
```

# Reddit Clone Deployment on Kubernetes

## Overview

This project aims to deploy a Reddit clone on Kubernetes using Docker containers. The deployment process involves testing the clone on an EC2 instance, creating a Docker image, pushing it to DockerHub, and finally deploying the application on Kubernetes using deployment and service manifest files.

## Prerequisites

1. **AWS Account**: Ensure that you have an AWS account to create EC2 instances.

2. **Docker**: Install Docker on your local machine. [Docker Installation Guide](https://docs.docker.com/get-docker/)

3. **kubectl**: Install kubectl, the Kubernetes command-line tool. [kubectl Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

4. **AWS CLI**: Install the AWS CLI to manage AWS resources. [AWS CLI Installation Guide](https://aws.amazon.com/cli/)

5. **EC2 Instances**: Create two EC2 instances for testing and deployment.

## Step 1: Testing on EC2 Instance

1.1 **Connect to the EC2 Instance:**
```bash
ssh -i <your-key.pem> ec2-user@<instance-public-ip>
```

1.2 **Clone the Repository:**
```bash
git clone https://github.com/your/reddit-clone.git
cd reddit-clone
```

1.3 **Test the Reddit Clone:**
Follow the instructions provided in the clone's README or documentation to set up and test the application.

## Step 2: Docker Image Creation and Push to DockerHub

2.1 **Build Docker Image:**
```bash
docker build -t your-dockerhub-username/reddit-clone:latest .
```

2.2 **Push to DockerHub:**
```bash
docker login
docker push your-dockerhub-username/reddit-clone:latest
```

## Step 3: Kubernetes Deployment

3.1 **Create Kubernetes Deployment Manifest:**
Create a file named `reddit-clone-deployment.yaml` with the deployment configuration. Refer to the Kubernetes documentation for deployment specifications.

Example:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reddit-clone
spec:
  replicas: 3
  selector:
    matchLabels:
      app: reddit-clone
  template:
    metadata:
      labels:
        app: reddit-clone
    spec:
      containers:
        - name: reddit-clone
          image: your-dockerhub-username/reddit-clone:latest
          ports:
            - containerPort: 3000
```

3.2 **Create Kubernetes Service Manifest:**
Create a file named `reddit-clone-service.yaml` with the service configuration. Refer to the Kubernetes documentation for service specifications.

Example:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: reddit-clone
spec:
  type: NodePort
  selector:
    app: reddit-clone
  ports:
    - port: 3000
      # By default and for convenience, the `targetPort` is set to
      # the same value as the `port` field.
      targetPort: 3000
      # Optional field
      # By default and for convenience, the Kubernetes control plane
      # will allocate a port from a range (default: 30000-32767)
      nodePort: 30007
```

3.3 **Apply Manifests:**
```bash
kubectl apply -f reddit-clone-deployment.yaml
kubectl apply -f reddit-clone-service.yaml
```

## Conclusion

Your Reddit clone is now deployed on Kubernetes using NodePort. Access the application using the NodePort allocated by Kubernetes. Monitor the pods and service to ensure proper functioning.

For additional configurations and optimizations, refer to the Kubernetes documentation and the Reddit clone's documentation.