# Day 81 of 100DaysOfCode

Feeling excited to start Day 81 of 100 DaysOfCode, today, I dived deep into Kubernetes by Deploying a django to-do project, So I wrote a yaml scripting that would that would help to deploy the application, I did it with guidance of [Abhishek Veermalika and TrainWithShubham](https://youtu.be/6Kax3ZvMOQU?si=s3Y9wbuSRnujuHXk).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-81
```
# Todo App Deployment

## Files

1. **Pod.yaml**
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: todo-app
   spec:
     containers:
     - name: todo-app
       image: pravesh2003/django-proj:v1
       ports:
       - containerPort: 8000
   ```

2. **Deployment.yaml**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: todo-app-deployment
     labels:
       app: todo-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: todo-app
     template:
       metadata:
         labels:
           app: todo-app
       spec:
         containers:
         - name: todo-app
           image: pravesh2003/django-proj:v1
           ports:
           - containerPort: 8000
   ```

## Explanation

### 1. Pod.yaml
- This YAML file defines a Kubernetes Pod named "todo-app."
- It specifies a single container named "todo-app" using the Docker image "pravesh2003/django-proj:v1."
- The container exposes port 8000.

### 2. Deployment.yaml
- This YAML file defines a Kubernetes Deployment named "todo-app-deployment."
- The deployment ensures that there are three replicas of the specified pod template.
- The pod template is defined with the same container specifications as in the Pod.yaml file.
- Labels are used for selector matching between the deployment and pods.

## Deployment Steps

1. Apply the Pod.yaml to create a single pod:
   ```bash
   kubectl apply -f Pod.yaml
   ```

2. Apply the Deployment.yaml to create a deployment with three replicas:
   ```bash
   kubectl apply -f Deployment.yaml
   ```

3. Verify the deployment and pods:
   ```bash
   kubectl get deployments
   kubectl get pods
   ```

4. Access the application by finding the external IP and accessing port 8000.

   **Note:** Additional configurations such as services, ingresses, and database connections may be required based on your specific application requirements.

Now your todo app should be deployed and accessible. Adjust configurations as needed for your environment.