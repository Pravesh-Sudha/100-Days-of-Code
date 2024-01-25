# Day 95 of 100DaysOfCode

Feeling excited to start Day 95 of 100 DaysOfCode, today, I dived deep into ArgoCd by watching ArgoCd course by [Abhishek Veermalla](https://youtu.be/eqiqQN1CCmM?si=Npa5nCQXTWySyHZj) in which he explained the ArgoCD completely from starting till end along with practical demo.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-95
```
    
## Overview:

This README file provides comprehensive information about GitOps, Argo CD, their architecture, installation guide, login process into Argo CD, using Minikube as the default cluster, advantages of using Argo CD, and the advantages of adopting GitOps methodology.

---

## What is GitOps?

GitOps is a methodology for managing and automating the deployment and operation of applications and infrastructure using Git repositories as the single source of truth. It emphasizes declarative configuration and automation through version-controlled manifests.

---

## What is Argo CD?

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It provides a user-friendly web interface and a CLI to manage and deploy applications on Kubernetes clusters.

---

## Architecture:

Argo CD architecture consists of the following components:

- **Application Controller**: Reconciles the desired state in Git with the observed state of the Kubernetes cluster.
  
- **API Server**: Exposes a REST API to interact with Argo CD.
  
- **Repo Server**: Manages the Git repositories containing the application manifests.
  
- **Dex (Optional)**: Provides authentication and authorization services.
  
- **Redis (Optional)**: Used for caching and maintaining the application state.
  
- **Kubernetes Cluster**: The target cluster where applications are deployed and managed.

---

## Installation:

### Prerequisites:

- **Kubernetes Cluster**: Ensure you have a Kubernetes cluster set up (e.g., Minikube).
  
- **kubectl**: Install the Kubernetes command-line tool.
  
- **Helm**: Install Helm package manager.

### Installation Steps:

1. Install Argo CD using Helm:

   ```
   helm repo add argo https://argoproj.github.io/argo-helm
   helm install argocd argo/argo-cd
   ```

2. Port forward the Argo CD API server:

   ```
   kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```

3. Access Argo CD UI:

   Open a web browser and navigate to `https://localhost:8080` to access the Argo CD UI.

---

## Log into Argo CD:

1. Retrieve the default admin password:

   ```
   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
   ```

2. Log in using the admin username (default: `admin`) and the password obtained in the previous step.

---

## Using Minikube as the Default Cluster:

To use Minikube as the default cluster for Argo CD, ensure that Minikube is running and the `kubectl` context is set to Minikube.

```
minikube start
kubectl config use-context minikube
```

---

## Advantages of Using Argo CD:

- **Declarative Configuration**: Define desired state in Git repositories.
  
- **Automated Synchronization**: Argo CD continuously monitors and synchronizes the actual state with the desired state.
  
- **Web UI and CLI**: Provides both a user-friendly web interface and a CLI for managing applications.
  
- **Rollback**: Supports easy rollback to previous versions of applications.

---

## Advantages of GitOps:

- **Version Control**: Leverages Git for versioning and auditing changes.
  
- **Consistency**: Ensures consistency across environments by using the same configuration for development, staging, and production.
  
- **Collaboration**: Facilitates collaboration among teams by using Git workflows.
  
- **Auditing and Compliance**: Enables auditing and compliance checks through version-controlled configuration.

---

## Conclusion:

This README file provides an overview of GitOps, Argo CD, their architecture, installation guide, login process into Argo CD, using Minikube as the default cluster, advantages of using Argo CD, and the advantages of adopting GitOps methodology. Follow the instructions provided to get started with GitOps and Argo CD.