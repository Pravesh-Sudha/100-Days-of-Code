# Day 78 of 100DaysOfCode

Feeling excited to start Day 78 of 100 DaysOfCode, today, I dived deep into Yaml and its Syntax, I feel like revising yaml is important, So I revised its basics with guidance of [Shubhum Londe](https://youtu.be/LFUi5JGr0cE?si=KQOOK88nRyJ8t8u4).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-78
```

# YAML (Yet Another Markup Language)

## What is YAML?

YAML is a human-readable data serialization format. It stands out for its simplicity and readability, making it easy for both humans and machines to understand. YAML is often used for configuration files and data exchange formats where data needs to be represented in a structured manner.

## Use Cases

### 1. Configuration Files

YAML is widely used for configuration files in various applications and systems. Configuration files in YAML are easy to read and write, making them a preferred choice for specifying settings and parameters.

### 2. Data Exchange

YAML serves as a common language for data exchange between different programming languages. Its human-readable syntax allows data to be easily shared and understood across different platforms.

### 3. Automation Scripts

YAML is commonly used in automation scripts, especially in DevOps practices. Tools like Ansible use YAML for defining automation tasks and playbooks, enabling infrastructure as code.

### 4. Kubernetes Manifests

In the world of container orchestration, YAML is extensively used for defining Kubernetes manifests. These manifests describe the desired state of Kubernetes resources such as pods, services, and deployments.

### 5. Continuous Integration/Continuous Deployment (CI/CD) Pipelines

Many CI/CD tools use YAML for pipeline configuration. Build and deployment steps, environment variables, and other pipeline settings are often defined in YAML files.

## YAML Syntax

YAML uses indentation to represent the structure of data. Here are some key syntax rules:

- **Indentation**: Spaces are used for indentation, and the number of spaces must be consistent within a block.

- **Key-Value Pairs**: Data is represented in a key-value format using a colon (`:`).

- **Lists**: Arrays or lists are represented using a hyphen (`-`) followed by a space.

- **Nested Structures**: Indentation is used for nesting structures, and each level of indentation represents a new level in the hierarchy.

### Sample YAML File

```yaml
# Sample YAML Configuration

server:
  name: my_server
  port: 8080

database:
  engine: postgres
  connection:
    host: db.example.com
    port: 5432
    username: admin
    password: secret

users:
  - name: Alice
    age: 30
  - name: Bob
    age: 25
```

This example demonstrates a simple YAML configuration file with a server configuration, database connection details, and a list of users.
