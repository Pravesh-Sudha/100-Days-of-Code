# Day 76 of 100DaysOfCode

Feeling excited to start Day 76 of 100 DaysOfCode, today, I dived deep into AWS Lambda, Cloudwatch, EBS and Python by building a Python project with guidance of [Abhishek Veeramallia](https://youtu.be/DgavixR_w5Y?si=qbTOwEeViNi2Yfto). In the project, I built a program that trigger a lambda function which convert GP2 type of volume of EBS into GP3.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-76
```

# Amazon CloudWatch and Amazon Elastic Block Store (EBS):

1. **Amazon CloudWatch:**
   - **Purpose:** CloudWatch is a monitoring and management service provided by AWS. It allows you to collect and track metrics, collect and monitor log files, and set alarms. This service provides insights into the performance, health, and resource utilization of your AWS resources and applications.
   - **Key Features:**
     - **Metrics:** CloudWatch provides a wide range of pre-defined metrics for AWS services, such as Amazon EC2, Amazon S3, and more. Additionally, you can create custom metrics.
     - **Alarms:** You can set alarms to be notified when certain thresholds are breached, helping you take automated actions or respond to issues promptly.
     - **Logs:** CloudWatch Logs enables you to centralize logs from your applications, operating systems, and AWS services in one location.

2. **Amazon Elastic Block Store (EBS):**
   - **Purpose:** EBS provides block-level storage volumes for use with Amazon EC2 instances. It offers persistent storage that can be attached to EC2 instances, providing them with durable and high-performance block-level storage.
   - **Key Features:**
     - **Volume Types:** EBS offers different types of volumes optimized for various use cases, such as General Purpose (SSD), Provisioned IOPS (SSD), and Cold HDD.
     - **Snapshots:** You can create point-in-time snapshots of your EBS volumes, which can be used for backup, replication, or creating new volumes.
     - **Encryption:** EBS volumes can be encrypted, providing an additional layer of security for your data at rest.


# AWS Lambda Function for EBS Volume Type Conversion

## Overview

This Python project demonstrates the creation of an AWS Lambda function that triggers when an Elastic Block Store (EBS) volume is created. The Lambda function utilizes Amazon CloudWatch Events to monitor the EBS volume creation event. In this example, we focus on converting EBS volume types from General Purpose SSD (gp2) to General Purpose SSD (gp3).

## Prerequisites

1. **AWS Account:** Ensure you have an AWS account with the necessary permissions to create Lambda functions, CloudWatch Events, and modify EBS volumes.

2. **AWS CLI Configuration:** Configure your AWS CLI with the appropriate credentials by running `aws configure` and providing the required information.

3. **Python Environment:** Make sure you have Python installed on your local machine.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ebs-volume-conversion-lambda.git
   cd ebs-volume-conversion-lambda
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **AWS Lambda Deployment:**
   - Update `lambda_function.py` with any specific logic or modifications you need.
   - Package the Lambda function code:
     ```bash
     zip -r lambda_function.zip lambda_function.py
     ```
   - Deploy the Lambda function using AWS CLI:
     ```bash
     aws lambda create-function \
       --function-name ebsVolumeConversionFunction \
       --runtime python3.8 \
       --role <your-lambda-execution-role-arn> \
       --handler lambda_function.lambda_handler \
       --zip-file fileb://lambda_function.zip
     ```

4. **CloudWatch Event Rule:**
   - Create a CloudWatch Event Rule to trigger the Lambda function when an EBS volume is created.
     ```bash
     aws events put-rule --name EBSVolumeCreationRule --event-pattern "{\"source\": [\"aws.ec2\"],\"detail-type\": [\"AWS API Call via CloudTrail\"],\"detail\":{\"eventName\":[\"CreateVolume\"]}}"
     ```

   - Add permissions to allow the CloudWatch Event Rule to invoke the Lambda function:
     ```bash
     aws lambda add-permission --function-name ebsVolumeConversionFunction --statement-id EBSVolumeConversionPermission --action "lambda:InvokeFunction" --principal events.amazonaws.com
     ```

   - Attach the CloudWatch Event Rule to the Lambda function:
     ```bash
     aws events put-targets --rule EBSVolumeCreationRule --targets "Id"="1","Arn"="<your-lambda-function-arn>"
     ```

5. **Testing:**
   - Create an EBS volume in the AWS Management Console and observe the Lambda function execution in the CloudWatch Logs.

## Additional Notes

- **Lambda Configuration:** Adjust the Lambda function configuration (memory, timeout, etc.) based on your workload requirements.

- **Error Handling:** Implement proper error handling and logging in the Lambda function for debugging and troubleshooting.

- **Cleanup:** To avoid incurring unnecessary costs, delete the Lambda function, CloudWatch Event Rule, and any other resources created during testing when they are no longer needed.

