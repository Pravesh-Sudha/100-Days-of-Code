# Day 61 of 100DaysofCode

Feeling excited to start Day 61 of 100 DaysOfCode, today, I created a Ansible Playbook Project , in which I get to know about Ansible fundamenatals, how to deploy a webpage and updating the configurations of the servers using playbook and many more with the help of [ShumhamLondhe](https://www.youtube.com/live/yyU2UiNI08M?si=z1uX6BIm_noLXvoD).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-61
```

# Ansible Setup and Configuration Guide

This guide provides step-by-step instructions on setting up Ansible, creating four EC2 Ubuntu instances on AWS, SSHing into the `ansible-master` server, installing Ansible, configuring the `/etc/ansible/hosts` file, and executing basic Ansible commands.

## Prerequisites

1. AWS account with the necessary permissions to create EC2 instances.
2. AWS CLI installed and configured on your local machine.
3. Basic knowledge of AWS services, SSH, and Ansible.

## Step 1: Create EC2 Instances

Use the following AWS CLI commands to create four Ubuntu instances:

```bash
# Replace <your-key-pair> with your existing key pair name
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name <your-key-pair> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=ansible-master}]'
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name <your-key-pair> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=server-1}]'
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name <your-key-pair> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=server-2}]'
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name <your-key-pair> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=server-3}]'
```

![Alt text](<Screenshot from 2023-11-25 12-38-16.png>)

## Step 2: SSH into `ansible-master`

```bash
# Replace <your-key.pem> with the path to your private key
ssh -i <your-key.pem> ubuntu@<ansible-master-public-ip>
```

## Step 3: Install Ansible on `ansible-master`

```bash
sudo apt update
sudo apt install ansible
```

![Alt text](<Screenshot from 2023-11-25 12-47-24.png>)

## Step 4: Configure `/etc/ansible/hosts`

Edit the Ansible hosts file:

```bash
sudo nano /etc/ansible/hosts
```

Add the following content:

```ini
[all:vars]
ansible_private_key_file=/path/to/your/private-key.pem

[servers]
<server-1-private-ip>
<server-2-private-ip>
<server-3-private-ip>
```

Replace `<ansible-master-private-ip>`, `<server-1-private-ip>`, `<server-2-private-ip>`, and `<server-3-private-ip>` with the respective private IP addresses of your instances.

![Alt text](<Screenshot from 2023-11-25 13-09-58.png>)

## Step 5: Basic Ansible Commands

Run basic Ansible commands on the `ansible-master`:

```bash
# Ping all servers
ansible servers -m ping

# Check free memory on all servers
ansible all -a "free -h"

# Update packages on all servers
ansible servers -a "sudo apt update"
```

## Ansible Playbook Example

An Ansible playbook is a collection of tasks to be executed on a set of hosts. Create a simple playbook, e.g., `deploy.yml`:

```yaml
---
-
  name: Install Nginx and Deploy Website on Localhost
  host: servers
  become: yes
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: latest

    - name: Starting Nginx
      service:
        name: nginx
        state: started
        enabled: yes 

    - name: Deploying Website
      copy:
        src: index.html
        dest: /var/www/html  
```

Here is a `date_play.yml` file output:

![Alt text](<Screenshot from 2023-11-25 14-10-11.png>)

### Create a index.html in the same Directory

Here is a sample index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, World!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .container {
            text-align: center;
        }

        h1 {
            color: #333;
            font-size: 3em;
            margin-bottom: 20px;
        }

        p {
            color: #666;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, World!</h1>
        <p>This is a beautiful "Hello, World!" page created by a professional web developer.</p>
    </div>
</body>
</html>

```

Run the playbook:

```bash
ansible-playbook -v depoly.yml
```
