# Day 67 of 100DaysOfCode

Feeling excited to start Day 67 of 100 DaysOfCode, today, I completed Episode 5 of 2-Tier Application Deployment by [TrainWithShubham](https://youtu.be/LxPd81wiUP4?si=cXEomQ_O9eTDgZZZ). In this application deployment series, I get to know about the basics of DevOps Practices like Kubernetes Deployment, pushing on dockerHub and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-67
```

## What is HELM?

HELM is a package manager for Kubernetes applications. It simplifies the process of deploying and managing applications on Kubernetes by providing a standardized way to define, package, and deploy applications. HELM packages are called "charts," which are a collection of pre-configured Kubernetes resources.

## Key Components

### 1. Helm CLI

The Helm Command Line Interface (CLI) is the primary tool for interacting with HELM. It provides commands for managing charts, such as installing, upgrading, and uninstalling applications. The Helm CLI is used by developers and operators to streamline the deployment and management of applications on Kubernetes clusters.

```bash
# Example commands
helm install <chart-name>             # Install a chart
helm upgrade <release-name> <chart>   # Upgrade a release
helm uninstall <release-name>         # Uninstall a release
```

### 2. Charts

A chart is a package of pre-configured Kubernetes resources required to run a specific application. It includes YAML manifest files for deploying services, pods, config maps, and other resources. Charts make it easy to share and version application deployments, promoting consistency across different environments.

Charts are organized with the following structure:

```plaintext
my-chart/
  ├── Chart.yaml         # Metadata about the chart
  ├── values.yaml        # Default configuration values
  ├── charts/            # Dependencies on other charts
  ├── templates/         # Kubernetes manifests (YAML files)
  └── ...
```

### 3. Chart Repository

A chart repository is a collection of packaged charts that can be easily shared and distributed. Helm uses repositories to fetch and install charts. Public repositories like Helm Hub (https://hub.helm.sh/) or private repositories can be configured to store and share charts within an organization.

### 4. Release

A release is an instance of a chart deployed on a Kubernetes cluster. Each release has a unique name and is associated with a specific version of the chart. Helm manages releases, making it easy to upgrade, rollback, or uninstall applications.

### 5. Values

Values are configuration parameters that can be customized during the installation of a chart. These parameters are defined in the `values.yaml` file within the chart. Customizing values allows operators to adapt the application to different environments or use cases.

## Getting Started

To start using HELM, follow these basic steps:

1. **Install Helm:** Refer to the official documentation for instructions on installing the Helm CLI on your local machine or cluster.

2. **Create a Chart:** Use the `helm create` command to generate a new chart template. Customize the chart and its values according to your application requirements.

3. **Install a Chart:** Use the `helm install` command to deploy the chart on your Kubernetes cluster. Customize values as needed.

4. **Explore Helm Hub:** Visit Helm Hub to discover and share charts from the Helm community: https://hub.helm.sh/

