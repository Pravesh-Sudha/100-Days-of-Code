# Day 24 of 100DaysofCode

Feeling excited to start Day 24 of 100 DaysOfCode, today, I continued gitlab course video by [FreeCodeCamp](https://youtu.be/PGyhBwLyK2U?si=eertNUtjOPGNjpno). This part of video provides a beginner guide on how to structure your gitlab CI pipeline, aws fundamentals and its CLI along with its important services like S3 buckets (Simple Storage Service).

## Usage

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-24
```

## Structuring Pipeline

Structuring a pipeline in GitLab involves defining the stages, jobs, and tasks that make up your continuous integration and continuous deployment (CI/CD) process. GitLab provides a flexible YAML configuration file called `.gitlab-ci.yml` to define your pipeline. Here's a basic guide on how to structure a pipeline in GitLab:

1. **Create a `.gitlab-ci.yml` file**:

   Start by creating a `.gitlab-ci.yml` file in the root of your GitLab repository. This file will define your pipeline's structure and behavior.

2. **Define Stages**:

   A pipeline typically consists of stages, which represent different phases of your CI/CD process (e.g., build, test, deploy). Define your stages using the `stages` keyword:

   ```yaml
   stages:
     - build
     - test
     - deploy
   ```

3. **Define Jobs**:

   Inside each stage, you define jobs. A job is a specific task or set of tasks that need to be executed within a stage. Each job can run in a separate environment or container. Define your jobs using the `jobs` keyword:

   ```yaml
   build_job:
     stage: build
     script:
       - echo "Building the application"

   test_job:
     stage: test
     script:
       - echo "Running tests"

   deploy_job:
     stage: deploy
     script:
       - echo "Deploying to production"
   ```

   In this example, there are three jobs - one for building the application, one for running tests, and one for deployment.

4. **Specify Runner and Environment**:

   You can specify the runner (executor) and environment for each job using the `tags` and `environment` keywords:

   ```yaml
   build_job:
     stage: build
     script:
       - echo "Building the application"
     tags:
       - docker
     environment:
       name: development
       url: https://dev.example.com
   ```

   In this example, the job is tagged to run on a runner with the `docker` tag, and it's associated with the `development` environment.

5. **Define Variables**:

   You can define environment-specific variables or job-specific variables using the `variables` keyword:

   ```yaml
   build_job:
     stage: build
     script:
       - echo "Building the application"
     variables:
       DATABASE_URL: "postgres://user:password@db.example.com/mydb"
   ```

6. **Artifacts and Dependencies**:

   If a job generates artifacts (e.g., compiled binaries), you can define them using the `artifacts` keyword. You can also specify job dependencies using the `dependencies` keyword:

   ```yaml
   test_job:
     stage: test
     script:
       - echo "Running tests"
     dependencies:
       - build_job
     artifacts:
       paths:
         - test-results/
   ```

   In this example, the `test_job` depends on the successful completion of the `build_job`, and it also collects test results as artifacts.

7. **Triggering the Pipeline**:

   Once you've defined your `.gitlab-ci.yml` file, whenever you push changes to your GitLab repository, GitLab CI/CD will automatically trigger a pipeline based on the configuration.

8. **Review and Monitor**:

   You can review the pipeline's progress and results in the GitLab CI/CD interface, which provides detailed information about each job and stage.

Remember to adapt the pipeline structure to your specific project requirements. GitLab CI/CD offers a wide range of features and flexibility, including conditional jobs, manual actions, and more, so you can tailor your pipeline to fit your needs.

To disable a job, simply write a dot `.` in front of job name, for example:

 ```yaml
   .build_job:
     stage: build
     script:
       - echo "Building the application"
 ```      

## AWS

Amazon Web Services (AWS) is a cloud computing platform offered by Amazon. It provides a wide range of services, including computing power, storage, databases, machine learning, analytics, and more, which allow organizations to build and run applications in a scalable and cost-effective manner.

Here's a quick introduction to some key AWS concepts and components: AWS CLI, IAM (Identity and Access Management), and S3 (Simple Storage Service).

1. **AWS CLI (Command Line Interface)**:

   - AWS CLI is a command-line tool that allows you to interact with AWS services from your local terminal or command prompt.
   - You can use AWS CLI to manage AWS resources, create and configure services, and automate tasks.
   - To get started, you'll need to install the AWS CLI on your local machine and configure it with your AWS credentials (access key and secret key).

2. **IAM (Identity and Access Management)**:

   - IAM is a service that enables you to manage access to AWS resources securely.
   - With IAM, you can create and manage users, groups, and roles, and define what actions they are allowed to perform on specific AWS resources.
   - IAM allows you to set fine-grained permissions, ensuring that only authorized individuals or applications can access your AWS resources.

3. **S3 (Simple Storage Service)**:

   - Amazon S3 is an object storage service that allows you to store and retrieve data, such as files, documents, images, and videos.
   - It provides highly scalable and durable storage with a pay-as-you-go pricing model.
   - S3 uses a flat namespace and organizes data into buckets, which are similar to folders.
   - Each object (file) in S3 is associated with a unique URL and can be accessed via a RESTful API.
   - S3 offers features like versioning, data lifecycle policies, access control, and data encryption for enhanced data management and security.

Here's a brief example of using AWS CLI with IAM to interact with S3:

- Create an S3 bucket using AWS CLI:
  ```bash
  aws s3 mb s3://my-new-bucket-name
  ```

- Upload a file to the bucket:
  ```bash
  aws s3 cp my-file.txt s3://my-new-bucket-name/
  ```

- List objects in the bucket:
  ```bash
  aws s3 ls s3://my-new-bucket-name/
  ```

- IAM can be used to control who can perform these actions, ensuring secure access to S3 resources.

AWS is a vast ecosystem with many services, and this introduction barely scratches the surface. However, these fundamental concepts are essential to getting started with AWS, IAM, and S3, which are often building blocks for more complex cloud architectures and applications.

## Uploading File to Aws S3

To upload files to an AWS S3 bucket using GitLab, you can utilize GitLab CI/CD pipelines in conjunction with the AWS CLI or AWS S3 SDK for the programming language of your choice. Here's a step-by-step guide:

### Prerequisites:

1. **AWS Account:** You need an AWS account with appropriate permissions to access the S3 bucket.

2. **GitLab Repository:** You should have a GitLab repository where you want to automate the file upload process.

3. **GitLab Runner:** Ensure that your GitLab project has a GitLab Runner set up and configured. This runner should have access to AWS CLI or SDK for S3.

### Steps:

1. **Configure AWS Credentials:**

   You need to configure AWS credentials in your GitLab Runner environment. You can do this by setting environment variables for your GitLab project:

   - `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID.
   - `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key.
   - `AWS_DEFAULT_REGION`: Your AWS region (e.g., `us-east-1`).

   You can set these environment variables in your GitLab project settings under "CI/CD > Variables."

2. **Create a GitLab CI/CD Pipeline Configuration:**

   In your GitLab repository, create a `.gitlab-ci.yml` file if you don't already have one. This file defines your CI/CD pipeline jobs. Here's a basic example:

   ```yaml
   stages:
     - deploy

   deploy:
     stage: deploy
     script:
       - aws s3 cp local-file.txt s3://your-bucket-name/
     only:
       - master  # Change this branch as needed
   ```

   In the above YAML configuration:

   - `stages` define the stages in your pipeline. In this case, there's only one stage: "deploy."
   - The `deploy` job is responsible for uploading the file to S3 using the AWS CLI.
   - `script` contains the commands to be executed in the job. Replace `local-file.txt` with the path to your local file and `s3://your-bucket-name/` with your S3 bucket's path.
   - The `only` keyword specifies the branch (e.g., `master`) on which this pipeline job should run. Adjust it as needed.

3. **Commit and Push to GitLab:**

   Commit the `.gitlab-ci.yml` file and push it to your GitLab repository.

4. **Run the Pipeline:**

   Once the `.gitlab-ci.yml` file is pushed, GitLab CI/CD will automatically trigger a pipeline when you push changes to the specified branch (`master` in the example). The pipeline job will execute the AWS CLI command to upload the file to the S3 bucket.

5. **Monitor Pipeline Execution:**

   You can monitor the pipeline's progress and view logs in the GitLab CI/CD section of your GitLab project.

## Hosting Website

Hosting a website on Amazon S3 using GitLab involves several steps, including creating an S3 bucket, configuring static website hosting, and setting up a GitLab CI/CD pipeline to deploy your website automatically. Here's a step-by-step guide:

1. **Create an S3 Bucket:**

   - Log in to your AWS Management Console.
   - Navigate to the S3 service.
   - Click "Create Bucket."
   - Choose a globally unique name for your bucket (e.g., "www.example.com").
   - Select the region that's closest to your target audience.
   - Uncheck "Block all public access" to make your bucket publicly accessible.
   - Create the bucket.

2. **Configure Static Website Hosting:**

   - Inside your S3 bucket, go to the "Properties" tab.
   - Click "Static website hosting."
   - Select "Use this bucket to host a website."
   - Set the "Index document" to the main HTML file (e.g., "index.html").
   - Optionally, set the "Error document" to handle 404 errors.
   - Save the changes.

3. **Upload Website Files to S3:**

   - You can use the AWS CLI or a GitLab CI/CD pipeline to upload your website files to the S3 bucket. Here's an example using GitLab CI/CD:

     In your `.gitlab-ci.yml` file, create a job to deploy your website:

     ```yaml
     stages:
       - deploy

     deploy:
       stage: deploy
       script:
         - aws s3 sync ./path-to-your-website-files/ s3://www.example.com/
       only:
         - master # Change this branch as needed
     ```

     Replace `./path-to-your-website-files/` with the actual path to your website files, and `s3://www.example.com/` with your S3 bucket's URL.

4. **GitLab CI/CD Configuration:**

   - Ensure that your GitLab CI/CD runner has AWS CLI installed and configured with the necessary credentials.

5. **Push Your Code and Trigger the CI/CD Pipeline:**

   - Commit and push your code to the GitLab repository.
   - The CI/CD pipeline will automatically deploy your website to the S3 bucket when you push changes to the specified branch (e.g., `master`).

6. **Access Your Website:**

   - Once the pipeline is successful, your website should be accessible using the S3 bucket's website endpoint (e.g., http://www.example.com.s3-website-us-east-1.amazonaws.com).

7. **Optional: Set Up Custom Domain:**

   - If you have a custom domain, configure the necessary DNS records to point to the S3 bucket's website endpoint. You may also need to set up a CloudFront distribution for SSL support.

8. **Testing and Maintenance:**

   - Continuously test your website after each deployment to ensure it's working as expected.
   - Update your website source code as needed and push changes to GitLab to trigger automatic deployments.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.