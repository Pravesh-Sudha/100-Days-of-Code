# Day 1 of 100DaysofCode

Feeling excited to start Day 1 of 100 DaysOfCode, today, I learnt about the Evolution of Cloud + Infrastructure as code (Part 1) and Terraform overview and setup locally.

<h3>Pre Cloud V/S Cloud Era</h3>

* Pre-Cloud era belongs to 1990s - 2000s in which if you come up with an idea, you need to write it down in software and buy a whole different server and set up a data center for hosting the software on web which was a very challenging task.
* Cloud era belongs to 2000s - Present in which cloud providers like Amazon Web Services(AWS) , Google Cloud Provider (GCP), Microsoft Azure and many more provides hosting services on web in a cost efficent way. You don't have stress on the challenging part of deploying on physical server.

<h4>What has Changed</h4>

* Infrastructure provisioned via APIs
* Servers can be created and Destroyed in seconds
* Long-lived + mutable -> short-lived + immutable

<h4>Three Approaches of provisioning Cloud Resources</h4>

* <b>GUI</b>: It is the Graphical User Interface. Different cloud providers have different types of GUI like Aws management console have different features compared to GCP console.
* <b>API/CLI</b>: It is the Command Line Interface. All cloud providers give you access to their provider through Cli. Forexample, Aws command in Cli can be used to connect an AWS cloud provider.  
* <b>IaC</b>: Infrastructure as Code is the best way to connect to your cloud provider and deploy your application. IaC tools like Terraform can help you have multi-cloud access to connect with your cluster.

<h2>Infrastructure as Code</h2>

According to [Red Hat](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac#:~:text=choose%20Red%20Hat%3F-,Overview,to%20edit%20and%20distribute%20configurations.) docs, Infrastructure as Code (IaC) is the managing and provisioning of infrastructure through code instead of through manual processes. With IaC, configuration files are created that contain your infrastructure specifications, which makes it easier to edit and distribute configurations.

<h3>Categories of IaC Tools</h3>

* Ad Hoc scripts
* Configuration Management Tools like <b>Ansible</b>
* Server Templating Tools
* Orchestration Tools like Kubernetes
* Provisioning Tools which can be declartive or imperative

<h3>What is Terraform</h3>

* Terraform is a tool for building, changing, and versioning infrastructure safely and efficently.
* Enables application software best practices to infrastructure
* Compatible with many clouds and services

<h3>Terraform Architecture</h3>

* It has a terraform core which Communicate with Terraform state and Terraform Config and take actions on the state file to change the congiuration according to Terraform Config file.
* Terraform state file contains references to all the architecture that we have configured.