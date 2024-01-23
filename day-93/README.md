# Day 93 of 100DaysOfCode

Feeling excited to start Day 93 of 100 DaysOfCode, today, I dived deep into Aws VPC, and its components by a VPC with internet and NAT gateway, with private and public subnetes with help of [Abhishek Veermalla](https://youtu.be/FZPTL_kNvXc?si=HgIrKNZzecQ7g-xq) in which he explained the whole process.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-93
``` 

## AWS VPC Setup with Auto Scaling, Load Balancer, and Security Groups

### Step 1: Create a VPC

1. Navigate to the [AWS Management Console](https://aws.amazon.com/).
2. Open the VPC Dashboard.
3. Click on "Create VPC."
4. Provide a name for your VPC, set the IPv4 CIDR block, and click "Create."

### Step 2: Create Subnets

1. In the VPC Dashboard, click on "Subnets" in the left-hand navigation pane.
2. Create two public and two private subnets in different availability zones.
3. Associate the public subnets with the VPC's Internet Gateway.

### Step 3: Internet Gateway and Route Tables

1. In the VPC Dashboard, click on "Internet Gateways."
2. Create an Internet Gateway and attach it to your VPC.
3. Create route tables for public and private subnets.
4. Associate the public subnets with the route table that has a route to the Internet Gateway.

### Step 4: NAT Gateway

1. In the VPC Dashboard, click on "Nat Gateways."
2. Create a NAT Gateway in a public subnet.
3. Update the private subnet route tables to include a route to the NAT Gateway.

### Step 5: Security Groups

1. In the EC2 Dashboard, click on "Security Groups."
2. Create security groups for your public and private instances.
3. Define inbound and outbound rules according to your requirements.

### Step 6: Launch Configuration and Auto Scaling Group

1. In the EC2 Dashboard, click on "Launch Configurations."
2. Create a Launch Configuration, specifying your Amazon Machine Image (AMI), instance type, and user data script if needed.
3. In the Auto Scaling Dashboard, click on "Auto Scaling Groups."
4. Create an Auto Scaling Group, referencing the Launch Configuration, and set up desired capacity and scaling policies.

### Step 7: Load Balancer

1. In the EC2 Dashboard, click on "Load Balancers."
2. Create a Load Balancer, choosing appropriate settings and associating it with the instances in your Auto Scaling Group.
3. Configure listeners and health checks.

### Step 8: Testing

1. Launch instances within your Auto Scaling Group.
2. Verify that instances are distributed across availability zones.
3. Test the Load Balancer to ensure traffic is distributed evenly.

### Step 9: Cleanup (Optional)

If you want to clean up resources:

1. Terminate instances launched by the Auto Scaling Group.
2. Delete the Auto Scaling Group, Launch Configuration, and Load Balancer.
3. Disassociate and delete the Internet Gateway, NAT Gateway, and Route Tables.
4. Delete the VPC.
