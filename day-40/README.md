# Day 40 of 100DaysofCode

Feeling excited to start Day 40 of 100 DaysOfCode, today, I watched an amazing video on [Jenkins Tutorial – by Nana](https://youtu.be/pMO26j2OUME?si=JcFv8q-9Ec1RwF5S) by <b>TechWorldWithNana</b>. This Video contains beginner guide to Jenkins, and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-40
```

## What is Jenkins?

According to the docs, Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.

Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with a Java Runtime Environment (JRE) installed. Continuous delivery is an approach where teams release quality products frequently and predictably from source code repository to production in an automated fashion.

# Jenkins Pipeline Example

This repository provides a basic example of a Jenkins pipeline defined in a `Jenkinsfile`. Jenkins pipelines are used to automate building, testing, and deploying code. In this example, we'll create a simple pipeline that builds and tests a hypothetical application.

1. Create a `Jenkinsfile` in the root of your application's Git repository. This file defines the steps of your Jenkins pipeline.

   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build') {
               steps {
                   sh 'echo "Building the application..."'
                   sh 'mvn clean package'
               }
           }
           stage('Test') {
               steps {
                   sh 'echo "Running tests..."'
                   sh 'mvn test'
               }
           }
           stage('Deploy') {
               steps {
                   sh 'echo "Deploying the application..."'
                   // Add deployment commands here
               }
           }
       }
   }
    ```

## Understanding the Jenkinsfile

- `pipeline`: Defines the entire Jenkins pipeline.
- `agent any`: Specifies that the pipeline can run on any available agent (Jenkins worker node).
- `stages`: Contains a list of stages to be executed sequentially.
- `stage`: Defines a specific stage within the pipeline.
- `steps`: Contains the commands or steps to be executed within the stage.
- `sh`: Executes shell commands.
- `mvn`: Example command for Maven, replace with your build and test tools.
- The "Build," "Test," and "Deploy" stages are placeholders; customize them according to your project's needs.

# Pros and Cons of Scripted and Declarative Jenkinsfiles

[Jenkins](https://www.jenkins.io/) pipelines can be defined using two main syntaxes: Scripted and Declarative. Both have their advantages and disadvantages, and choosing between them depends on your specific use case and preferences.

## Scripted Jenkinsfile

### Pros:

1. **Flexibility**: Scripted pipelines are highly flexible. You have full control over the build process, which is written in Groovy scripting language. You can execute arbitrary code, integrate external tools, and handle complex build scenarios.

2. **Mature**: Scripted pipelines have been around for a long time and are well-documented. You can find extensive resources, examples, and community support for Scripted pipelines.

### Cons:

1. **Complexity**: Due to their flexibility, Scripted pipelines can become complex and harder to maintain, especially for large and intricate build processes. They may require a deeper understanding of Groovy.

2. **Readability**: Scripted pipelines can be less readable than Declarative pipelines because they involve more Groovy scripting, which can make the pipeline less accessible to non-developers.

## Declarative Jenkinsfile

### Pros:

1. **Simplicity**: Declarative pipelines are designed to be simple and human-readable. They use a structured syntax that makes it easy to define stages and steps without diving into scripting.

2. **Easy to Learn**: Declarative pipelines are easier for beginners to understand. You don't need extensive Groovy knowledge to create them, making them more accessible to a wider audience.

3. **Built-in Syntax Checking**: Jenkins provides built-in syntax checking for Declarative pipelines, helping catch errors early in the development process.

### Cons:

1. **Limited Flexibility**: Declarative pipelines are more opinionated and may not cover all possible build scenarios. For complex or non-standard requirements, you might need to resort to Scripted pipelines.

2. **Less Control**: Declarative pipelines provide less control over the build process. If you need custom logic or complex conditions, you might find it challenging to achieve with Declarative syntax alone.

3. **Limited Reusability**: Reusing parts of a Declarative pipeline in other projects can be challenging, as they are designed to be self-contained.

## Choosing Between Scripted and Declarative Pipelines

- **Use Scripted Pipelines When**: You need complete control over your build process, have complex requirements, and are comfortable with Groovy scripting.

- **Use Declarative Pipelines When**: You want a simpler, more standardized approach that is easier to read and maintain. Declarative pipelines are often a better choice for standard CI/CD workflows.

Ultimately, the choice between Scripted and Declarative pipelines depends on your project's specific needs, your team's expertise, and your preference for a balance between flexibility and simplicity.

