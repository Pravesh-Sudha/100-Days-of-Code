# Day 44 of 100DaysofCode

Feeling excited to start Day 44 of 100 DaysOfCode, today, I watched an amazing video on [Getting Started With Ansible](https://youtube.com/playlist?list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&si=UYA7FzyLue5zXTcL) by <b>Learn Linux TV</b>. This Video contains beginner guide to Ansible, Tags, Managing Files and Services and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-44
```

## Introduction to Tags

Tags in Ansible are labels or identifiers that you can associate with tasks within your playbook. These tags help you organize and selectively run tasks when executing the playbook, giving you greater control over the automation process. Tags are particularly useful in large playbooks or when you want to focus on specific parts of your automation.

## Adding Tags to Playbooks

To add tags to tasks in your playbook, you simply include a `tags` field for each task. Here's an example of how you can add tags to your playbook:

```yaml
- hosts: all
  become: true
  tasks:
    - name: Install Apache2
      apt:
        name: apache2
        state: present
      tags:
        - apache

    - name: Install PHP
      apt:
        name: php
        state: present
      tags:
        - php
```

In this example, two tasks have been tagged with `apache` and `php` respectively. These tags allow you to execute tasks selectively when running the playbook.

## Running Tasks with Tags

To run tasks with specific tags, you can use the `--tags` option when executing the playbook. For instance, if you want to run only the tasks with the `apache` tag, you can use the following command:

```bash
ansible-playbook playbook.yml --tags apache
```

You can also exclude tasks with specific tags using the `--skip-tags` option. For example, to skip tasks tagged with `php`, you can use the following command:

```bash
ansible-playbook playbook.yml --skip-tags php
```

## Examples

Here's an example of how tags can be useful in a playbook:

```yaml
- hosts: all
  become: true
  tasks:
    - name: Install Apache2
      apt:
        name: apache2
        state: present
      tags:
        - web

    - name: Install PHP
      apt:
        name: php
        state: present
      tags:
        - web
        - php

    - name: Configure Database
      template:
        src: db_config.j2
        dest: /etc/db_config.conf
      tags:
        - db
```

With the tags applied, you can execute the playbook with different scenarios:

- To install web-related components: `ansible-playbook playbook.yml --tags web`
- To install only PHP: `ansible-playbook playbook.yml --tags php`
- To configure the database: `ansible-playbook playbook.yml --tags db`

This flexibility allows you to customize your automation based on your specific requirements.

## Best Practices

- Use meaningful tags to make your playbook more readable and maintainable.
- Avoid excessive tagging; use tags sparingly and only when necessary to maintain simplicity.
- Document your tags in your playbook or README to make it easier for other team members to understand and use them.

With tags, you can fine-tune the execution of your Ansible playbooks, making them adaptable to different situations and improving overall manageability.

# Managing Files and Services in Ansible Playbook

Ansible enables you to automate the management of files and services on remote hosts, making it a valuable tool for configuration management, deployment, and maintenance.

## Managing Files

### Copying Files

Use the `copy` module to copy files from your local machine to remote hosts:

```yaml
- name: Copy configuration file
  copy:
    src: /path/to/local/file.conf
    dest: /path/on/remote/file.conf
```

### Template Files

Use the `template` module to copy template files and apply variable substitutions:

```yaml
- name: Copy and template configuration file
  template:
    src: /path/to/template.conf.j2
    dest: /path/on/remote/file.conf
```

### Deleting Files

Use the `file` module to delete files on remote hosts:

```yaml
- name: Delete a file
  file:
    path: /path/on/remote/file.conf
    state: absent
```

## Managing Services

### Starting and Stopping Services

Use the `service` module to start and stop services on remote hosts:

```yaml
- name: Start a service
  service:
    name: servicename
    state: started

- name: Stop a service
  service:
    name: servicename
    state: stopped
```

### Enabling and Disabling Services

Use the `service` module to enable or disable services at boot:

```yaml
- name: Enable a service at boot
  service:
    name: servicename
    enabled: yes

- name: Disable a service at boot
  service:
    name: servicename
    enabled: no
```

## Examples

Here are some practical examples to manage files and services in Ansible playbooks:

### Copying a Configuration File

```yaml
- name: Copy configuration file
  copy:
    src: /local/path/app.conf
    dest: /remote/path/app.conf
```

### Managing a Service

```yaml
- name: Start and enable the Nginx service
  service:
    name: nginx
    state: started
    enabled: yes
```

### Deleting a Temporary File

```yaml
- name: Delete temporary file
  file:
    path: /tmp/tempfile.txt
    state: absent
```

## Best Practices

1. **Use Descriptive Names**: Give your tasks meaningful names to make the playbook more understandable.

2. **Use Variables**: Utilize Ansible variables to make your playbooks more dynamic and reusable.

3. **Document Playbooks**: Include comments or documentation within your playbooks to explain their purpose and usage.

4. **Test Playbooks**: Test playbooks in a safe environment or in "dry-run" mode before running them in production.

5. **Backup Important Files**: If you're making changes to critical files, consider backing up those files before making any modifications.

6. **Use Tags**: As explained in the previous README, use tags to selectively run tasks in your playbook.

By effectively managing files and services with Ansible, you can ensure consistency, reliability, and automation in your server and infrastructure management tasks.

# Creating a User in Ansible Playbook

Managing users on multiple servers can be a repetitive and error-prone task. Ansible allows you to automate user creation and configuration, making it easier to maintain a consistent user environment across your infrastructure.

## Creating a User

To create a user in Ansible, you can use the `user` module. Here's how you can do it:

```yaml
- name: Create a User
  hosts: target-hosts
  become: yes  # Use "yes" for privilege escalation

  tasks:
    - name: Create a new user
      user:
        name: newuser
        comment: New User
        groups: users
        shell: /bin/bash
        password: "{{ 'mypassword' | password_hash('sha512') }}"
        state: present
```

In this example:
- `name` specifies the name of the user to be created.
- `comment` is an optional comment describing the user.
- `groups` is an optional list of groups to which the user should belong.
- `shell` specifies the user's default shell.
- `password` sets the user's password securely using the `password_hash` filter.
- `state` is set to "present" to ensure the user is created.

## Examples

### Create a User with Specific Attributes

```yaml
- name: Create a User
  hosts: target-hosts
  become: yes

  tasks:
    - name: Create an admin user
      user:
        name: admin
        comment: Admin User
        groups:
          - admins
        shell: /bin/bash
        password: "{{ 'adminpassword' | password_hash('sha512') }}"
        state: present
```

### Delete a User

You can also delete a user by changing the `state` attribute to "absent":

```yaml
- name: Delete a User
  hosts: target-hosts
  become: yes

  tasks:
    - name: Remove a user
      user:
        name: user_to_delete
        state: absent
```

## Best Practices

- **Security**: Always manage passwords securely, and consider using Ansible's built-in password hashing functions.
- **Documentation**: Keep your playbooks well-documented, especially if you're creating or deleting user accounts.

By automating user creation and management with Ansible, you can ensure consistency and security in your server and infrastructure administration.