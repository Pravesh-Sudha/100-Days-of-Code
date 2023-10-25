# Day 49 of 100DaysofCode

Feeling excited to start Day 49 of 100 DaysOfCode, today, I created an AWS DevOps project. This project provides a beginner guide to AWS, its services like aws s3, artifact, codebuild, code commit, code deploy and many more. For referneces, [Watch](https://youtu.be/IUF-pfbYGvg?si=hu1DHRhcbn2rfT6W) the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-49
```

# AWS CodePipeline 

AWS CodePipeline is a fully managed continuous delivery service that helps automate the build, test, and deployment phases of your release process. It enables you to model, visualize, and automate your software release workflows, ensuring reliable and rapid application updates.

CodePipeline is designed to work with other AWS services and third-party tools to create a customizable and efficient release process. It provides flexibility, scalability, and a high degree of automation.

---

## Components

### Source Stage
The Source Stage is the initial step in a CodePipeline. It retrieves source code from a version control system (e.g., AWS CodeCommit, GitHub, or Bitbucket) and makes it available for further processing. Common source providers include:

- **AWS CodeCommit**: A fully managed source control service for hosting Git repositories.
- **GitHub**: A popular web-based platform for version control.
- **Amazon S3**: You can use an Amazon S3 bucket as a source for your pipeline.

### Build Stage
The Build Stage is where your source code is compiled, tested, and packaged into an artifact. Common build tools used include:

- **AWS CodeBuild**: A managed build service that compiles your source code, runs tests, and produces build artifacts.
- **Jenkins**: An open-source automation server that supports building, deploying, and automating any project.

### Test Stage
The Test Stage is responsible for running tests on the artifact produced in the Build Stage. Common testing tools include:

- **AWS CodeBuild**: You can use CodeBuild not only for building but also for running tests.
- **Selenium**: A tool for automating web browsers for testing web applications.
- **Junit**: A popular testing framework for Java applications.

### Deploy Stage
The Deploy Stage takes the tested artifact and deploys it to a target environment. Common deployment tools include:

- **AWS Elastic Beanstalk**: A Platform as a Service (PaaS) that simplifies deploying and managing applications.
- **AWS Lambda**: A serverless compute service that enables running code without provisioning or managing servers.

### Approval Stage
The Approval Stage is an optional step in the pipeline. It allows manual approval before proceeding to the next stage. This is useful for ensuring that human intervention is required before deploying changes to production.

---

## Getting Started

To create your own AWS CodePipeline, follow these general steps:

1. **Sign in to AWS**: Make sure you have an AWS account and sign in to the AWS Management Console.

2. **Create an IAM Role**: You need to set up an IAM role that provides the necessary permissions for your pipeline to interact with AWS services.

3. **Create a CodePipeline**: Go to the CodePipeline service in the AWS Management Console and create a new pipeline. You will configure the stages, source, build, and deployment settings.

4. **Define Your Pipeline Stages**: Configure the stages for your pipeline based on your application's requirements. Common stages include source, build, test, deploy, and approval.

5. **Configure Your Source Provider**: Specify your source code repository (e.g., GitHub, CodeCommit), and configure the source stage settings.

6. **Set Up the Build Stage**: Define your build settings, including the build environment, build commands, and artifact location.

7. **Configure Deployment**: Define how and where your application will be deployed. This may involve setting up deployment actions for AWS services like Elastic Beanstalk or Lambda.

8. **Test and Review**: Review your pipeline configuration and test it by running a sample release.

9. **Trigger Your Pipeline**: CodePipeline can be triggered automatically when changes are detected in the source repository, or manually initiated.

10. **Monitor and Troubleshoot**: Regularly monitor your pipeline for any issues, and use the AWS CloudWatch service for logging and monitoring.

---

## Advanced Features

AWS CodePipeline offers several advanced features, including:

- **Custom Actions**: You can create custom actions using AWS Lambda or third-party tools, allowing for more flexibility in your pipeline.

- **Cross-Region Pipelines**: Set up pipelines that span multiple AWS regions, enabling geographically distributed deployments.

- **Webhooks and Triggers**: Integrate CodePipeline with webhook events and external triggers to initiate pipeline executions.

- **Artifact Caching**: Improve build times by caching build artifacts for reuse in future builds.

- **IAM Permissions**: Fine-tune IAM permissions to ensure a least-privilege model for your pipeline.

---

## Best Practices

- Use Infrastructure as Code (IaC) to define your pipeline. AWS CloudFormation templates or AWS CDK can help maintain your pipeline as code.

- Implement automated testing to catch issues early in the pipeline, reducing the risk of deploying faulty code.

- Use deployment strategies like blue-green or canary deployments to minimize downtime and mitigate risks.

- Set up alarms and monitoring for your pipeline stages to quickly detect and resolve issues.

- Keep your pipeline stages simple and well-segmented to make troubleshooting and scaling easier.

---


