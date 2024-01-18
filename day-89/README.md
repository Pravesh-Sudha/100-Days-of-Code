# Day 89 of 100DaysOfCode

Feeling excited to start Day 89 of 100 DaysOfCode, today, I dived deep into Github Actions by following along with [Abhishek Veeramalla](https://youtu.be/K3RqgDPCjYs?si=RHWzjNJWQhkU0lkk) in which he explained Github actions from beginner to advance level.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-89
```

# GitHub Actions CI/CD Workflow Readme

## GitHub Actions

GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) and automation platform provided by GitHub. It allows you to automate various tasks in your software development lifecycle directly from your GitHub repository. Actions are defined in YAML files within the `.github/workflows` directory.

## Use Cases

GitHub Actions can be used for a variety of tasks, including:

- **Continuous Integration:** Automatically build and test your code on each push to the repository.
  
- **Continuous Deployment:** Automate the deployment of your application to different environments.

- **Automated Testing:** Run various types of tests, such as unit tests, integration tests, and end-to-end tests.

- **Code Quality:** Integrate code quality tools to analyze and report code quality metrics.

- **Containerization:** Build and push Docker images, deploy to container orchestration platforms like Kubernetes or Docker Swarm.

## Advantages over Jenkins

GitHub Actions has some advantages over Jenkins:

1. **Native Integration:** GitHub Actions is tightly integrated with GitHub repositories, making it easier to set up and manage workflows.

2. **YAML Configuration:** GitHub Actions uses simple YAML files for workflow configuration, making it easy to version control and manage as code.

3. **Scoped Environments:** Environments, secrets, and permissions are managed within the GitHub repository itself, simplifying access control.

4. **Free Tier:** GitHub Actions offers a generous free tier for public repositories and provides a substantial number of free minutes for private repositories.

5. **Ecosystem:** GitHub Actions has a growing marketplace with pre-built actions for common tasks, making it easier to leverage community contributions.

## Workflows Overview

### 1. `deploy-java-with-maven-sonar-k8s.yml`

This workflow performs an end-to-end CI/CD for a Java application with Maven, SonarQube analysis, and Kubernetes deployment.

- **Build Job (`build`):**
  - Checks out the code.
  - Sets up Java JDK.
  - Builds the Maven project.
  - Performs SonarQube analysis.

- **Deploy Job (`deploy`):**
  - Depends on the `build` job.
  - Checks out the code again.
  - Deploys the application to Kubernetes using the specified manifests.

### 2. `deploy-to-k8s.yml`

This workflow deploys a Dockerized application to Kubernetes.

- **Deploy Job (`deploy`):**
  - Checks out the code.
  - Builds and pushes the Docker image.
  - Deploys the application to Kubernetes using the specified deployment YAML.

### 3. `deploy-to-swarm.yml`

This workflow deploys a Dockerized application to Docker Swarm.

- **Deploy Job (`deploy`):**
  - Checks out the code.
  - Builds and pushes the Docker image.
  - Deploys the application to Docker Swarm using the specified stack YAML.

## Environment Variables

- **Common:**
  - `KUBECONFIG`: Kubernetes configuration file path.
  - `DOCKER_REGISTRY_PASS`: Docker registry password.

- **`deploy-java-with-maven-sonar-k8s.yml`:**
  - `SONAR_TOKEN`: SonarQube token.

- **`deploy-to-swarm.yml`:**
  - `DOCKER_HOST`: Docker Swarm manager address.
  - `DOCKER_REGISTRY_USER`: Docker registry username.

## Note

Make sure to replace placeholder values such as `<name of your org>`, `<key>`, `<name>`, `<ip-address-of-your-swarm-manager>`, `<username>`, `<registry-username>`, `<image-name>`, `<stack-name>`, etc., with your actual configuration.

Feel free to customize these workflows according to your specific project requirements.