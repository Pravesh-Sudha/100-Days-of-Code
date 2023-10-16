# Day 45 of 100DaysofCode

Feeling excited to start Day 45 of 100 DaysOfCode, today, I watched an amazing video on [Ansible Full Course | Ansible Tutorial For Beginners](https://youtu.be/EcnqJbxBcM0?si=rn7VI40PztI1QexO) by <b>SimpliLearn</b>. This Video contains beginner guide to Ansible, installation and setup, Ansible Architecture, Benefits of using ansible, writing your first playbook and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-45
```

# What is Ansible?

In simple terms, Ansible is a tool which can automate the configuration of all your systems, removing the headache of doing everything manually. With Ansible, you can write configuration in form of yaml and deploy in onto thousands of servers which configures them to the desired state. It has three functions:

    - Configuration Management
    - Orchestration
    - Deployment

# Installation and Setup    

Before you begin, make sure you have the following prerequisites:

- A computer with the target operating system installed.
- Administrative privileges (for Windows and some tasks on Ubuntu).
- Internet connection for downloading packages.

## Installation on Ubuntu

1. Open a terminal on your Ubuntu machine.

2. Update the package list to ensure you have the latest information about available packages:

   ```bash
   sudo apt update
   ```

3. Install Ansible using the following command:

   ```bash
   sudo apt install ansible
   ```

4. After the installation is complete, you can verify the installation by running:

   ```bash
   ansible --version
   ```

   This command should display the Ansible version and other information.

## Installation on Windows

1. Ansible can be installed on Windows using Windows Subsystem for Linux (WSL). Make sure you have WSL installed. You can follow the official Microsoft documentation for WSL installation.

2. Open your WSL terminal.

3. Update the package list:

   ```bash
   sudo apt update
   ```

4. Install Ansible:

   ```bash
   sudo apt install ansible
   ```

5. Verify the installation:

   ```bash
   ansible --version
   ```

   This command should display the Ansible version and other information.

## Installation on macOS

1. Install Homebrew if you haven't already. Homebrew is a package manager for macOS.

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Update Homebrew:

   ```bash
   brew update
   ```

3. Install Ansible using Homebrew:

   ```bash
   brew install ansible
   ```

4. Verify the installation:

   ```bash
   ansible --version
   ```

   This command should display the Ansible version and other information.

## Creating an Ansible Playbook

1. Create a directory for your Ansible project, if you haven't already:

   ```shell
   mkdir my-ansible-project
   cd my-ansible-project
   ```

2. Create an Ansible playbook file with a `.yml` extension. You can use any text editor of your choice. For example:

   ```shell
   touch echo_playbook.yml
   ```

3. Open `echo_playbook.yml` in your text editor.

## Step 2: Define Your Ansible Playbook

In this example, we'll create a simple playbook that uses the `echo` module to print a message on a remote server.

Here's the content of `echo_playbook.yml`:

```yaml
---
- name: Simple Echo Playbook
  hosts: your_target_host  # Replace with the hostname or IP address of the remote server
  tasks:
    - name: Print a Message
      command: echo "Hello, Ansible!"
```

- `name`: A user-defined name for the playbook.
- `hosts`: Specify the target host where you want to run the `echo` command. Replace `your_target_host` with the hostname or IP address of the remote server.

## Step 3: Run the Ansible Playbook

1. Open a terminal on your control machine.

2. Navigate to the directory where your playbook is located (`my-ansible-project` in this example).

3. Run the playbook using the `ansible-playbook` command:

   ```shell
   ansible-playbook echo_playbook.yml
   ```

4. Ansible will connect to the target server, execute the `echo` command, and display the output in your terminal.

## Step 4: Verify the Output

After running the playbook, you should see the output of the `echo` command on your remote server displayed in the terminal.

```shell
PLAY [Simple Echo Playbook] ****************************************************

TASK [Print a Message] ********************************************************
changed: [your_target_host]

PLAY RECAP ********************************************************************
your_target_host              : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

The `changed` value indicates that the `echo` command was executed successfully.

## Ansible Architecture

Ansible follows a client-server architecture:

- **Control Node:** The control node is where you run Ansible. It contains the Ansible command-line tools, playbooks, and inventory files. Playbooks are written in YAML and define the tasks to be executed on remote hosts.

- **Managed Nodes:** These are the target systems where Ansible will execute tasks. Managed nodes can be Linux servers, Windows servers, network devices, or any system with SSH access or Ansible's WinRM support for Windows.

Ansible communicates with managed nodes through SSH (Linux) or WinRM (Windows) and does not require any agent software to be installed on them.

# Benefits of Using Ansible

## 1. Infrastructure as Code

With Ansible, you can define your infrastructure as code, allowing you to create, configure, and manage your infrastructure using human-readable and versionable code. This approach enhances collaboration, reproducibility, and documentation.

## 2. Agentless Architecture

Ansible uses an agentless architecture, which means it doesn't require any additional software or agents to be installed on target machines. This simplifies deployment and reduces the overhead associated with maintaining agents.

## 3. Simple and Human-Readable Language

Ansible playbooks are written in YAML, a simple and human-readable language. This makes it easy for both technical and non-technical users to understand and create automation scripts.

## 4. Idempotence

Ansible is idempotent, meaning you can run the same playbook multiple times, and it will ensure that the desired state of the system is achieved. This prevents unintended changes and simplifies system management.

## 5. Broad Platform Support

Ansible offers support for a wide range of operating systems and platforms, including Linux, Windows, macOS, and various cloud providers. It provides a consistent automation solution across diverse environments.

## 6. Automation and Orchestration

Ansible goes beyond simple task automation. It allows you to orchestrate complex tasks, define dependencies between tasks, and automate multi-step processes, making it suitable for a variety of use cases.

## 7. Version Control Integration

Ansible integrates seamlessly with version control systems like Git. This enables you to maintain, version, and collaborate on your automation code, ensuring consistency and traceability.

## 8. Scalability

You can scale Ansible to manage both small and large infrastructures. It supports parallel execution, making it suitable for managing clusters of servers or cloud instances efficiently.

## 9. Security

Ansible provides robust security features, including secure communication with SSH and SSL/TLS, role-based access control, and the ability to encrypt sensitive data. These features help protect your automation infrastructure and data.

## 10. Community and Ecosystem

Ansible has a vibrant and active community that contributes to its growth and development. It offers a wide range of modules and roles, which can be easily shared and reused, saving time and effort when building automation solutions.
