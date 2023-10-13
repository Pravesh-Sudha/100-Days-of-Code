# Day 43 of 100DaysofCode

Feeling excited to start Day 43 of 100 DaysOfCode, today, I watched an amazing video on [Getting Started With Ansible](https://youtube.com/playlist?list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&si=UYA7FzyLue5zXTcL) by <b>Learn Linux TV</b>. This Video contains beginner guide to Ansible, Improving your Playbook, Targetting Specific Nodes, Tags and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-43
```

## When Statements

The `when` keyword is used within tasks to define conditions for their execution. It accepts an expression, which is evaluated. If the expression returns `True`, the task is executed; otherwise, it is skipped.

The basic syntax of a `when` statement in Ansible is as follows:
```yaml
tasks:
  - name: Task Name
    module: some_module
    when: some_condition
```

In the `when` field, `some_condition` is an expression that should evaluate to either `True` or `False`.

## Examples

### Conditional Task Execution

In this example, we have a simple Ansible playbook that installs a package, but only if it's running on an Ubuntu system.

```yaml
---
- name: Install Apache on Ubuntu
  hosts: web_servers
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
      when: "'Ubuntu' in ansible_facts['distribution']"
```

In this playbook, the `when` statement checks if the distribution name in `ansible_facts` contains the word "Ubuntu." If it does, the task will be executed; otherwise, it will be skipped.

### Complex Conditions

You can also create more complex conditions by combining multiple expressions using logical operators (AND, OR) and grouping them using parentheses.

```yaml
---
- name: Conditional Tasks
  hosts: web_servers
  tasks:
    - name: Task 1
      debug:
        msg: "This task always runs"
    
    - name: Task 2
      debug:
        msg: "This task runs on CentOS or RedHat"
      when: "'CentOS' in ansible_facts['distribution'] or 'RedHat' in ansible_facts['distribution']"

    - name: Task 3
      debug:
        msg: "This task runs on Ubuntu and only in production"
      when: "'Ubuntu' in ansible_facts['distribution'] and inventory_hostname in groups['production']"
```

# Ansible Playbook Best Practices

Ansible is a versatile automation and configuration management tool, but to make the most of it, it's essential to follow best practices. These practices help maintain organized, efficient, and reliable Ansible playbooks.

## Directory Structure

A well-structured directory layout is crucial for managing your Ansible project. A typical structure might include:

- `group_vars` and `host_vars` for variable files.
- `roles` for organizing and reusing role definitions.
- `playbooks` for playbook files.
- `inventory` for defining your infrastructure.
- `files` and `templates` for asset files.
- `vars` for defining variables.
- `library` for custom modules.

## Playbook Organization

Each playbook should have a clear, single purpose. Keep your playbooks focused on specific tasks or objectives. This approach makes it easier to manage, understand, and reuse playbooks.

## Modularization

Use roles to modularize your playbooks. Roles group related tasks and can be reused across different playbooks. This promotes code reusability and simplifies maintenance.

## Variable Management

- Use `group_vars` and `host_vars` to manage variables specific to groups and hosts.
- Use `vars` files within roles to define role-specific variables.
- Use encrypted files for sensitive data.
- Avoid hardcoding values in playbooks; use variables instead.

## Error Handling

- Use the `failed_when` attribute to define when a task is considered a failure.
- Include exception handling for tasks that might fail.
- Use the `ignore_errors` option judiciously, and document why you're ignoring errors.

## Security

- Restrict access to sensitive files and variables.
- Use Ansible Vault to encrypt sensitive data.
- Limit the use of `become` and `become_user` to only when necessary.
- Maintain proper SSH key management and SSH configurations.

## Idempotence

Write your tasks to be idempotent. Tasks should be safe to run multiple times without causing unintended side effects. This ensures predictable and reliable automation.

## Testing

- Test your playbooks in a safe environment before applying them to production systems.
- Use Ansible's dry-run (`--check`) and verbose (`-vvv`) modes to understand the potential impact of your playbooks.
- Consider using a test framework like Molecule to automate testing.

## Version Control

Use a version control system (e.g., Git) to manage your Ansible code. Version control helps track changes, collaborate with team members, and provides a history of your automation code.

# Targeting Specific Nodes in Ansible Playbook

Ansible provides an ability to target specific nodes in an its playbook. Ansible is a powerful automation tool for configuration management, application deployment, and task orchestration. To perform tasks on specific nodes, you need to define the target hosts effectively.

## Targeting Syntax

Ansible provides various methods for specifying target hosts in your playbook:

- **All hosts:** You can target all hosts defined in your inventory by using `all`. For example:

    ```yaml
    - hosts: all
      tasks:
        - name: This task runs on all hosts
          # Task details
    ```

- **Single host:** To target a single host, use the hostname directly:

    ```yaml
    - hosts: webserver1
      tasks:
        - name: This task runs on webserver1
          # Task details
    ```

- **Multiple hosts:** You can target multiple hosts by using patterns, such as groups or regular expressions:

    ```yaml
    - hosts: webservers
      tasks:
        - name: This task runs on all hosts in the 'webservers' group
          # Task details
    ```

    ```yaml
    - hosts: dev*
      tasks:
        - name: This task runs on all hosts matching the pattern 'dev*'
          # Task details
    ```

- **Excluding hosts:** You can exclude specific hosts using the `!` operator:

    ```yaml
    - hosts: all:!webserver1
      tasks:
        - name: This task runs on all hosts except 'webserver1'
          # Task details
    ```

## Examples

### Basic Playbook Targeting

Here is a simple example of an Ansible playbook that targets specific hosts:

```yaml
- hosts: webservers
  tasks:
    - name: Ensure Nginx is installed
      apt:
        name: nginx
        state: present
      become: yes
```

In this example, the playbook will run the task on all hosts in the 'webservers' group.

### Advanced Targeting with Regular Expressions

You can use regular expressions to target hosts that match a specific pattern. For example:

```yaml
- hosts: ~^web\d$
  tasks:
    - name: This task runs on hosts with names like 'web1', 'web2', etc.
      # Task details
```

This playbook will target all hosts whose names match the regular expression `^web\d$`, which includes hosts like 'web1', 'web2', and so on.

## Targeting Strategies

When targeting specific nodes in Ansible, consider these strategies:

1. **Use Groups:** Organize your hosts into groups in your inventory file. This simplifies playbook targeting by referring to the group name.

2. **Use Regular Expressions:** Regular expressions can be powerful for targeting hosts with similar names or patterns.

3. **Limit the Scope:** Use the `--limit` option when running the playbook to override the playbook's host selection. This can be helpful for one-off or testing scenarios.


