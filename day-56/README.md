# Day 56 of 100DaysofCode

Feeling excited to start Day 56 of 100 DaysOfCode, today, I watched an amazing Node.js tutorial by CodeWithHarry in hindi. The video provides a beginner guide to node, how it works, and all the essential components of Node. For referneces, [Click](https://youtu.be/BLl32FvcdVM?si=30gSNHyksTulf043) to watch the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-56
```

# Node.js

Node.js is an open-source, server-side JavaScript runtime environment that allows you to execute JavaScript code on the server, making it a powerful tool for building scalable network applications and server-side scripting. This readme file provides an overview of Node.js, its architecture, how it works, installation instructions, and additional resources to help you get started.

It is free and open source server envirnment, Javascript can be used on the server and a single language for both frontend and backend

## Frontend

The frontend refers to the user interface and user experience of the application. It's what the user interacts with directly. In our to-do list application, the frontend includes the visual elements users see and interact with, such as the task input form, the list of tasks, buttons for marking tasks as completed, and any other graphical elements.

### Everyday Use Case Example

Imagine you are using a to-do list app on your phone. The frontend is the part of the app that you see and interact with directly. When you open the app, you see a clean and user-friendly interface that allows you to add, edit, and mark tasks as completed. This is the frontend of the application.

## Backend

The backend is the behind-the-scenes part of the application that handles the logic, processes data, and communicates with the database. It's responsible for storing and retrieving tasks, managing user authentication, and performing other server-side operations. In our to-do list application, the backend handles tasks such as saving new tasks, updating existing ones, and retrieving tasks from the database.

### Everyday Use Case Example

Continuing with the to-do list app example, let's say you add a new task on the frontend – "Buy groceries." When you hit the "Add" button, the frontend sends a request to the backend, instructing it to save the new task in the database. The backend receives this request, processes it, and ensures that the task is stored securely. Later, when you open the app again, the backend retrieves the tasks from the database and sends them to the frontend, which displays the updated list.

# npm (Node Package Manager) - Readme

npm is the default package manager for Node.js, a JavaScript runtime environment. It allows developers to easily install, manage, and share third-party packages and libraries. These packages can be anything from small utility libraries to entire frameworks. npm simplifies the process of integrating external code into your projects, making development more efficient and collaborative.

## Basic Commands

### 1. Initializing a Project

To initialize a new Node.js project and create a `package.json` file (a file that holds metadata about the project and its dependencies), use the following command:

```bash
npm init
```

Follow the prompts to set up your project.

### 2. Installing Packages

To install a package and add it to your project's dependencies, use the following command:

```bash
npm install <package-name>
```

For example:

```bash
npm install lodash
```

### 3. Listing Installed Packages

To list all the packages installed in your project, use:

```bash
npm ls
```

### 4. Installing Packages Globally

To install a package globally (making it available system-wide), use the `-g` flag:

```bash
npm install -g <package-name>
```

### 5. Removing Packages

To remove a package from your project's dependencies, use:

```bash
npm uninstall <package-name>
```

### 6. Updating Packages

To update all packages to their latest versions, use:

```bash
npm update
```

### 7. Running Scripts

You can define scripts in the `scripts` section of your `package.json` file and execute them using:

```bash
npm run <script-name>
```

For example:

```bash
npm run start
```

