# Day 86 of 100DaysOfCode

Feeling excited to start Day 86 of 100 DaysOfCode, today, I dived deep into KubeADM and kubernetes by deploying a Flask-Mongo Application on KubeADM, So I create two ec2 instance and install kubeadm and establish a relation of master and worker with guidance of [TrainWithShubham](https://youtu.be/LPaWASGjwbs?si=cgr6JMtnZd0Un8Lx).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-86
```

# Kubernetes Project README

This README provides instructions for setting up a Kubernetes cluster on two AWS EC2 instances using kubeadm. The cluster will consist of one master node and one worker node. Additionally, we'll install necessary tools such as kubectl, kubeadm, docker on both instances. Finally, we'll deploy a Flask-MongoDB application using provided manifest files.

## Prerequisites

1. **AWS Account:** Ensure you have an AWS account with the necessary permissions to create EC2 instances.

2. **AWS CLI:** Install the AWS CLI to interact with AWS services.

3. **SSH Key Pair:** Create an SSH key pair and ensure you have the private key.

## Setting up EC2 Instances

1. Create two EC2 instances of type `t2.medium` using the AWS CLI or AWS Console.

2. Obtain the public IP addresses of both instances.

## Installing Kubernetes

### On Master Node

```bash
# Connect to the master node via SSH
ssh -i /path/to/private-key.pem ec2-user@<master-node-public-ip>

# Install kubeadm, kubectl, and kubelet
sudo yum update -y
sudo amazon-linux-extras install docker
sudo amazon-linux-extras enable containerd
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install kubeadm, kubectl, kubelet
sudo amazon-linux-extras install kubernetes1.18
sudo yum install -y kubeadm kubectl kubelet

# Initialize the Kubernetes master
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

Follow the instructions from the output, including running the `kubeadm join` command on the worker node.

### On Worker Node

```bash
# Connect to the worker node via SSH
ssh -i /path/to/private-key.pem ec2-user@<worker-node-public-ip>

# Install kubeadm, kubectl, kubelet
sudo yum update -y
sudo amazon-linux-extras install docker
sudo amazon-linux-extras enable containerd
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install kubeadm, kubectl, kubelet
sudo amazon-linux-extras install kubernetes1.18
sudo yum install -y kubeadm kubectl kubelet
```

Run the `kubeadm join` command obtained from the master node.

## Deploying Flask-MongoDB Application

1. Clone the GitHub repository containing the Kubernetes manifests:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Apply the Kubernetes manifests:

   ```bash
   kubectl apply -f taskmaster.yml
   kubectl apply -f taskmaster-svc.yml
   kubectl apply -f mongo.yml
   kubectl apply -f mongo-svc.yml
   kubectl apply -f mongo-pv.yml
   kubectl apply -f mongo-pvc.yml
   ```

3. Open ports 6443 and 30007 in the security group of the master node to allow communication between the master and worker nodes and to access the NodePort service.

4. Access the Flask-MongoDB application using the worker node's public IP and NodePort (e.g., `http://<worker-node-public-ip>:30007`).

Now, your Kubernetes cluster is set up, and the Flask-MongoDB application is deployed. Feel free to explore and enhance the project as needed.