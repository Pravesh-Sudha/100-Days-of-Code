# Day 100 of 100DaysOfCode

Feeling excited to start Day 100 of 100 DaysOfCode, today, I dived deep into AWS CICD configuration by continuing AWS with day-15 of AWS Bootcamp by [Abhishek Veermalla](https://youtu.be/8ftrKNbSv28?si=R2FuPfekwTxI9Qk1) in which we continued CD part of the AWS project.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-100
```

## Prerequisites

Before proceeding, ensure you have the following:

- An AWS account with permissions to create and manage CodeDeploy applications, EC2 instances, IAM roles, and other necessary resources.
- An EC2 instance running a supported operating system (Linux or Windows) and properly configured for CodeDeploy deployments.
- CodeBuild project configured to build your application code and create an artifact for deployment.
- CodePipeline set up to automate the deployment process, including integration with CodeBuild.

## Setup

Follow these steps to set up the deployment process:

### 1. Configure CodeDeploy Application

- Create a new CodeDeploy application in the AWS Management Console.
- Define a deployment group within the application, specifying deployment type, deployment configuration, and EC2 instances to target.

### 2. IAM Roles

- Ensure that the IAM roles associated with your EC2 instance and CodeDeploy have the necessary permissions.
- The EC2 instance role should allow CodeDeploy to deploy to it, including permissions to download artifacts from Amazon S3.
- CodeDeploy role should allow access to required AWS services like Amazon S3, CloudWatch, and CodeBuild.

### 3. Install CodeDeploy Agent

- Connect to your EC2 instance and install the CodeDeploy agent following the instructions provided by AWS.
- Ensure the CodeDeploy agent is running and has the necessary permissions to execute deployment scripts.

### 4. Update CodeBuild Configuration

- Update your CodeBuild project configuration to produce an artifact that CodeDeploy can use for deployment.
- Make sure the artifact includes all necessary files and dependencies required for your application to run.

### 5. Update CodePipeline Configuration

- Access the CodePipeline console and update your pipeline configuration to include a deployment stage using CodeDeploy.
- Specify the CodeDeploy application and deployment group created earlier in the pipeline configuration.

### 6. Test Deployment

- Trigger a test deployment by pushing changes to your repository or manually starting the pipeline.
- Monitor the deployment progress in the CodeDeploy console or through CloudWatch logs.

## Usage

To deploy code changes to your EC2 instance:

1. Make changes to your application code and commit them to the configured repository.
2. Push the changes to trigger the CodePipeline, which will build the code using CodeBuild and deploy it using CodeDeploy.
3. Monitor the deployment progress in the CodeDeploy console or through CloudWatch logs.

## Troubleshooting

If deployment fails, consider the following troubleshooting steps:

- Check the CodeDeploy logs on the EC2 instance for error messages.
- Review the IAM roles and permissions to ensure the CodeDeploy agent has the necessary permissions to perform deployments.
- Check the CodeBuild configuration to ensure it produces a valid artifact for deployment.

