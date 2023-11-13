# Day 54 of 100DaysofCode

Feeling excited to start Day 54 of 100 DaysOfCode, today, I watched a Introduction to Node.js Tutorial by ProgrammingWithMosh. This video provides a beginner guide to Node.js, how it works, Node Architecture, creating, updating and deleting modules and many more. For referneces, [Click](https://youtu.be/TlB_eWDSMt4?si=9RIfetbmvayvDWGr) to watch the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-54
```

# Node.js

Node.js is an open-source, server-side JavaScript runtime environment that allows you to execute JavaScript code on the server, making it a powerful tool for building scalable network applications and server-side scripting. This readme file provides an overview of Node.js, its architecture, how it works, installation instructions, and additional resources to help you get started.

## Table of Contents

- [What is Node.js?](#what-is-nodejs)
- [Node.js Architecture](#nodejs-architecture)
- [How Node.js Works](#how-nodejs-works)
- [Installation](#installation)

---

## What is Node.js?

Node.js, often referred to as Node, is a runtime environment that allows you to run JavaScript code on the server side. It is built on the V8 JavaScript engine, which is the same engine that powers the Google Chrome browser. Node.js is designed to be event-driven, non-blocking, and lightweight, making it well-suited for building real-time, highly concurrent applications.

Key features and characteristics of Node.js include:

- **Non-blocking I/O:** Node.js uses an event-driven, asynchronous architecture, which means it can handle multiple concurrent operations without blocking the execution of other code.
- **V8 JavaScript engine:** Node.js leverages the high-performance V8 JavaScript engine, providing excellent execution speed.
- **CommonJS modules:** Node.js uses a module system that allows you to organize and reuse code effectively.
- **NPM (Node Package Manager):** NPM is a package manager for Node.js that makes it easy to install and manage libraries and packages.
- **Cross-platform:** Node.js is available on various operating systems, including Windows, macOS, and Linux.

## Node.js Architecture

Node.js has a single-threaded, event-driven architecture that enables asynchronous execution of code. Here's a brief overview of its architecture:

- **Event Loop:** The event loop is at the core of Node.js. It continuously checks for pending events, such as I/O operations, timers, and user-defined events. When an event is ready to be processed, it invokes the corresponding callback function.

- **Libuv:** Node.js uses the Libuv library to provide an asynchronous event-driven runtime. Libuv abstracts the underlying operating system's I/O operations, allowing Node.js to work efficiently across different platforms.

- **Callbacks:** Node.js relies heavily on callbacks. Callback functions are passed as arguments and are executed when an asynchronous operation is completed. This non-blocking approach helps Node.js handle numerous concurrent connections efficiently.

## How Node.js Works

Node.js operates by running JavaScript code on the server. Here's an overview of how it works:

1. **Server Initialization:** You create a Node.js script that sets up a server, listens to specific ports, and defines how to respond to incoming requests.

2. **Event Loop:** Node.js starts an event loop, which continuously checks for events (e.g., incoming HTTP requests, file read/write operations, timers).

3. **Non-blocking I/O:** When an event, such as an incoming request, is detected, Node.js uses non-blocking I/O operations to handle it. This ensures that the server remains responsive to other requests and operations.

4. **Callbacks:** Callback functions are used to execute code asynchronously, allowing Node.js to handle multiple concurrent requests without blocking.

5. **Modules:** Node.js uses modules for code organization and reusability. You can import and use modules as needed in your application.

6. **NPM:** Node Package Manager (NPM) provides a vast ecosystem of open-source packages and modules that can be easily integrated into your Node.js application.

## Installation

To get started with Node.js, follow these installation steps:

1. Visit the official Node.js website: [Node.js Official Website](https://nodejs.org/)

2. Download the appropriate installer for your operating system (Windows, macOS, or Linux).

3. Run the installer and follow the installation instructions.

4. After installation, you can verify that Node.js and NPM are correctly installed by opening your command prompt or terminal and running the following commands:

   ```bash
   node -v
   npm -v
   ```

   These commands should display the installed Node.js and NPM versions.

## Create, Update, and Delete Module

The Create, Update, and Delete Module allows you to interact with files and directories in Node.js. This module provides functions for creating, updating, and deleting files and directories. It's essential for file operations.

### Usage

To use this module, you can follow these steps:

1. Import the module using `require('fs')`.
2. Utilize functions like `fs.writeFileSync()`, `fs.readFile()`, and `fs.unlink()` for file manipulation.

For detailed documentation, refer to Create, Update, and Delete Module Documentation.

## OS Module

The OS Module provides various utility functions for interacting with the operating system. It allows you to access information about the system, such as architecture, platform, and more.

### Usage

To use the OS Module:

1. Import the module using `require('os')`.
2. Access functions like `os.arch()`, `os.platform()`, and `os.cpus()` for system information.

For in-depth information, refer to OS Module Documentation.

## HTTP Module

The HTTP Module in Node.js enables you to create HTTP servers and make HTTP requests. It is essential for building web applications and handling HTTP-related tasks.

### Usage

To work with the HTTP Module:

1. Import the module using `require('http')`.
2. Create an HTTP server with `http.createServer()` or make HTTP requests with `http.request()`.

For detailed documentation and examples, refer to HTTP Module Documentation.

## Path Module

The Path Module simplifies file and directory path manipulation in Node.js. It provides functions for working with paths, making it easier to handle file operations.

### Usage

To use the Path Module:

1. Import the module using `require('path')`.
2. Utilize functions like `path.join()`, `path.resolve()`, and `path.basename()` for path operations.

For more information, refer to Path Module Documentation.

## File System Module

The File System (fs) Module in Node.js allows you to work with the file system. It provides functions for reading, writing, updating, and manipulating files and directories.

### Usage

To work with the File System Module:

1. Import the module using `require('fs')`.
2. Use functions like `fs.readFile()`, `fs.writeFile()`, and `fs.readdir()` for file operations.

For a detailed guide and examples, refer to File System Module Documentation.

## Event Module

The Event Module in Node.js is crucial for building event-driven applications. It enables you to create, emit, and handle events, making it essential for handling asynchronous operations and real-time applications.

Feel free to explore each module's documentation for detailed information about their features and usage. If you have any questions or encounter issues, please refer to the official Node.js documentation or seek assistance from the Node.js community.

Happy coding!
