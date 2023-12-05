# Day 66 of 100DaysOfCode

Feeling excited to start Day 66 of 100 DaysOfCode, today, I completed Episode 4 of 2-Tier Application Deployment by [TrainWithShubham](https://youtu.be/LxPd81wiUP4?si=cXEomQ_O9eTDgZZZ). In this application deployment series, I get to know about the basics of DevOps Practices like Kubernetes Deployment, pushing on dockerHub and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-66
```

# Kubernetes Components Overview

1. [Pod](#pod)
2. [Service](#service)
3. [Deployment](#deployment)
4. [ConfigMap](#configmap)
5. [Secrets](#secrets)

## Pod

A **Pod** is the smallest deployable unit in Kubernetes, representing a single instance of a running process. Pods encapsulate one or more containers, sharing the same network namespace and storage.

- **Use Cases:**
  - Running a single-container application.
  - Running sidecar containers that enhance the main container.

- **Example Pod Definition:**
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: example-pod
  spec:
    containers:
    - name: main-container
      image: nginx:latest
  ```

## Service

A **Service** is an abstraction that defines a set of Pods and provides a stable endpoint to access them. It enables load balancing and service discovery within the Kubernetes cluster.

- **Use Cases:**
  - Exposing applications to the external world.
  - Load balancing traffic between Pods.

- **Example Service Definition:**
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: example-service
  spec:
    selector:
      app: example-app
    ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  ```

## Deployment

A **Deployment** manages the deployment and scaling of Pods. It allows you to describe the desired state of your application and automatically handles updates and rollbacks.

- **Use Cases:**
  - Rolling out application updates.
  - Scaling applications up or down.

- **Example Deployment Definition:**
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: example-deployment
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: example-app
    template:
      metadata:
        labels:
          app: example-app
      spec:
        containers:
        - name: main-container
          image: nginx:latest
  ```

## ConfigMap

A **ConfigMap** is used to decouple configuration artifacts from Pod definitions. It provides a way to inject configuration data into applications.

- **Use Cases:**
  - Storing configuration parameters.
  - Updating configurations without changing Pod definitions.

- **Example ConfigMap Definition:**
  ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: example-configmap
  data:
    app_config: |
      key1: value1
      key2: value2
  ```

## Secrets

A **Secret** is similar to ConfigMap but specifically designed to store sensitive information such as passwords, API keys, and tokens.

- **Use Cases:**
  - Storing confidential data securely.
  - Providing a way to inject sensitive information into Pods.

- **Example Secret Definition:**
  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: example-secret
  type: Opaque
  data:
    username: dXNlcm5hbWU=
    password: cGFzc3dvcmQ=
  ```

