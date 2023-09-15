# Day 25 of 100DaysofCode

Feeling excited to start Day 25 of 100 DaysOfCode, today, I built a Dockerfile for a 2048 game and continued gitlab course video by [FreeCodeCamp](https://youtu.be/PGyhBwLyK2U?si=eertNUtjOPGNjpno). This part of video provides a beginner guide on Continous Delivery (CD) Pipeline, Enivironments, Aws Elastic 
Beanstack and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-25
```

## 2048-Game Dockerfile

```markdown
# Dockerfile Explanation

This README provides an explanation of the Dockerfile used to create a Docker image for running a simple web server that serves the popular game "2048" from GitHub using Nginx.

## Dockerfile Contents

```Dockerfile
# Use the Ubuntu 22.04 base image
FROM ubuntu:22.04

# Update the package repository
RUN apt-get update

# Install required packages (curl, zip, and nginx)
RUN apt-get install -y curl zip nginx

# Append "daemon off;" to the Nginx configuration to run in the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Download the 2048 game source code from GitHub and unzip it
RUN curl -o /var/www/html/master.zip -L https://codeload.github.com/gabrielecirulli/2048/zip/master
RUN cd /var/www/html && unzip master.zip && mv 2048-master/* . && rm -rf 2048-master master.zip

# Expose port 80 to allow incoming HTTP traffic
EXPOSE 80

# Start Nginx with the custom configuration
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
```

## Dockerfile Explanation

- `FROM ubuntu:22.04`: Specifies the base image as Ubuntu 22.04.

- `RUN apt-get update`: Updates the package repository.

- `RUN apt-get install -y curl zip nginx`: Installs the required packages: `curl` for downloading files, `zip` for handling ZIP archives, and `nginx` for the web server.

- `RUN echo "daemon off;" >> /etc/nginx/nginx.conf`: Appends "daemon off;" to the Nginx configuration file to run it in the foreground.

- `RUN curl -o /var/www/html/master.zip -L https://codeload.github.com/gabrielecirulli/2048/zip/master`: Downloads the 2048 game source code from GitHub.

- The subsequent `RUN` commands unzip the downloaded ZIP archive, move the contents to the web server's root directory, and clean up unnecessary files.

- `EXPOSE 80`: Documents that the container will expose port 80 for incoming HTTP traffic. To publish this port, you would use the `-p` option when running the container.

- `CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]`: Specifies the command to run when the container starts. It starts Nginx with the custom configuration.

## Usage

To build the Docker image:

```bash
docker build -t my-2048-game .
```

To run a container from the image:

```bash
docker run -d -p 80:80 my-2048-game
```

The game should be accessible in a web browser at `http://localhost`.


## Continuous Delivery Pipeline in GitLab

This README provides an explanation of Continuous Delivery (CD) pipelines in GitLab and how they enable automated and efficient software delivery.

## What is Continuous Delivery?

Continuous Delivery (CD) is a software development practice that focuses on automating the software delivery process. It ensures that code changes are automatically built, tested, and deployed to production or staging environments with minimal manual intervention. CD aims to deliver software updates quickly, reliably, and with high quality.

## GitLab CI/CD Pipelines

GitLab offers built-in CI/CD capabilities through its integrated CI/CD platform, which is powered by GitLab CI/CD Runners and configured using `.gitlab-ci.yml` files.

A GitLab CI/CD pipeline is a set of automated processes that run whenever code changes are pushed to a GitLab repository. These processes can include building and compiling code, running automated tests, and deploying the application to various environments, such as development, staging, and production.

## Key Concepts in GitLab CI/CD Pipelines

1. **`.gitlab-ci.yml` file**: The pipeline configuration is defined in a YAML file named `.gitlab-ci.yml`. This file describes the jobs, stages, and rules for your CI/CD pipeline.

2. **Jobs and Stages**: A CI/CD pipeline consists of one or more jobs organized into stages. Jobs are individual tasks or steps that execute specific actions, such as building, testing, or deploying. Stages define the sequence in which jobs are executed.

3. **Runners**: GitLab CI/CD Runners are responsible for executing the jobs defined in the pipeline. Runners can be shared runners provided by GitLab or specific runners set up on your own infrastructure.

4. **Triggers**: Pipelines can be triggered manually by developers, automatically on code pushes, or based on other events such as merge requests or schedules.

## Typical CI/CD Workflow

Here is a typical CI/CD workflow in GitLab:

1. Developers push code changes to a GitLab repository.

2. GitLab CI/CD detects the code changes and triggers a pipeline based on the rules defined in `.gitlab-ci.yml`.

3. The pipeline runs jobs to build, test, and package the application.

4. If all jobs are successful, the pipeline may deploy the application to a staging environment for further testing.

5. If the staging tests pass, the pipeline can automatically deploy the application to production.

## Benefits of GitLab CI/CD Pipelines

- **Automation**: CD pipelines automate the build, test, and deployment processes, reducing manual intervention and human error.

- **Consistency**: Pipelines ensure consistent and repeatable builds and deployments, leading to more reliable software releases.

- **Faster Feedback**: Developers receive quick feedback on code changes through automated testing, helping identify and fix issues early.

- **Visibility**: GitLab provides detailed visibility into pipeline execution, making it easy to track progress and troubleshoot failures.

- **Scalability**: Pipelines can be customized to support complex workflows and accommodate the needs of different projects.

## Environments

In GitLab, "environments" are a feature that allows you to define and manage different deployment targets or execution environments for your application. Environments help you organize and control the deployment of your code to various stages, such as development, testing, staging, and production. They provide a way to promote your application through different stages in your development and release process.

Key features and aspects of GitLab environments include:

1. **Deployment Targets**: Each environment represents a specific deployment target. For example, you might have environments for "Development," "Staging," and "Production."

2. **Protection Levels**: You can set protection levels for environments, specifying who has access to deploy to them and under what conditions.

3. **Automatic Deployments**: GitLab can automatically deploy code to an environment when certain conditions are met, such as successful CI/CD pipeline runs.

4. **Manual Deployments**: You can manually trigger deployments to environments when needed. This can be useful for promoting code to higher-level environments like staging and production.

5. **Environment URL**: You can associate a URL with an environment, making it easy to access the deployed application in that environment directly from GitLab.

6. **Deployment History**: GitLab keeps a history of deployments to each environment, allowing you to track when changes were deployed and by whom.

7. **Integration with CI/CD**: Environments are closely integrated with GitLab's CI/CD pipelines. You can define deployment jobs in your `.gitlab-ci.yml` file that specify how your application should be deployed to different environments.

Here's how environments are typically used in GitLab:

- **Development**: The "Development" environment is often the first environment where code changes are deployed for testing and debugging by developers. It may not be accessible to end-users.

- **Testing**: After successful testing in the development environment, code changes can be promoted to a "Testing" environment for broader testing and validation.

- **Staging**: The "Staging" environment closely resembles the production environment, and it's used for final testing before deploying changes to the production environment. It's typically used for user acceptance testing (UAT) and quality assurance.

## Getting Started

To get started with GitLab CI/CD pipelines, you can:

1. Create a `.gitlab-ci.yml` file in your project repository to define your pipeline stages and jobs.

2. Configure GitLab CI/CD Runners, either using shared runners provided by GitLab or by setting up your own runners.

3. Push code changes to your repository to trigger the pipeline and observe the automated CI/CD process in action.

## AWS Elastic Beanstalk

AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) offering from Amazon Web Services (AWS) that simplifies the deployment, scaling, and management of web applications. It abstracts many of the underlying infrastructure details and allows developers to focus primarily on writing code and deploying their applications without the need to manage servers or infrastructure components.

## Writing a gitlab-ci.yml to host website on AWS Beanstalk

Deploying a website to AWS Elastic Beanstalk (Elastic Beanstalk) using GitLab CI/CD with a Docker image is a common setup. Here's an overview of the steps involved:

1. **Create a Docker Image for Your Website**:
   - In your GitLab repository, create a Dockerfile that defines how to build a Docker image for your website.
   - Use a base image that suits your application stack (e.g., Node.js, Python, Ruby, etc.), install dependencies, and copy your application code into the image.
   - Build the Docker image and push it to a container registry (e.g., Amazon Elastic Container Registry, Docker Hub, GitLab Container Registry).

2. **Set Up Elastic Beanstalk**:
   - Log in to your AWS Management Console and navigate to Elastic Beanstalk.
   - Create an Elastic Beanstalk application and environment. Choose the platform that matches your Docker image (e.g., Multi-container Docker).
   - Configure environment variables and settings as needed for your application.

3. **Configure GitLab CI/CD**:
   - In your GitLab repository, create a `.gitlab-ci.yml` file to define your CI/CD pipeline.
   - Configure CI/CD jobs to build your Docker image, push it to the container registry, and deploy it to Elastic Beanstalk. Here's a simplified example:

   ```yaml
   stages:
     - build
     - deploy

   build:
     stage: build
     script:
       - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG .
       - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG

   deploy:
     stage: deploy
     only:
       - master
     script:
       - EB_ENV_NAME="your-environment-name"
       - EB_APP_NAME="your-application-name"
       - EB_REGION="your-aws-region"
       - aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
       - aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
       - aws elasticbeanstalk create-environment --application-name $EB_APP_NAME --environment-name $EB_ENV_NAME --region $EB_REGION --cname-prefix $EB_ENV_NAME
   ```

   Note: Replace placeholders with actual values for environment, application names, and AWS credentials.

4. **Configure GitLab Variables**:
   - In GitLab CI/CD settings, define CI/CD variables for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to securely store your AWS credentials.
   
5. **Commit and Push**:
   - Commit your `.gitlab-ci.yml` and code changes to your GitLab repository.

6. **CI/CD Execution**:
   - Whenever you push code changes, GitLab CI/CD will automatically execute the pipeline.
   - The pipeline will build the Docker image, push it to the registry, and deploy it to Elastic Beanstalk if the commit is on the master branch (as per the `only` condition in the `.gitlab-ci.yml`).

7. **Monitor Deployment**:
   - Monitor the progress of the deployment in your GitLab CI/CD pipeline logs and the AWS Elastic Beanstalk environment dashboard.

This setup allows you to automate the deployment of your website to AWS Elastic Beanstalk using GitLab CI/CD with Docker images. It ensures that your application is built, tested, and deployed consistently with each code change.

## Resources

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab Runner Documentation](https://docs.gitlab.com/runner/)
- [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)

