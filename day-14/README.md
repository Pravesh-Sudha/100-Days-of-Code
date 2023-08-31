# Day 13 of 100DaysofCode

Feeling excited to start Day 14 of 100 DaysOfCode, today, I learnt about the advanced shell scripting commands in a great Video by [Train With Shubhum](https://youtube.com/playlist?list=PLlfy9GnSVerQr-Se9JRE_tZJk3OUoHCkh&si=RpQBLv9geaalTCek). This video includes advanced shell commands like Memory Commands, AWK Commands, While Loops, cut commands, Disk Check Script and vim editor.

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

### free

Display information about the system's memory usage

```bash
free -h
```

### top

Interactively monitor system processes and memory usage.

```bash
top
```

### disk free

Display information about the system's disk size and usage

```bash
df -H
```

### AWK

Awk is a versatile text processing tool. 

```bash
df -H | awk '{print $1, $3}' filename
```
Use `awk` to print specific columns from a file (e.g., column 1 and 3) from the `df -H` command.

### Vim

Using the Vim Editor
Vim is a powerful text editor for the command line.

Opening a File
Open a file using Vim.

```bash 
vim filename
```
Command Mode Basics:
- i: Enter insert mode
- Esc: Exit insert mode
- :w: Save changes
- :q: Quit Vim
- :wq: Save and quit
- :x: Same as :wq

### While Loops

A basic loop structure in shell scripting.
See the `script.sh` file for pratical demo.

```bash 
while [ condition ]; do
    # commands
done
```
### Cut Commands

cut is used to extract sections from lines of files.

Extract Specific Columns from a File
Extract characters 1-5 and 10-15 from each line of a file.


## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-13
```

## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
