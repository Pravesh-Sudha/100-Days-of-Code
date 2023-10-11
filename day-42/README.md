# Day 42 of 100DaysofCode

Feeling excited to start Day 42 of 100 DaysOfCode, today, I watched an amazing video on [Getting Started With Ansible](https://youtube.com/playlist?list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&si=UYA7FzyLue5zXTcL) by <b>Learn Linux TV</b>. This Video contains beginner guide to Ansible, how SSH works with Ansible, basic git commands for ansible and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-42
```

## SSH Key Generation

SSH keys are used for secure authentication when connecting to a remote server. Follow these steps to generate an SSH key pair:

### On Your Local Machine

Open your terminal or command prompt.

1. Generate an SSH key pair using the `ssh-keygen` command:
   ```bash
   ssh-keygen -t id_ed25519 -b 2048
   ```

   You can choose a different encryption algorithm or key size, but id_ed25519 with 2048 bits is more secure.

2. You will be prompted to specify a location for saving the SSH key. Press Enter to accept the default location (usually `/home/username/.ssh/id_rsa` for Linux or `C:\Users\username\.ssh\id_rsa` for Windows).

3. Set a passphrase for added security (optional). It's recommended to use a passphrase, but you can leave it blank for convenience.

Your SSH key pair (public and private keys) has been generated.

## 2. SSH Key Deployment

After generating your SSH key pair, you'll need to deploy the public key to the remote server. This process varies depending on the server's configuration.

### Option 1: Manual Deployment

1. Copy your public key to the server using `ssh-copy-id` (if available) or a simple `cat` command:
   ```bash
   ssh-copy-id user@server
   ```

2. You may need to provide your user's password for authentication.

### Option 2: Manual Copy-Paste

If you cannot use `ssh-copy-id`, manually copy your public key to the server's `~/.ssh/authorized_keys` file. 

## 3. SSH Login

You can now use your SSH key to securely log in to the remote server.

1. Open a terminal on your local machine.

2. Use the `ssh` command to connect to the server:
   ```bash
   ssh user@server
   ```

   Replace `user` with your server username and `server` with the server's hostname or IP address.

3. If you set a passphrase during key generation, you will be prompted to enter it.

You should now be securely connected to the remote server using SSH.

# How to Add SSH Keys in GitHub and Clone Repositories Using SSH Keys

In GitHub, SSH keys provide a secure way to authenticate and interact with your repositories and those of others. This guide will walk you through the process of adding SSH keys to your GitHub account and using them to clone repositories. 

## Table of Contents

1. [Generate SSH Key Pair](#generate-ssh-key-pair)
2. [Add SSH Key to GitHub](#add-ssh-key-to-github)
3. [Clone a Repository Using SSH](#clone-a-repository-using-ssh)

## 1. Generate SSH Key Pair

Before you can use SSH keys with GitHub, you need to generate a key pair (public and private keys). If you already have one, you can skip this step.

### On Linux or macOS

Open a terminal and run the following command, replacing `your_email@example.com` with the email associated with your GitHub account:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Follow the prompts, leaving the passphrase empty if you want to use the key without entering a password.

### On Windows

If you are using Windows, you can generate SSH keys using the Windows Subsystem for Linux (WSL), Git Bash, or a tool like PuTTYgen. We'll assume you're using WSL for this guide.

1. Open WSL and run the same command as for Linux/macOS:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

## 2. Add SSH Key to GitHub

After generating your SSH key pair, you need to add your public key to your GitHub account.

1. Copy the content of your public key to the clipboard:

```bash
cat ~/.ssh/id_rsa.pub
```

2. Log in to your GitHub account.

3. Click your profile picture in the upper-right corner, and select "Settings."

4. In the left sidebar, click on "SSH and GPG keys."

5. Click the "New SSH key" button.

6. Paste your public key into the "Key" field.

7. Give your key a descriptive title in the "Title" field (e.g., "My Laptop SSH Key").

8. Click the "Add SSH key" button.

Your SSH key is now associated with your GitHub account.

## 3. Clone a Repository Using SSH

Now that you have added your SSH key to your GitHub account, you can use it to clone repositories.

1. Find the SSH URL of the repository you want to clone. You can find this URL on the repository's main page, and it will look like `git@github.com:username/repository.git`.

2. Open your terminal and navigate to the directory where you want to clone the repository.

3. Clone the repository using the SSH URL:

```bash
git clone git@github.com:username/repository.git
```

Replace `username` with the actual GitHub username and `repository` with the repository name.

4. If this is your first time using SSH with GitHub, you might be asked to confirm the authenticity of the host. Type "yes" to proceed.

You can now work with the cloned repository using SSH for secure authentication.

# Ansible Commands and Configuration Simplification with ansible.cfg

Ansible is a powerful automation tool used for configuration management, application deployment, and task automation. To streamline your Ansible experience and make it more efficient, you can use an `ansible.cfg` configuration file to store default settings. In this README, we will cover common Ansible commands and how to simplify them using `ansible.cfg`.

## Table of Contents

1. [Common Ansible Commands](#common-ansible-commands)
2. [Using `ansible.cfg` for Configuration](#using-ansiblecfg-for-configuration)

## 1. Common Ansible Commands

Here are some common Ansible commands used for various tasks:

### 1.1. Running Ad-Hoc Commands

You can run ad-hoc Ansible commands to perform quick tasks on remote hosts.

```bash
ansible <group> -m <module> -a "<module_arguments>"
```

- `<group>`: The name of the group or host to target.
- `<module>`: The Ansible module to execute.
- `<module_arguments>`: Arguments specific to the module being used.

Example:

```bash
ansible web_servers -m shell -a "uptime"
```

### 1.2. Playbooks Execution

Playbooks are YAML files that define tasks and configurations to be applied to target hosts.

```bash
ansible-playbook playbook.yml
```

- `playbook.yml`: The name of the playbook file to execute.

### 1.3. Inventory Management

You can specify the inventory file when running commands or playbooks:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

- `inventory.ini`: The path to the Ansible inventory file.

## 2. Using `ansible.cfg` for Configuration

To simplify Ansible commands and reduce repetition, you can create an `ansible.cfg` file to store default configurations. This file should be placed in the directory where you run your Ansible commands.

Here's an example `ansible.cfg` file:

```ini
[defaults]
inventory = inventory.ini
private_key_file = ~/.ssh/my-ssh-key.pem
```

In this example:

- `[defaults]` defines default configuration settings.
- `inventory` specifies the default inventory file.
- `remote_user` sets the default SSH username.
- `private_key_file` sets the default SSH private key.

With these settings in `ansible.cfg`, you can simplify commands. For example:

```bash
ansible-playbook playbook.yml
```

This command will use the `inventory.ini` file, `myuser` as the remote user, and `~/.ssh/my-ssh-key.pem` as the private key without specifying them in every command.

Creating an `ansible.cfg` file and customizing default configurations can make your Ansible workflow more efficient, as you won't need to repeat the same options in every command.

# Ansible Basic and Advanced Commands

Ansible is a powerful automation tool that simplifies configuration management, application deployment, and task automation. This README provides an overview of basic and advanced Ansible commands to help you get started with managing your infrastructure efficiently.

## Table of Contents

1. [Basic Ansible Commands](#basic-ansible-commands)
2. [Advanced Ansible Commands](#advanced-ansible-commands)

## 1. Basic Ansible Commands

### 1.1. Running Ad-Hoc Commands

Ad-hoc commands are used for quick tasks on remote hosts.

```bash
ansible <group> -m <module> -a "<module_arguments>"
```

- `<group>`: The name of the group or host to target.
- `<module>`: The Ansible module to execute.
- `<module_arguments>`: Arguments specific to the module being used.

Example:

```bash
ansible web_servers -m ping
```

### 1.2. Playbooks Execution

Playbooks are YAML files that define tasks and configurations to be applied to target hosts.

```bash
ansible-playbook playbook.yml
```

- `playbook.yml`: The name of the playbook file to execute.

### 1.3. Inventory Management

You can specify the inventory file when running commands or playbooks:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

- `inventory.ini`: The path to the Ansible inventory file.

## 2. Advanced Ansible Commands

### 2.1. Using Variables

Ansible allows you to use variables in playbooks for dynamic behavior:

```yaml
---
- name: Configure Nginx
  hosts: web_servers
  vars:
    nginx_port: 80
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
    - name: Configure Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
```

In this example, the `nginx_port` variable is defined in the playbook.

### 2.2. Conditionals

You can use conditional statements to control playbook execution based on specific conditions:

```yaml
---
- name: Ensure Nginx is running
  hosts: web_servers
  tasks:
    - name: Start Nginx
      service:
        name: nginx
        state: started
      when: nginx_installed.stat.exists
```

In this example, Ansible checks if Nginx is installed before attempting to start it.

### 2.3. Loops

Loops allow you to repeat tasks for multiple items:

```yaml
---
- name: Install multiple packages
  hosts: web_servers
  tasks:
    - name: Install packages
      apt:
        name: "{{ item }}"
        state: present
      loop:
        - package1
        - package2
        - package3
```

This playbook installs multiple packages in the loop.

### 2.4. Handlers

Handlers are tasks that run in response to a change in the playbook. They are typically used for services that need to be restarted:

```yaml
---
- name: Ensure Nginx is running
  hosts: web_servers
  tasks:
    - name: Start Nginx
      service:
        name: nginx
        state: started
      notify: Restart Nginx
  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

In this example, if Nginx is started, it notifies the handler to restart Nginx.

These are just a few examples of basic and advanced Ansible commands. With Ansible, you can automate complex infrastructure management tasks, and its flexibility makes it a valuable tool for IT automation. For more detailed information, refer to the official Ansible documentation: [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html).