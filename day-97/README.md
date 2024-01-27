# Day 97 of 100DaysOfCode

Feeling excited to start Day 97 of 100 DaysOfCode, today, I dived deep into AWS CFT by practicing AWS with day-11 of AWS Bootcamp by [Abhishek Veermalla](https://youtu.be/ov4WmWgQgsA?si=YxdOmK1ErACkXhzJ) in which we practiced how to use and when to use AWS CFT and leverage its benefits.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-97
```
---

### What is CloudFormation (CFT)?

AWS CloudFormation (CFT) is an infrastructure as code (IaC) service provided by Amazon Web Services (AWS). It allows you to define and provision AWS infrastructure and resources in a declarative template format. Instead of manually provisioning each resource, you can use CFT to automate the process, making infrastructure management more efficient, consistent, and scalable.

### Infrastructure as Code (IaC) Principle

IaC is the practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. With CFT, infrastructure can be defined and managed using a template, allowing for version control, consistency, and reproducibility.

### When to Use CloudFormation (CFT)

CloudFormation is beneficial in various scenarios:

- **Repeatable Deployments:** When you need to provision identical or similar infrastructure multiple times, CFT templates provide a consistent and reliable way to achieve this.
- **Scalability:** For dynamically scaling applications or environments, CFT allows you to define scaling policies and resources to handle fluctuating demands.
- **Resource Management:** CFT simplifies the management and tracking of AWS resources, making it easier to understand the relationship between different components of your infrastructure.
- **Change Management:** As infrastructure requirements evolve, CFT templates can be modified and applied to update existing stacks, ensuring changes are implemented consistently across environments.

### Drift Detection

Drift detection in CloudFormation refers to the process of identifying any configuration changes made directly to AWS resources provisioned through a CloudFormation stack, outside the control of the CloudFormation template. This includes manual alterations or modifications made through the AWS Management Console, CLI, or other APIs. Drift detection helps maintain the desired state defined in the template and provides insights into configuration drift for compliance and auditing purposes.

### CloudFormation Template Structure

A CloudFormation template is a JSON or YAML formatted text file that defines the AWS resources and their configurations. The template consists of the following key sections:

- **AWSTemplateFormatVersion:** Specifies the CloudFormation template version.
- **Description:** Provides a description of the template.
- **Parameters:** Defines input parameters for the template.
- **Mappings:** Specifies key-value pairs for resource configuration.
- **Conditions:** Defines conditional statements for resource creation.
- **Resources:** Describes the AWS resources to be provisioned.
- **Outputs:** Defines output values that can be returned.

### Creating Templates in CloudFormation Designer

CloudFormation Designer is a graphical tool provided by AWS to create and modify CloudFormation templates visually. It allows you to visually design templates using drag-and-drop functionality, helping you to visualize the structure and relationships between resources. Once the template is created or modified in the designer, you can export the template in JSON or YAML format for use in CloudFormation.

### Drift Detection

Drift detection in CloudFormation is a feature that allows you to detect any configuration changes made directly to AWS resources provisioned through a CloudFormation stack. By periodically checking for drift, you can ensure that the actual configuration of your resources matches the expected configuration defined in the CloudFormation template. This helps maintain consistency and detect any unauthorized or unexpected changes to your infrastructure.
