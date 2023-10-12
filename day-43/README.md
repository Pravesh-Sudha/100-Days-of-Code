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

## Documentation

- Provide meaningful names for tasks, roles, and playbooks.
- Use comments to explain complex tasks and conditions.
- Maintain README.md files in your roles and playbooks, documenting their purpose, usage, and variables.
- Document inventory structure and variable definitions.
- Keep an inventory file with clear host definitions and group assignments.

## Version Control

Use a version control system (e.g., Git) to manage your Ansible code. Version control helps track changes, collaborate with team members, and provides a history of your automation code.

