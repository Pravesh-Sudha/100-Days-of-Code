# Day 68 of 100DaysOfCode

Feeling excited to start Day 68 of 100 DaysOfCode, today, I completed Episode 6 and 7 of 2-Tier Application Deployment by [TrainWithShubham](https://youtu.be/LxPd81wiUP4?si=cXEomQ_O9eTDgZZZ). In this application deployment series, I get to know about the basics of DevOps Practices like Kubernetes Deployment, EKS cluster and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-68
```

# IAM
Create a user “eks-admin” with AdministratorAccess
Create Security Credentials Access Key and Secret access key 

# EC2

Create an ubuntu instance (region us-west-2)

ssh to the instance from local

# Install AWS CLI v2
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin --update
```

# Clone the Github Repo
```bash
git clone https://github.com/LondheShubham153/two-tier-flask-app.git
cd two-tier-flask-app/eks-manifests
```

# Setup your access by

`aws configure`

# Install kubectl
```bash
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client
```


# Install eksctl
```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```


# Setup EKS Cluster
```bash
eksctl create cluster --name my-cluster --region us-west-2 --node-type t2.micro --nodes-min 2 --nodes-max 2
aws eks update-kubeconfig --region us-west-2 --name my-cluster
kubectl get nodes
```

# Run Manifests
```bash
kubectl create namespace two-tier-ns
kubectl apply -f .
Kubectl delete -f .
```

# Delete the Cluster
`eksctl delete cluster --name my-cluster --region us-west-2`

