# Day 69 of 100DaysOfCode

Feeling excited to start Day 69 of 100 DaysOfCode, today, I watched AWS Relational Database Service RDS Masterclass | AWS RDS Full Course | RDS Zero to Hero | AWS Demo by [A Monk in Cloud](https://youtu.be/rM_c7K0-tC0?si=X-M9CG5DEIQCJos4). In this video, I get to know about the basics of AWS RDS like overviewe of database, database on EC2, Overview of RDS and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-69
```
# AWS RDS (Relational Database Service) 

Welcome to the README for AWS RDS, a fully-managed relational database service provided by Amazon Web Services (AWS). This document provides an overview of AWS RDS, covers various database types supported, outlines the deployment of databases on EC2 instances, guides you through migrating traditional databases from EC2 to RDS, and explains automatic backup, snapshots, and database restoration processes.

## Table of Contents

1. [What is AWS RDS?](#what-is-aws-rds)
2. [Database Types](#database-types)
3. [Database on EC2 Instances](#database-on-ec2-instances)
4. [Migrating Traditional Databases to RDS](#migrating-traditional-databases-to-rds)
5. [Automatic Backup](#automatic-backup)
6. [Snapshots](#snapshots)
7. [Restoring a Database](#restoring-a-database)


## What is AWS RDS?

AWS RDS is a fully-managed relational database service that makes it easy to set up, operate, and scale a relational database in the cloud. It supports multiple database engines, takes care of routine database tasks, and provides high availability and security.

## Database Types

AWS RDS supports various database engines, including:

- MySQL
- PostgreSQL
- MariaDB
- Oracle
- Microsoft SQL Server
- Amazon Aurora (compatible with MySQL and PostgreSQL)

Choose the database engine that best suits your application requirements.

## Database on EC2 Instances

In some cases, you may choose to deploy a database on EC2 instances for more control and customization. However, managing a database on EC2 requires more operational overhead compared to RDS.

## Migrating Traditional Databases to RDS

Migrating a traditional database from EC2 to RDS involves careful planning and execution. Follow these general steps:

1. **Evaluate Compatibility:** Ensure your database is compatible with the desired RDS database engine.
2. **Backup Data:** Take a backup of your existing database on EC2.
3. **Create RDS Instance:** Set up an RDS instance with the chosen database engine.
4. **Restore Data:** Restore the backup to the new RDS instance.
5. **Update Application Connections:** Update your application to point to the new RDS endpoint.

## Automatic Backup

AWS RDS provides automated backups of your database. Key features include:

- **Retention Period:** Define how long automated backups should be retained.
- **Daily Snapshot:** A snapshot is taken once a day during the maintenance window.
- **Point-in-Time Recovery:** Restore your database to any second during your retention period.

## Snapshots

You can manually create snapshots of your RDS instance at any time. Snapshots are user-initiated and are retained until you choose to delete them.

## Restoring a Database

Restoring a database can be done from both automated backups and manual snapshots. Follow the AWS documentation for detailed steps based on your specific use case.

## Create an RDS Instance

1. Log in to the [AWS Management Console](https://console.aws.amazon.com/).

2. Navigate to the **RDS Dashboard**.

3. Click on **Create Database**.

4. Choose the **Standard Create** option.

## Configure RDS Settings

1. **Engine Options:**
   - Select the desired database engine (e.g., MySQL, PostgreSQL, etc.).
   - Choose the appropriate version.

2. **Templates:**
   - Choose the use case template that best fits your application needs.

3. **Settings:**
   - Specify the DB instance identifier.
   - Set the master username and password.

## Configure Advanced Settings

1. **Network & Security:**
   - Choose the VPC and subnet group for the RDS instance.
   - Configure the publicly accessible option.

2. **Database Options:**
   - Set the database name.
   - Define the initial database size and storage auto-scaling.

3. **Backup:**
   - Configure automated backups and retention periods.

4. **Monitoring:**
   - Enable enhanced monitoring if required.

5. **Maintenance:**
   - Set the preferred backup window and maintenance window.

## Database Security

1. **VPC Security Group:**
   - Configure the security group to control inbound and outbound traffic.

2. **Database Authentication:**
   - Choose the authentication method (password authentication is recommended).

3. **IAM Authentication (Optional):**
   - Enable IAM database authentication for enhanced security.

## Review and Launch

1. Review the configured settings on the **Review** page.

2. Click on **Create Database** to launch the RDS instance.

3. Monitor the status on the **RDS Dashboard** until the instance shows as "Available."

## Monitor and Manage

1. Explore the **Monitoring** tab to view performance metrics.

2. Configure **alarms** for critical metrics using Amazon CloudWatch.

3. Set up automatic backups and snapshots for data protection.

## Connect to the RDS Database

1. Obtain the **Endpoint** from the RDS Dashboard.

2. Use a database client (e.g., MySQL Workbench, pgAdmin) to connect to the RDS instance using the provided credentials.

3. Perform necessary database operations and queries.

