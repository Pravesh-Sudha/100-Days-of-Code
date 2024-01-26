# Day 96 of 100DaysOfCode

Feeling excited to start Day 96 of 100 DaysOfCode, today, I dived deep into ArgoCd by practicing ArgoCd examples from offical [ArgoCd Github Repos](https://github.com/Pravesh-Sudha/argocd-example-apps) in which we practiced how to use argocd as a gitops tool and leverage its benefits.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-96
```

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

## Creating Guestbook Appliaction using Manifest files

Once you are logged in to the ArgoCD server, follow the following steps to create the Guestbook application:

1. Click on New App.
2. Give a Application name like my-first-time   
3. Select default as project name
4. Select Sync policy as Automatic
5. Set the repo url as https://github.com/Pravesh-Sudha/argocd-example-apps
6. Select the path as guestbook
7. Set the default Kubernetes destination and give the namespace as default
8. Hit create and your application will be created.

Now you can try to change deployment file from the kubectl but it will rollback to the specification mentioned in the github repo.



