# Day 80 of 100DaysOfCode

Feeling excited to start Day 80 of 100 DaysOfCode, today, I dived deep into Shell and Shell scripting by making a devops project, So I wrote a shell scripting that would alert me of cost usage of aws resources with guidance of [Abhishek Veermalika](https://youtu.be/gx5E47R9fGk?si=SBcsZKVZLe5nQW1F).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-80
```

# AWS Resource Tracker

This shell script provides a simple solution for tracking AWS resource usage by printing information about S3 buckets, EC2 instances, Lambda functions, and IAM users. The script generates a report and appends it to a file named `resourceTracker`. It is intended to be run on a regular schedule using cron, specifically at 6 PM daily.

## Author
- Pravesh
- Date: 3-Jan
- Version: v1

## Prerequisites
- AWS CLI installed and configured with the necessary permissions.
- jq (a lightweight and flexible command-line JSON processor) installed.

## Usage
1. Make sure the script has execute permissions:
   ```bash
   chmod +x resourceTracker.sh
   ```

2. Add the script to the crontab to run it daily at 6 PM:
   ```bash
   0 18 * * * aws_resource_tracker.sh
   ```
   
   This can be done by using the command:
   ```bash
   crontab -e
   ```

   And then adding the line at the end of the crontab file.

## Script Details

### Script Purpose
The script performs the following actions:

1. **List all S3 Buckets:**
   ```bash
   aws s3 ls > resourceTracker
   ```

2. **List all EC2 Instances:**
   ```bash
   aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId' >> resourceTracker
   ```

3. **List all Lambda Functions:**
   ```bash
   aws lambda list-functions >> resourceTracker
   ```

4. **List all IAM Users:**
   ```bash
   aws iam list-users | jq '.Users[].UserName' >> resourceTracker
   ```

### Notes
- The script uses the `aws` command-line interface to interact with AWS services.
- JSON responses from AWS API calls are processed using `jq`.
- The results are appended to the `resourceTracker` file.
