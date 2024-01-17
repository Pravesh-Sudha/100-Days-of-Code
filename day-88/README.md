# Day 88 of 100DaysOfCode

Feeling excited to start Day 88 of 100 DaysOfCode, today, I dived deep into Terraform by following along with [Abhishek Veeramalla](https://youtu.be/NLmF64KdLN0?si=ZbHuMuTQPze8tMiK) in which he explained terraform from beginner to advance level.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-88
```

# Terraform 

## Overview

This README provides essential information for DevOps engineers and developers to effectively use Terraform for infrastructure provisioning and management.

### Terraform Use-Cases

Terraform is a versatile Infrastructure as Code (IaC) tool, widely used for:

1. **Provisioning Infrastructure**: Create and manage infrastructure resources across various cloud providers and on-premises environments.

2. **Configuration Management**: Define and maintain the desired state of infrastructure using code.

3. **Multi-Cloud Management**: Manage resources across different cloud providers using a single configuration.

4. **Collaborative Infrastructure**: Share and collaborate on infrastructure configurations using version control systems.

5. **Continuous Integration/Continuous Deployment (CI/CD)**: Integrate Terraform into your CI/CD pipelines to automate infrastructure deployment.

### Terraform Life Cycle

Terraform follows a typical life cycle:

1. **Initialization (`terraform init`)**: Download and configure providers and modules.

2. **Planning (`terraform plan`)**: Preview changes before applying them.

3. **Apply (`terraform apply`)**: Apply changes to create or update infrastructure.

4. **Destroy (`terraform destroy`)**: Destroy resources created by Terraform.

### Write Your First Terraform Project

To start your first Terraform project:

1. Install Terraform by downloading it from [terraform.io](https://www.terraform.io/downloads.html).
2. Create a new directory for your project.
3. Create a `.tf` file with your infrastructure configuration.
4. Initialize the project with `terraform init`.
5. Preview the changes with `terraform plan`.
6. Apply the changes with `terraform apply`.

### Terraform State File

Terraform uses a state file to store the current state of managed infrastructure. Best practices include:

- **Remote State Storage**: Store the state file remotely to enable collaboration and versioning.
- **State Locking**: Implement state locking mechanisms to prevent concurrent modifications.

### Terraform Best Practices

Follow these best practices for effective Terraform usage:

1. **Modularity**: Use modules to organize and reuse configurations.
2. **Variables and Outputs**: Utilize variables and outputs for dynamic and reusable configurations.
3. **Version Control**: Store configurations in version control systems for collaboration and history tracking.
4. **Provider Configuration**: Use provider configuration files to manage multiple environments.
5. **Documentation**: Document your configurations and use descriptive names.

### Terraform Modules

Modules enable the reuse of configurations. Create modular configurations for specific functionalities, making it easier to maintain and share.

### Problems with Terraform

Some common challenges with Terraform include:

1. **State Management**: Handling and versioning of the state file.
2. **Dependencies**: Managing dependencies between resources.
3. **Provider Limitations**: Not all providers support all features equally.

### Terraform Interview Questions

Prepare for Terraform interviews by understanding:

1. **Terraform Basics**: Lifecycle, state file, providers, and resources.
2. **Modules and Reusability**: How to create and use modules.
3. **Best Practices**: Demonstrating knowledge of Terraform best practices.
4. **Real-world Scenarios**: Solving problems related to infrastructure provisioning and management.
