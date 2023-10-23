# Day 48 of 100DaysofCode

Feeling excited to start Day 48 of 100 DaysOfCode, today, I learned about AWS Lambda in an amazing beginner friendly project. This project provides a beginner guide to AWS, its services like aws lambda, how to setup your CLI and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-48
```

## What is AWS Lambda?

According to the docs, AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS). It allows you to run code without provisioning or managing servers, making it a key component of serverless architecture. With AWS Lambda, you can execute code in response to events and triggers without worrying about the underlying infrastructure. Here are some key features and use cases of AWS Lambda:

1. Event-Driven Execution: AWS Lambda can be triggered by a variety of events, such as changes to data in an S3 bucket, updates to a database, API Gateway requests, or scheduled tasks. When an event occurs, Lambda automatically executes the code you've configured to handle that event.

2. Pay-as-You-Go Pricing: With AWS Lambda, you pay only for the compute time your code actually runs. There are no upfront costs, and you're not charged when your code is not running.

3. Auto-Scaling: Lambda automatically scales to handle the number of incoming requests. You don't need to worry about provisioning servers or managing infrastructure, as AWS takes care of this for you.

4. Language Support: AWS Lambda supports multiple programming languages, including Node.js, Python, Java, C#, Ruby, and more, allowing you to use the language that best suits your application.

5. Statelessness: Lambda functions are stateless, meaning they don't retain information between invocations. Any data that needs to be stored should be done in external services like Amazon S3 or databases.

6. Easy Integration: AWS Lambda can be integrated with other AWS services, making it a powerful tool for building serverless applications. It can also be used in conjunction with Amazon API Gateway for building serverless APIs.

7. Customizable Resource Allocation: You can specify the amount of memory and CPU allocated to a Lambda function, allowing you to optimize performance and cost based on your application's needs.

## Creating a Lambda Function from the Management Console

**Prerequisites**

- An AWS account with the necessary permissions to create Lambda functions.
- Basic familiarity with AWS services and the AWS Management Console.

### Step 1: Sign In to the AWS Management Console

1. Open your web browser and go to the [AWS Management Console](https://aws.amazon.com/console/).
2. Sign in with your AWS account credentials.

### Step 2: Navigate to AWS Lambda

1. Once you're logged in, search for "Lambda" in the AWS Management Console's search bar.
2. Click on "Lambda" under the "Compute" category.

### Step 3: Create a New Lambda Function

1. In the Lambda dashboard, click the "Create function" button.

### Step 4: Configure Your Lambda Function

1. Choose "Author from scratch."
2. Fill in the basic information for your function:
   - **Function name:** Enter a name for your Lambda function.
   - **Runtime:** Choose the runtime environment for your code (e.g., Node.js, Python, Java, etc.).
   - **Execution role:** Create a new role or use an existing role with permissions for your function.
3. Click the "Create function" button.

### Step 5: Configure Your Function Code

1. In the "Function code" section, you can either upload a .zip file with your code or edit code inline.
2. Write or upload the code for your Lambda function.
3. Configure your function's handler, runtime settings, and other details.

### Step 6: Set Up Your Function Trigger

1. In the "Add triggers" section, you can add an event source that will trigger your Lambda function (e.g., an S3 bucket, an API Gateway, etc.).
2. Configure the trigger settings as needed.

### Step 7: Review and Create

1. Review the configuration of your Lambda function to ensure it's correct.
2. Click the "Create function" button to create your Lambda function.

### Step 8: Test Your Lambda Function

1. In the Lambda function details, you can click the "Test" button to test your function with sample data.
2. Observe the execution results in the console.


