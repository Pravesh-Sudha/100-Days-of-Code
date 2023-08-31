# Day 13 of 100DaysofCode

Feeling excited to start Day 13 of 100 DaysOfCode, today, I learnt about the advanced shell scripting commands in a great Video by [Train With Shubhum](https://youtube.com/playlist?list=PLlfy9GnSVerQr-Se9JRE_tZJk3OUoHCkh&si=RpQBLv9geaalTCek). This video includes advanced shell commands like how to add a user, for loops, practices of a devops engineer and how to automate backups with Bash scripts.

## Prerequisites

Before using these commands, ensure you have one of the following environments set up:

- **Ubuntu Desktop:** Install Ubuntu on your local machine by following the official installation guide at [ubuntu.com](https://ubuntu.com/download/desktop).

- **Windows Subsystem for Linux (WSL):** If you're using Windows, set up WSL by following the instructions at [Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install).

- **Amazon EC2 Instance:** If you prefer a cloud environment, create an Amazon EC2 instance running a Linux distribution. Follow the steps outlined in the [AWS documentation](https://aws.amazon.com/getting-started/hands-on/run-your-app-using-amazon-ec2/).

# Advanced Shell Commands

This repository contains a collection of advanced Linux commands that are essential for navigating and managing a Linux operating system. Whether you're a beginner looking to get started with Linux or need a quick reference, this README provides a handy guide to fundamental commands.

## Introduction

Shell scripting refers to the practice of creating and executing scripts written in a shell language, which is a command-line interface provided by an operating system. The shell is a text-based interface that allows users to interact with an operating system's services and functionalities using text-based commands. Shell scripting involves writing a series of these commands in a script file, which can be executed to automate tasks, perform system administration, manipulate files and data, and more.

## Example of a file

``` bash
#!/bin/bash
A simple shell script to greet the user

echo "Hello! Please enter your name:"
read name

echo "Hello, $name! Nice to meet you."
```

## Commands

Loops allow you to repeat commands:

```bash
for i in {1..5}; do
    echo "Number: $i"
done
```

If-elif statment in Shell:

```bash
#!/bin/bash

read -p "Enter a number: " num

if [ $num -gt 0 ]; then
    echo "Number is positive"
elif [ $num -lt 0 ]; then
    echo "Number is negative"
else
    echo "Number is zero"
fi
```

Adding a User in Shell:

```bash
#!/bin/bash

read -p "Enter the username: " username

# Check if the user already exists
if id "$username" &>/dev/null; then
    echo "User '$username' already exists."
else
    # Prompt for user details
    read -p "Enter the full name: " fullname
    read -p "Enter the password: " password

    # Create the user with the provided details
    useradd -c "$fullname" -m "$username"
    echo "$username:$password" | chpasswd

    echo "User '$username' created successfully."
fi
```

Functions allow you to group commands:

```bash
greet() {
    echo "Hello from function!"
}

greet
```

## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-13
```

## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
