# Day 79 of 100DaysOfCode

Feeling excited to start Day 79 of 100 DaysOfCode, today, I dived deep into Ansible and its Components, I feel like revising ansible is important, So I revised its basics with guidance of [Shubhum Londe](https://youtu.be/SGB7EdiP39E?si=aAqkB3szKPGDgCHP).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-79
```

# Ansible 

Ansible is an open-source automation tool that simplifies configuration management, application deployment, and task automation. It allows DevOps engineers to define infrastructure as code (IaC) and automate repetitive tasks, making it an essential tool for managing infrastructure and ensuring consistency across environments.

## Key Components of Ansible

### 1. **Inventory:**
   - The inventory file defines the hosts (servers) on which Ansible will execute tasks. It can be a simple text file or a dynamic inventory script, listing hostnames or IP addresses. Inventory is a crucial aspect of Ansible as it dictates the target environment for your automation tasks.

   Example of an inventory file (`inventory.ini`):
   ```ini
   [web_servers]
   server1 
   ansible_host=192.168.1.101 
   ansible_user=myuser
   ansible_ssh_private_key_file=/path/to/private_key.pem

   [db_servers]
   server2
   ansible_host=192.168.1.102 
   ansible_user=myuser 
   ansible_ssh_private_key_file=/path/to/private_key.pem
   ```

### 2. **Playbooks:**
   - Playbooks are written in YAML and define a set of tasks to be executed on the hosts defined in the inventory. Playbooks are the primary building blocks of Ansible automation. They can include roles, variables, and handlers to organize and reuse automation logic.

   Example playbook (`deploy_app.yml`):
   ```yaml
   ---
   - name: Deploy Web Application
     hosts: web_servers
     tasks:
       - name: Copy application files
         copy:
           src: /path/to/app
           dest: /var/www/html

       - name: Restart web server
         service:
           name: apache2
           state: restarted
   ```

### 3. **Roles:**
   - Roles provide a way to organize and reuse tasks, handlers, and variables. They encapsulate functionality in a structured directory format, making it easier to share and maintain automation logic across projects.

   Example role structure:
   ```
   roles/
   └── web_server
       ├── tasks
       │   └── main.yml
       ├── handlers
       │   └── main.yml
       ├── templates
       ├── vars
       └── defaults
   ```

### 4. **Modules:**
   - Ansible modules are pre-built units of work that perform specific tasks. Modules can manage system resources, install packages, configure services, and more. Ansible ships with a wide range of modules, and custom modules can also be developed.

   Example module in a task:
   ```yaml
   - name: Install Nginx
     apt:
       name: nginx
       state: present
     become: true
   ```

## Ansible Commands

### 1. **Running a Playbook:**
   - Use the `ansible-playbook` command to execute a playbook.
   ```bash
   ansible-playbook -i inventory.ini deploy_app.yml
   ```

### 2. **Ad-Hoc Commands:**
   - Execute ad-hoc commands for quick tasks using `ansible` command.
   ```bash
   ansible -i inventory.ini web_servers -m shell -a "uptime"
   ```

### 3. **Inventory Management:**
   - View the list of hosts defined in the inventory.
   ```bash
   ansible-inventory -i inventory.ini --list
   ```

### 4. **Check Mode:**
   - Run a playbook in check mode to see what changes would be made without actually applying them.
   ```bash
   ansible-playbook -i inventory.ini deploy_app.yml --check
   ```

### 5. **Vault:**
   - Encrypt sensitive data using Ansible Vault.
   ```bash
   ansible-vault encrypt secret.yml
   ```

### 6. **Dynamic Inventory:**
   - Utilize dynamic inventory scripts to dynamically generate the inventory based on external systems.
   ```bash
   ansible -i /path/to/dynamic_inventory_script.py web_servers -m ping
   ```

## Conclusion

Ansible simplifies infrastructure automation by providing a flexible and powerful toolset. This guide provides a brief overview of Ansible's components and common commands. Explore the official documentation for in-depth details and advanced features: [Ansible Documentation](https://docs.ansible.com/).