# Day 73 of 100DaysOfCode

Feeling excited to start Day 73 of 100 DaysOfCode, today, I got my first Fiverr client and I got to know about ACM and Family transfer through it. In the project, I get to know about basics of ACM, Certificate types, family transfer and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-73
```

# AWS Certificate Manager and AWS Transfer Family Integration

## Table of Contents
1. [Introduction](#introduction)
2. [AWS Certificate Manager (ACM)](#aws-certificate-manager)
   - [What is ACM?](#what-is-acm)
   - [Creating a Certificate](#creating-a-certificate)
3. [AWS Transfer Family](#aws-transfer-family)
   - [Overview](#overview)
   - [Setting Up AWS Transfer Family](#setting-up-aws-transfer-family)
4. [Integrating FTPS Server with S3](#integrating-ftps-server-with-s3)
   - [Creating an FTPS Server](#creating-an-ftps-server)
   - [Connecting to S3 Bucket](#connecting-to-s3-bucket)
5. [Conclusion](#conclusion)

## 1. Introduction<a name="introduction"></a>

This README guide provides instructions on integrating AWS Certificate Manager (ACM) and AWS Transfer Family to create a secure FTPS server connected to an Amazon S3 bucket.

## 2. AWS Certificate Manager (ACM)<a name="aws-certificate-manager"></a>

### What is ACM?<a name="what-is-acm"></a>

AWS Certificate Manager is a service that makes it easy to provision, manage, and deploy SSL/TLS certificates for use with AWS services. It simplifies the process of obtaining and renewing SSL/TLS certificates, providing a seamless integration with various AWS resources.

### Creating a Certificate<a name="creating-a-certificate"></a>

To create a certificate using ACM:

1. Navigate to the AWS Management Console.
2. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/).
3. Choose "Request a certificate."
4. Follow the wizard to request a public or private certificate.

   Note: For FTPS, it's recommended to use a wildcard or domain-validated certificate.

## 3. AWS Transfer Family<a name="aws-transfer-family"></a>

### Overview<a name="overview"></a>

AWS Transfer Family is a fully managed service that enables you to transfer files into and out of Amazon S3 using the FTPS, FTP, and SFTP protocols. It provides a secure and scalable solution for file transfer workflows.

### Setting Up AWS Transfer Family<a name="setting-up-aws-transfer-family"></a>

1. Navigate to the AWS Management Console.
2. Open the Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/).
3. Choose "Create server."
4. Configure server settings, including endpoint type, identity provider, and logging.

   Note: For FTPS, select "FTPS" as the protocol.

## 4. Integrating FTPS Server with S3<a name="integrating-ftps-server-with-s3"></a>

### Creating an FTPS Server<a name="creating-an-ftps-server"></a>

1. Follow the steps in the "Setting Up AWS Transfer Family" section to create an FTPS server.
2. Attach the ACM certificate created in the "Creating a Certificate" section to the server.

### Connecting to S3 Bucket<a name="connecting-to-s3-bucket"></a>

1. Access the AWS Transfer Family console.
2. Choose the server created.
3. Configure your server endpoint.
4. In the "Identity provider" section, choose "Custom."
5. Configure the IAM role for the server to access the S3 bucket.
6. Save your configuration.

Now, your FTPS server is set up and connected to the specified S3 bucket securely.

## 5. Conclusion<a name="conclusion"></a>

This guide provides a comprehensive overview of integrating AWS Certificate Manager and AWS Transfer Family to create a secure FTPS server connected to an S3 bucket. Ensure that you follow security best practices and regularly update your certificates for a robust and secure file transfer solution.