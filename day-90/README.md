# Day 90 of 100DaysOfCode

Feeling excited to start Day 90 of 100 DaysOfCode, today, I dived deep into Github Actions by following along with [Abhishek Veeramalla](https://youtu.be/K3RqgDPCjYs?si=RHWzjNJWQhkU0lkk) in which he explained Github actions self hosted runners and created a project for it.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-90
```

## Prerequisites

Before getting started, ensure you have the following prerequisites:

1. **GitHub Repository**: Create a GitHub repository for your Python project.

2. **AWS Account**: You need an AWS account with the necessary permissions to create and manage EC2 instances.

3. **EC2 Instance**: Launch an EC2 instance that will serve as the self-hosted runner. Make sure to configure security groups and IAM roles appropriately.

4. **GitHub Token**: Generate a GitHub personal access token with the `repo` and `workflow` scopes. This token will be used to authenticate the self-hosted runner with GitHub.

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Pravesh-Sudha/simple-go-server.git
cd simple-go-server/
```

### 2. Create GitHub Secrets

In your GitHub repository, navigate to "Settings" > "Secrets" and add the following secrets:

- `AWS_ACCESS_KEY_ID`: AWS access key with EC2 permissions.
- `AWS_SECRET_ACCESS_KEY`: AWS secret access key corresponding to the access key.
- `AWS_REGION`: AWS region where your EC2 instance is located.
- `GITHUB_TOKEN`: GitHub personal access token.

### 3. Update GitHub Actions Workflow

Edit the `.github/workflows/your-filename.yml` file to customize the workflow according to your project requirements. Update the following placeholders:

- Replace `runs-on: ubuntu-latest` with the `self-hosted`.
- Configure your Instance with by running commands from `https://github.com/your-username/repo-name/settings/actions/runners/new`.

### 4. Commit and Push Changes

```bash
git add .
git commit -m "Add GitHub Actions workflow for deployment"
git push
```

## Workflow Description

The GitHub Actions workflow is triggered on each push to the repository. It performs the following steps:

1. **Checkout Code**: Checks out the latest version of your code.
2. **Set up Go**: Configures the Python environment.
3. **Install Dependencies**: Installs project dependencies using `go`.
4. **Deploy to EC2**: Uses SSH to connect to the EC2 instance and deploys the go project.

## Monitoring and Troubleshooting

- Monitor workflow runs in the "Actions" tab of your GitHub repository.
- Check the runner logs on the EC2 instance for detailed information in case of failures.

## Conclusion

This GitHub Actions setup provides an automated and integrated way to deploy your go project on an EC2 instance. Tailor the workflow to match your project's specific needs and architecture.