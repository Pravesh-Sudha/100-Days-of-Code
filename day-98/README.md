# Day 98 of 100DaysOfCode

Feeling excited to start Day 98 of 100 DaysOfCode, today, I dived deep into AWS Code Pieline by practicing AWS with day-12 and 13 of AWS Bootcamp by [Abhishek Veermalla](https://youtu.be/n42nFDTkTCI?si=Q0p_0i32ijV8JTJs) in which we practiced how to use AWS Code Pipeline and leverage its benefits.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-98
```

---

### AWS CodeCommit:

AWS CodeCommit is a fully-managed source control service that makes it easy for teams to host secure and highly scalable Git repositories. It eliminates the need to manage your own source control system or worry about scaling its infrastructure. With features like branching, merging, access control, and integrations with other AWS services, CodeCommit streamlines the code management process for teams of any size.

### AWS CI/CD Pipeline:

AWS CI/CD Pipeline is a fully managed continuous integration and continuous delivery service that automates the build, test, and deployment phases of your release process. It allows you to model, visualize, and automate the steps required to release your software, from committing code changes to production deployment. AWS CI/CD Pipelines integrate seamlessly with other AWS services, such as CodeCommit, CodeBuild, and CodeDeploy, to create a streamlined deployment workflow.

### Jenkins vs. AWS Pipelines:

Jenkins is an open-source automation server that is widely used for building, testing, and deploying software projects. It offers a high degree of flexibility and customization through its extensive plugin ecosystem. On the other hand, AWS Pipelines is a fully managed service provided by AWS that offers similar CI/CD capabilities but with the advantage of seamless integration with other AWS services. While Jenkins requires self-hosting and maintenance, AWS Pipelines abstracts away the infrastructure management overhead, making it easier to set up and manage CI/CD pipelines.

### AWS CodeBuild:

AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces software packages that are ready for deployment. It eliminates the need to provision and manage build servers, allowing you to scale your build infrastructure dynamically based on demand. CodeBuild integrates with other AWS services and supports popular build tools and programming languages, making it easy to automate the build process as part of your CI/CD pipeline.

### AWS CodeDeploy:

AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2 instances, AWS Lambda functions, and on-premises servers. It simplifies the deployment process by providing features like rolling updates, deployment health monitoring, and automatic rollback in case of failures. CodeDeploy integrates with other AWS services and supports a wide range of deployment scenarios, making it suitable for both simple and complex applications.

---

## The Pipeline Process:

1. **CodeCommit Integration**: Developers commit code changes to AWS CodeCommit repositories, which serve as the source control system for the project.

2. **CodeBuild**: Upon code commits, AWS CodeBuild triggers build processes defined in the build specification file (buildspec.yml), which compiles source code, runs tests, and produces artifacts.

3. **CI/CD Pipeline**: AWS CI/CD Pipeline orchestrates the build, test, and deployment phases of the release process. It automatically triggers pipeline execution upon changes in the source code repository.

4. **Deployment Configuration**: AWS CodeDeploy is configured within the pipeline to define deployment strategies, target deployment environments, and specify validation tests.

5. **Deployment Execution**: CodeDeploy deploys the built artifacts to the specified compute services, ensuring seamless and automated deployment of software updates.

6. **Monitoring and Validation**: Deployment health and performance are monitored, and validation tests are executed to ensure the stability and correctness of the deployed application.

7. **Rollback (if necessary)**: In case of deployment failures or issues, AWS CodeDeploy automatically initiates rollback procedures to revert to the previous stable version.

8. **Pipeline Visualization and Management**: The entire CI/CD pipeline process is visualized and managed through the AWS Management Console, providing insights into pipeline execution and performance metrics.

---
