# Day 84 of 100DaysOfCode

Feeling excited to start Day 84 of 100 DaysOfCode, today, I dived deep into Github actions by deploying a portfolio website using Github actions and deploying the website on AWS S3, So I wrote a Workflow with guidance of [TrainWithShubham](https://youtu.be/zPwMnGMEL3Y?si=ZrJ6AGTZwujQ5sOO).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-84
```

# Portfolio Deployment with GitHub Actions

This GitHub Actions workflow automates the deployment of a portfolio website to an Amazon S3 bucket. It is triggered on each push to the `main` branch. The deployment process involves syncing the contents of the repository to the specified S3 bucket.

## Usage

### Step 1: Set up AWS Credentials in GitHub Secrets

Before using this workflow, you need to add your AWS credentials as secrets in your GitHub repository.

1. Navigate to your GitHub repository.
2. Go to the **Settings** tab.
3. In the left sidebar, click on **Secrets**.
4. Click on **New repository secret**.
5. Add the following secrets:

   - `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.

### Step 2: Modify the GitHub Actions Workflow

Edit the `.github/workflows/main.yaml` file in your repository and customize it according to your specific needs. Update the S3 bucket name in the `aws s3 sync` command to match your desired bucket name.

```yaml
name: Portfolio Deployment

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy: 
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v1

    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1

    - name: Deploy static site to S3 bucket
      run: aws s3 sync . s3://YOUR_BUCKET_NAME --delete
```

Replace `YOUR_BUCKET_NAME` with your specific S3 bucket name.

### Step 3: Set Up the S3 Bucket

1. Create an S3 bucket named `pravesh-portfolio-bucket` in the AWS Management Console.
2. Configure the bucket to allow public access by adjusting the bucket policy or access control list (ACL) settings. Make sure not to block public access.
3. Enable static website hosting for the bucket and specify `index.html` as the index document.

## Notes

- This workflow assumes that your portfolio website contains an `index.html` file at the root of the repository.
- Make sure your AWS credentials have the necessary permissions to interact with S3.
- Review and customize the workflow to meet your specific deployment requirements.
- Monitor the workflow runs in the GitHub Actions tab to ensure successful deployments.

Now, with these configurations, your portfolio website will be automatically deployed to the specified S3 bucket whenever changes are pushed to the `main` branch.