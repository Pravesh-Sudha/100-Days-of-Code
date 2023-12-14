# Day 70 of 100DaysOfCode

Feeling excited to start Day 70 of 100 DaysOfCode, today, I created a AWS Vpc and VPC peering project with help of [ShubhumLonde](https://youtu.be/UVNVPquIkXE?si=J-FYTeliQ9eqSlZV). In this project, I get to know about the basics of AWS Vpc, VPC peering, how to create a VPC, private Subnets and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-70
```

# AWS VPC and Networking Guide

## Table of Contents
1. [Introduction](#introduction)
2. [AWS VPC](#aws-vpc)
    - [What is VPC?](#what-is-vpc)
    - [Key Features](#key-features)
3. [Creating a VPC](#creating-a-vpc)
    - [Step 1: Access AWS Management Console](#step-1-access-aws-management-console)
    - [Step 2: Navigate to VPC Dashboard](#step-2-navigate-to-vpc-dashboard)
    - [Step 3: Create a VPC](#step-3-create-a-vpc)
4. [VPC Peering](#vpc-peering)
    - [What is VPC Peering?](#what-is-vpc-peering)
    - [Creating VPC Peering Connection](#creating-vpc-peering-connection)
    - [Accepting VPC Peering Connection](#accepting-vpc-peering-connection)
5. [Private Subnets](#private-subnets)
    - [Creating Private Subnets](#creating-private-subnets)
    - [Associating Subnets with Route Tables](#associating-subnets-with-route-tables)
6. [Internet Gateway](#internet-gateway)
    - [Creating an Internet Gateway](#creating-an-internet-gateway)
    - [Attaching an Internet Gateway to a VPC](#attaching-an-internet-gateway-to-a-vpc)
7. [Route Tables](#route-tables)
    - [Creating a Route Table](#creating-a-route-table)
    - [Associating a Route Table with a Subnet](#associating-a-route-table-with-a-subnet)
8. [NAT Gateway](#nat-gateway)
    - [Creating a NAT Gateway](#creating-a-nat-gateway)
    - [Associating a Route Table with NAT Gateway](#associating-a-route-table-with-nat-gateway)

### What is VPC?
Amazon Virtual Private Cloud (VPC) is a logically isolated section of the AWS Cloud where you can launch resources in a virtual network. It allows you to define your own network topology, configure IP address ranges, create subnets, and customize route tables.

### Key Features
- **Isolation**: VPC provides network isolation from other VPCs, enhancing security.
- **Subnetting**: Allows subdivision of IP address ranges into subnets for better resource organization.
- **Security Groups and Network ACLs**: Provides fine-grained control over inbound and outbound traffic.
- **Internet Gateway**: Enables communication between instances in your VPC and the internet.

## Creating a VPC
### Step 1: Access AWS Management Console
Log in to the [AWS Management Console](https://aws.amazon.com/console/).

### Step 2: Navigate to VPC Dashboard
Go to the VPC Dashboard by selecting "VPC" from the services menu.

### Step 3: Create a VPC
Click on "Create VPC" and follow the wizard to define your VPC, including its IP address range, subnets, and any additional configurations.

![Alt text](<Screenshot from 2023-12-14 19-27-42.png>)

## VPC Peering
### What is VPC Peering?
VPC Peering allows communication between instances in different VPCs as if they are on the same network.

### Creating VPC Peering Connection
1. In the VPC Dashboard, select "Peering Connections" and click "Create Peering Connection."
2. Specify the VPCs to be peered and configure the peering connection.

### Accepting VPC Peering Connection
1. In the VPC Dashboard, select "Peering Connections."
2. Accept the pending peering connection.

## Private Subnets
### Creating Private Subnets
1. In the VPC Dashboard, select "Subnets" and click "Create Subnet."
2. Define the subnet within the IP address range of the VPC.

### Associating Subnets with Route Tables
1. Create a route table for private subnets.
2. Associate private subnets with the route table to control traffic flow.

## Internet Gateway
### Creating an Internet Gateway
1. In the VPC Dashboard, select "Internet Gateways" and click "Create Internet Gateway."
2. Attach the Internet Gateway to your VPC.

### Attaching an Internet Gateway to a VPC
1. In the VPC Dashboard, select your VPC and go to the "Attachments" tab.
2. Attach the Internet Gateway to the VPC.

## Route Tables
### Creating a Route Table
1. In the VPC Dashboard, select "Route Tables" and click "Create Route Table."
2. Define the route table and add routes for desired traffic.

### Associating a Route Table with a Subnet
1. In the VPC Dashboard, select "Subnets."
2. Edit the subnet's route table association and select the desired route table.

## NAT Gateway
### Creating a NAT Gateway
1. In the VPC Dashboard, select "NAT Gateways" and click "Create NAT Gateway."
2. Associate the NAT Gateway with a public subnet.

### Associating a Route Table with NAT Gateway
1. In the VPC Dashboard, select "Route Tables."
2. Edit the route table associated with private subnets to route traffic through the NAT Gateway.



