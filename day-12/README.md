# Day 12 of 100DaysofCode

Feeling excited to start Day 12 of 100 DaysOfCode, today, I learnt about the basic shell scripting commands in a great Video by [Train With Shubhum](https://youtube.com/playlist?list=PLlfy9GnSVerQr-Se9JRE_tZJk3OUoHCkh&si=RpQBLv9geaalTCek). Shell scripting is the process of automating tasks and interacting with the operating system using a series of commands written in a shell scripting language. Shell scripts can help streamline repetitive tasks, perform system administration, and create custom utilities.

## Prerequisites

Before using these commands, ensure you have one of the following environments set up:

- **Ubuntu Desktop:** Install Ubuntu on your local machine by following the official installation guide at [ubuntu.com](https://ubuntu.com/download/desktop).

- **Windows Subsystem for Linux (WSL):** If you're using Windows, set up WSL by following the instructions at [Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install).

- **Amazon EC2 Instance:** If you prefer a cloud environment, create an Amazon EC2 instance running a Linux distribution. Follow the steps outlined in the [AWS documentation](https://aws.amazon.com/getting-started/hands-on/run-your-app-using-amazon-ec2/).

# Basic Shell Commands

This repository contains a collection of basic Linux commands that are essential for navigating and managing a Linux operating system. Whether you're a beginner looking to get started with Linux or need a quick reference, this README provides a handy guide to fundamental commands.

## Introduction

Shell scripting refers to the practice of creating and executing scripts written in a shell language, which is a command-line interface provided by an operating system. The shell is a text-based interface that allows users to interact with an operating system's services and functionalities using text-based commands. Shell scripting involves writing a series of these commands in a script file, which can be executed to automate tasks, perform system administration, manipulate files and data, and more.

## To create and run this script:

- Open a text editor (such as nano, vim, or any code editor).
- Copy and paste the above script into the editor.
- Save the file with a `.sh` extension (e.g., `greeting.sh`).
- Make the script executable by running: `chmod +x greeting.sh`
- Run the script: `./greeting.sh`

## Example of a file

``` bash
#!/bin/bash
A simple shell script to greet the user

echo "Hello! Please enter your name:"
read name

echo "Hello, $name! Nice to meet you."
```

## Commands

The `echo` command prints text to the terminal.

```bash
echo "Hello, world!"
```

The `ls` command lists directory contents.

```bash
ls
ls -l   # Detailed list
ls -a   # Show hidden files
```

The `grep` command searches for text patterns within files.

```bash
grep "pattern" file.txt
```

The `chmod` command changes file permissions.

```bash
chmod +x script.sh   # Add execute permission
chmod 644 file.txt  # Change permissions numerically
```

The `sleep` command allows to sleep the program for some time.

```bash
sleep 2 # This will sleep the program for 2 seconds.
```

The `wget` command downloads files from the internet.

```bash
wget https://example.com/file.txt
```

Bash allows you to work with variables to store and manipulate data:

```bash
name="John"
echo "Hello, $name!"
```

Conditional statements help make decisions in scripts:

```bash
if [ "$num" -gt 10 ]; then
    echo "Greater than 10"
else
    echo "Less than or equal to 10"
fi
```

Bash can read and manipulate files:

```bash
file="example.txt"

if [ -e "$file" ]; then
    echo "$file exists."
else
    echo "$file does not exist."
fi
```

## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-12
```

## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
