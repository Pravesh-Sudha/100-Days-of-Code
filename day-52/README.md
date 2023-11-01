# Day 52 of 100DaysofCode

Feeling excited to start Day 52 of 100 DaysOfCode, today, I create a Nginx Web-app project. This project provides a beginner guide to nginx, how it works, creating, updating and deleting operations and many more. For referneces, [Watch](https://youtu.be/J6mDkcqU_ZE?si=U_XznDhuURGSZPdV) the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-52
```

# Nginx - A High-Performance Web Server and Reverse Proxy Server

![Nginx Logo](https://nginx.org/nginx.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
   - [Linux](#linux)
   - [Windows](#windows)
   - [macOS](#macos)
4. [Configuration](#configuration)
5. [Basic Usage](#basic-usage)
6. [Common Use Cases](#common-use-cases)
7. [Contributing](#contributing)

## Introduction

[Nginx](https://nginx.org/) (pronounced "engine-x") is a powerful and high-performance web server, as well as a reverse proxy server. It's known for its efficiency, scalability, and reliability, making it a popular choice for serving web applications and websites. Nginx is open-source software and has a large community of users and developers.

## Features

- Web server: Nginx can serve static and dynamic content efficiently.
- Reverse proxy: It can act as a reverse proxy server to distribute client requests to multiple backend servers.
- Load balancing: Nginx can distribute incoming traffic to balance the load among multiple server instances.
- SSL/TLS termination: Supports secure connections using SSL/TLS encryption.
- URL rewriting and redirection: Can manipulate URLs to control how requests are handled.
- Caching: Nginx can cache content to improve website performance.
- High concurrency: Handles a large number of simultaneous connections with low resource usage.
- Extensibility: Supports various third-party modules to extend its functionality.

## Installation

### Linux

1. **Ubuntu/Debian**:

   ```bash
   sudo apt update
   sudo apt install nginx
   ```

2. **CentOS/RHEL**:

   ```bash
   sudo yum install epel-release
   sudo yum install nginx
   ```

### Windows

1. Download the Windows version of Nginx from the [Nginx website](https://nginx.org/en/download.html).

2. Extract the downloaded ZIP archive to your desired installation directory.

3. Navigate to the installation directory and run `nginx.exe`.

### macOS

You can install Nginx on macOS using [Homebrew](https://brew.sh/):

```bash
brew install nginx
```

## Configuration

Nginx configuration files are typically located in `/etc/nginx/` on Linux systems. The main configuration file is `nginx.conf`. You can customize Nginx's behavior by editing this file. Here's a basic configuration example:

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    location / {
        root /var/www/html;
        index index.html;
    }
}
```

## Basic Usage

1. Start Nginx after installation:

   ```bash
   sudo service nginx start  # On Linux
   nginx.exe  # On Windows
   ```

2. Open a web browser and enter your server's IP address or domain name to access the default Nginx welcome page.

3. You can place your web content in the default root directory at `/var/www/html` (Linux) or the installation directory (Windows).

## Common Use Cases

Nginx is widely used for various purposes, including:

- Hosting websites and web applications.
- Load balancing and reverse proxying.
- SSL/TLS termination.
- Caching static content to reduce server load.
- URL redirection and rewriting.


## Contributing

If you'd like to contribute to Nginx, you can find the source code and information on how to get involved on the [Nginx GitHub repository](https://github.com/nginx/nginx).
