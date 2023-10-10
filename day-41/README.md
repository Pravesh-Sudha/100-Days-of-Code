# Day 41 of 100DaysofCode

Feeling excited to start Day 41 of 100 DaysOfCode, today, I watched an amazing video on [Getting Started With Ansible](https://youtube.com/playlist?list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&si=UYA7FzyLue5zXTcL) by <b>Learn Linux TV</b>. This Video contains beginner guide to Ansible, its playbooks  and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-41
```

## Table of Contents
- [What is Ansible?](#what-is-ansible)
- [Ansible Architecture](#ansible-architecture)
- [Sample Playbook](#sample-playbook)

---

## What is Ansible?

Ansible is an open-source automation tool that simplifies the management of IT infrastructure and application deployment by allowing you to automate tasks, configure systems, and orchestrate complex workflows. It is agentless, meaning it does not require any software to be installed on target systems. Ansible uses SSH for remote communication with target servers, making it highly secure and efficient.

Ansible is particularly useful for:

- **Configuration Management:** Managing and maintaining server configurations in a consistent state across multiple machines.

- **Application Deployment:** Automating the deployment of applications and services, ensuring they are consistently configured.

- **Provisioning:** Creating and managing virtual machines or cloud resources as needed.

- **Orchestration:** Defining and executing complex workflows and tasks involving multiple servers and services.

- **Security Automation:** Enforcing security policies and configurations across your infrastructure.

- **Continuous Integration/Continuous Deployment (CI/CD):** Integrating Ansible into your CI/CD pipelines to automate deployment and testing processes.

Ansible uses a declarative language to define the desired state of systems, which makes it easy to use and understand.

## Ansible Architecture

Ansible follows a client-server architecture:

- **Control Node:** The control node is where you run Ansible. It contains the Ansible command-line tools, playbooks, and inventory files. Playbooks are written in YAML and define the tasks to be executed on remote hosts.

- **Managed Nodes:** These are the target systems where Ansible will execute tasks. Managed nodes can be Linux servers, Windows servers, network devices, or any system with SSH access or Ansible's WinRM support for Windows.

Ansible communicates with managed nodes through SSH (Linux) or WinRM (Windows) and does not require any agent software to be installed on them.

## Sample Playbook

Below is a sample Ansible playbook that installs and configures a web server (Nginx) on a group of Linux servers. This playbook is written in YAML and demonstrates the simplicity of Ansible playbooks.

```yaml
---
- name: Install and Configure Nginx
  hosts: web_servers
  become: yes  # Use privilege escalation (sudo) to execute tasks as root

  tasks:
    - name: Update package cache
      apt:
        update_cache: yes
      when: ansible_os_family == 'Debian'

    - name: Install Nginx
      apt:
        name: nginx
        state: present
      when: ansible_os_family == 'Debian'

    - name: Start Nginx and enable it on boot
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Configure Nginx default site
      template:
        src: default.j2
        dest: /etc/nginx/sites-available/default
      notify:
        - Reload Nginx

  handlers:
    - name: Reload Nginx
      service:
        name: nginx
        state: reloaded
```

In this playbook:

- We specify the name of the playbook and the target hosts in the `hosts` field. `web_servers` is a group of servers defined in the Ansible inventory.

- We use privilege escalation (`become: yes`) to execute tasks as the root user.

- The playbook includes tasks to update the package cache, install Nginx, start the Nginx service, and configure the default Nginx site.

- A handler is defined to reload Nginx whenever the configuration changes.

This playbook demonstrates how Ansible can be used to automate the installation and configuration of software on remote servers.

For more information and advanced use cases, please refer to the [Ansible documentation](https://docs.ansible.com/ansible/latest/index.html).