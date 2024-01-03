#!/bin/bash

###################
# Author: Pravesh
# Date:  3-Jan
#
# Version: v1
#
# This script will report about Aws Resource Usage
##################

set -x

# AWS S3
# AWS EC2
# AWS Lambda
# AWS IAM

# List all S3 buckets
echo "Printing all the S3 Buckets"
aws s3 ls > resourceTracker

# List all EC2 instances
echo "Printing all the EC2 instance's ID"
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId' >> resourceTracker

# List all Lambda Functions
echo "Printing all the Lambda Functions"
aws lambda list-functions >> resourceTracker

# List all IAM Users
echo "Printing all the IAM User's Name"
aws iam list-users | jq '.Users[].UserName' >> resourceTracker
