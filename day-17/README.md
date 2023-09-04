# Day 17 of 100DaysofCode

Feeling excited to start Day 17 of 100 DaysOfCode, today, I built a simple DevOps project to practice terrafrom in a great Video by [Cloud Champ](https://youtu.be/wFWg0Y68Owo?si=d22UKo57evV13FPQ). This video explains Aws S3 bucket, terraform basics and how does a Real life project works.zz

## Prerequisites

Before you begin, ensure you have the following prerequisites:

1. An AWS account.
2. AWS CLI installed and configured with appropriate access rights.
3. The website files (index.html, error.html, and profile.jpg) you want to host.
4. [Terraform](https://www.terraform.io/downloads.html) installed on your local machine.

## Setup AWS Console and cli

To get started with Python, you need to install it on your system. Here are the steps for installation:

- **Step 1:**  Sign Up for an AWS Account (if not already done) : If you don't already have an AWS account, you'll need to sign up for one on the AWS website.

- **Step 2:** Step 2: Install the AWS CLI: If you haven't already installed the AWS CLI on your local machine, you can download and install it from the official AWS CLI website: https://aws.amazon.com/cli/

- **Step 3:** Configure AWS CLI Access: Open a command prompt or terminal on your local machine and run the following command:

   ```bash
   aws configure
   ```

- You will be prompted to enter the following information:

    - AWS Access Key ID: This is the access key associated with your AWS account. You can generate or retrieve it from the AWS Management Console under IAM (Identity and Access Management) > Users > (Select User) > Security credentials > Access keys.

    - AWS Secret Access Key: This is the secret key associated with the access key. It should be kept secret. You can retrieve it when you create or regenerate an access key in the AWS Management Console.

    - Default region name: Enter the AWS region you want to use as the default. For example, "us-east-1" for the US East (N. Virginia) region.

    - Default output format: You can leave this as the default value (usually "json").

## Project Structure

```bash
project-directory/
│
├── index.html
├── error.html
├── profile.jpg
├── main.tf
├── variables.tf
├── outputs.tf
└── README.md
```

## Deployment Steps

Follow these steps to deploy your static portfolio website on AWS S3 using Terraform:

1. **Clone or Initialize Your Terraform Configuration:**

   Initialize your Terraform configuration by running the following command in your project directory:

   ```bash
   terraform init
   ```

2. Edit `main.tf` (Terraform Configuration):

Customize the main.tf file with your AWS S3 bucket configuration. Here's an example:

    ```bash
    provider "aws" {
    region = "your-preferred-region"
    }

    resource "aws_s3_bucket" "portfolio_bucket" {
    bucket = "your-unique-bucket-name"
    acl    = "public-read"
    }

    resource "aws_s3_bucket_object" "index_html" {
    bucket       = aws_s3_bucket.portfolio_bucket.id
    key          = "index.html"
    source       = "index.html"
    content_type = "text/html"
    }

    # Repeat for error.html and profile.jpg
    ```

3. Deploy Your Terraform Configuration:

    Run the following Terraform commands to apply your configuration:

    ```bash
    terraform plan
    terraform apply
    ```

4. Access Your Portfolio Website:

    Your website is now live at `http://your-unique-bucket-name.s3-website-your-preferred-region.amazonaws.com`.

5. Cleanup (Optional):

    To delete the resources created by Terraform, run:

    `terrafrom destroy`    

## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-17/static-website
terraform init
terraform plan
terraform apply
```
Add a `profile.jpg` file into your project directory

## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
