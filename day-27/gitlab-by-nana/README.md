# GitLab CI CD Tutorial for Beginners [Crash Course] By TechWorld With Nana

Today, I watched [Gitlab-Course](https://youtu.be/qP8kir2GUgo?si=xClWT_AanV_bQUXt) by <b>TechWorld With Nana</b>. This video contains beginner guide to gitlab documentation, how to write gitlab scripts and many more.

## CI/CD in Simple Words

CI/CD stands for continous integreation and continous deployment | delivery. It involves continous testing -> Building -> Releasing -> Code Changes -> testing process. When developer commits a code, it triggers a pipeline that builds the project and runs some test to ensure that the code changes don't break the project. It is the practice of continously release code changes to end environments. 

## Why Gitlab as CI/CD tool?

GitLab is a popular DevOps platform that offers integrated CI/CD (Continuous Integration/Continuous Deployment) capabilities. When comparing GitLab to other CI/CD tools, such as Jenkins, Travis CI, CircleCI, and others, GitLab has several advantages:

1. **Integrated Solution**: GitLab provides an all-in-one solution for source code management (Git repositories), CI/CD, issue tracking, and more. This integration can simplify the development process, as you don't need to manage multiple tools and integrations.

2. **Single Interface**: GitLab offers a single web interface for all DevOps-related tasks, making it easier for teams to collaborate and manage their projects. This can improve efficiency and reduce the learning curve.

3. **Version Control**: GitLab is built around Git, which is one of the most widely used version control systems. It provides robust version control capabilities, including branching, merging, and code review features.

4. **Built-in CI/CD**: GitLab CI/CD is tightly integrated with the version control system, allowing you to define and manage your CI/CD pipelines within the same platform where your code resides. This streamlines the development workflow.

5. **Auto DevOps**: GitLab's Auto DevOps feature simplifies CI/CD configuration by automatically detecting, building, testing, and deploying applications. This is especially useful for small to medium-sized projects.

6. **Security Scanning**: GitLab includes built-in security scanning tools that can help you identify and address security vulnerabilities in your code and dependencies as part of the CI/CD process.

7. **Scalability**: GitLab is designed to scale with your organization. It can handle large codebases and complex CI/CD workflows, making it suitable for both small startups and large enterprises.

8. **Self-Managed and Cloud Options**: GitLab offers both self-managed (on-premises) and cloud-hosted versions, providing flexibility for organizations with different infrastructure needs and security requirements.

9. **Extensive Integrations**: While GitLab aims to provide an all-in-one solution, it also offers integrations with other popular tools and services, allowing you to connect it with your existing toolchain if needed.

10. **Active Community and Support**: GitLab has a vibrant community and offers various support options, including paid support plans for enterprises. This ensures you can find help and resources when needed.

11. **CI/CD Pipelines as Code**: GitLab allows you to define your CI/CD pipelines using a configuration file (`.gitlab-ci.yml`), which can be version-controlled along with your code. This approach enables transparent and reproducible pipelines.

12. **Container Registry**: GitLab Container Registry allows you to store and manage Docker images, making it easy to integrate containerization into your CI/CD workflow.

13. **GitLab Runner**: GitLab Runner is an open-source component that handles running your CI/CD jobs. It's compatible with various operating systems and can be easily configured to meet your specific needs.

14. **Cost-Effective**: GitLab offers a free version with many features, making it a cost-effective choice for small to mid-sized projects. The paid versions offer additional features and support for larger enterprises.

## Gitlab Architecture 

GitLab is a web-based platform that provides a wide range of features for managing source code repositories, tracking issues, collaborating on software development, and implementing continuous integration/continuous deployment (CI/CD) pipelines. Its architecture is designed to support these functionalities efficiently. Here's an overview of the GitLab architecture:

- Web Server:
    The web server component of GitLab is responsible for handling HTTP requests and serving the GitLab web interface to users. It acts as the gateway for users to interact with their Git repositories, projects, issues, merge requests, and other features provided by GitLab through a web browser.

- GitLab Runner:
    GitLab Runner is an essential component of GitLab's CI/CD functionality. It is responsible for executing CI/CD jobs defined in `.gitlab-ci.yml` configuration files. Each job in the pipeline runs in a separate Runner, which can be installed on various platforms, including Linux, Windows, and macOS.

## Adding Variables for Login Credentials

Adding variables for login credentials in GitLab CI/CD pipelines is a good practice for securely managing sensitive information like usernames and passwords. You can use GitLab CI/CD variables to store and securely manage these credentials. Here's how you can add variables for login credentials:

1. **Access your GitLab project**:
   - Go to your GitLab project where you want to add the CI/CD variables.

2. **Navigate to CI/CD Settings**:
   - Click on "Settings" in the project's sidebar.
   - In the settings menu, select "CI/CD."

3. **Create CI/CD Variables**:
   - Scroll down to the "Variables" section.
   - Click the "Expand" button to reveal the variable configuration options.

4. **Add Variables**:
   - Click the "Add Variable" button to add a new CI/CD variable.
   - You can add multiple variables for different login credentials. For example, you might add variables for a username and a password.

5. **Configure the Variables**:
   - For each variable, provide a name and a value. The name should be descriptive, while the value should contain the actual login credential.
   - You can choose whether the variable is protected or not. Protected variables are only available for protected branches or tags.

6. **Save Variables**:
   - After adding the variables, click the "Add Variable" button to save them.

7. **Use CI/CD Variables in `.gitlab-ci.yml`**:
   - In your GitLab CI/CD pipeline configuration file (usually `.gitlab-ci.yml`), you can reference these variables using the predefined syntax:
   
   ```yaml
   variables:
     USERNAME: $CI_JOB_VARIABLE_NAME
     PASSWORD: $CI_JOB_ANOTHER_VARIABLE
   ```

   - Replace `CI_JOB_VARIABLE_NAME` and `CI_JOB_ANOTHER_VARIABLE` with the actual variable names you created in the GitLab UI.

8. **Use Variables in Your CI/CD Jobs**:
   - You can use these variables in your CI/CD jobs. For example, if you have a job that requires login credentials, you can reference the variables in your script or configuration.

Here's an example of how you might use these variables in a job:

```yaml
my_job:
  script:
    - echo "Username: $USERNAME"
    - echo "Password: $PASSWORD"
    # Use the credentials in your job's script or configuration.
```

## Deploying Application on Gitlab

Deploying an application using GitLab involves setting up a Continuous Integration/Continuous Deployment (CI/CD) pipeline that automates the deployment process whenever changes are pushed to your GitLab repository. Here are the general steps to deploy an application on GitLab:

1. **Create a GitLab Repository**:
   - If you haven't already, create a GitLab repository to host your application code. You can do this by logging into GitLab, selecting a project, and creating a new repository.

2. **Add Your Code**:
   - Push your application code to the GitLab repository. Make sure your codebase is ready for deployment and includes all necessary configuration files.

3. **Set Up CI/CD Pipeline**:
   - Create a `.gitlab-ci.yml` file in the root of your repository. This file defines your CI/CD pipeline configuration. In this file, you'll specify the stages and jobs needed for your deployment process.

   ```yaml
   stages:
     - build
     - deploy

   build:
     stage: build
     script:
       - echo "Build your application here"

   deploy:
     stage: deploy
     script:
       - echo "Deploy your application here"
   ```

   Customize the `script` sections with the commands needed to build and deploy your application.

4. **Define CI/CD Variables**:
   - If your deployment process requires environment-specific configuration or secrets (e.g., database credentials, API keys), define them as CI/CD variables in your GitLab project settings.

5. **Configure Deployment Targets**:
   - Depending on your application and deployment strategy, you may need to configure deployment targets such as servers, containers, or cloud platforms. Ensure that your deployment environment is set up to receive deployments from GitLab CI/CD.

6. **Test the Pipeline Locally**:
   - Before pushing your changes to GitLab, you can test your CI/CD pipeline locally using GitLab Runner to ensure that everything is working as expected.

7. **Push Changes to GitLab**:
   - Commit and push your changes to your GitLab repository. This will trigger the CI/CD pipeline automatically.

8. **Monitor CI/CD Pipeline**:
   - Go to your GitLab project's CI/CD pipeline page to monitor the progress of the pipeline. You should see jobs for building and deploying your application.

9. **Review Logs and Artifacts**:
   - Review the logs generated by your CI/CD jobs for any errors or issues. Artifacts produced during the pipeline (e.g., build artifacts, deployment scripts) can be used for troubleshooting.

10. **Deploy to Production**:
    - Depending on your deployment strategy, you may have a manual approval step to deploy to production. You can use environments in GitLab to manage different deployment stages (e.g., development, staging, production).

11. **Continuous Monitoring and Maintenance**:
    - After deployment, continuously monitor your application in the production environment and perform any necessary maintenance or updates.

12. **Rollbacks and Versioning**:
    - Implement a strategy for rolling back to previous versions in case of issues. You can use GitLab's version control capabilities to manage your application's versions.