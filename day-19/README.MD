# Day 19 of 100DaysofCode

Feeling excited to start Day 19 of 100 DaysOfCode, today, I learnt about NPM full course for beginners (Part-1) in a great Video by [Codedamn](https://youtu.be/cjoTTSbOuG0?si=wuQHLd8x--mETWsh). This video includes fundamentals of NPM, How it is used in Real life project.

## Usage

Clone this repository or simply refer to the README for a quick reference on using the NPM commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-19
```

## Introduction to Node and NPM

Node.js (or simply Node) is an open-source, cross-platform JavaScript runtime environment that allows developers to run JavaScript code on the server-side. It was created by <b>Ryan Dahl</b> in 2009 and has gained widespread adoption in web development for building scalable and efficient server applications. Node.js is built on the V8 JavaScript engine developed by Google and uses an event-driven, non-blocking I/O model, which makes it well-suited for building real-time applications, APIs, and web servers.

In the context of Node.js, a Node module is a reusable block of code that encapsulates specific functionality and can be loaded into other Node.js applications. Node modules are designed to promote code reusability and maintainability. They are a fundamental part of Node.js development and enable developers to organize and structure their code effectively. They are of two types: Core Module and User-defined modules.

Node Package Manager (NPM) is a package manager for JavaScript and Node.js. It's one of the most widely used tools for managing packages, dependencies, and scripts in Node.js applications. NPM serves as a central repository for thousands of open-source JavaScript packages and allows developers to easily install, manage, and distribute these packages in their projects.

NPM provides a command-line interface (CLI) for interacting with packages and offers a variety of features, including version management, package publishing, and dependency resolution.

## NPM vs. Yarn
NPM has a strong competitor in Yarn, another package manager for JavaScript and Node.js. Both NPM and Yarn have similar core functionality, but there are some key differences:

1. Package Locking:
NPM: Historically, NPM used npm-shrinkwrap.json for package locking. In more recent versions, it introduced package-lock.json.

Yarn: Yarn was created with a focus on deterministic builds from the beginning and uses yarn.lock for package locking.

2. Speed:
NPM: While NPM has improved in terms of speed, it used to be slower than Yarn for package installations.

Yarn: Yarn was initially praised for its speed and caching mechanisms.

3. Consistency:
NPM: With the introduction of package-lock.json, NPM aimed to achieve consistency and predictability in package installations.

Yarn: Yarn was built with a strong focus on consistency, ensuring that the same dependencies always lead to the same installed packages.

4. Workspaces:
NPM: NPM added support for workspaces with the introduction of NPM v7, allowing better management of monorepos with multiple packages.

Yarn: Yarn has had workspaces support for longer, making it a popular choice for monorepo setups.

5. User Experience:
NPM: NPM's CLI is straightforward and user-friendly.

Yarn: Yarn's CLI also offers a smooth user experience.

It's important to note that the choice between NPM and Yarn often comes down to personal preference and project requirements. Both package managers have their strengths, and developers can use either based on their specific needs.

## Installation 

- Check for Existing Installations: Before installing Node.js and npm, check if they are already installed on your system. Open a terminal or command prompt and run the following commands:

```bash
node -v
npm -v
```

- If you see version numbers in the output, it means Node.js and npm are already installed. You can skip the installation steps.

- Download Node.js and npm:
    - Visit the official Node.js website at https://nodejs.org/
    - Download the recommended version (usually the LTS or Long-Term Support version) for your operating      system. The LTS version is a stable release and is suitable for most users.
    - Install Node.js and npm:

- On Windows:
    - Run the downloaded installer.
    - Follow the installation wizard's instructions.
    - Node.js and npm will be installed on your system.

- On macOS:
    - Run the downloaded macOS installer package (usually a .pkg file).
    - Follow the installation instructions.
    - Node.js and npm will be installed on your Mac.

- On Linux (Debian/Ubuntu):
    - Open a terminal.
    - Navigate to the directory where the downloaded package is located.
    - Install Node.js and npm using apt:

    ```bash
    sudo apt update
    sudo apt install nodejs npm
    ```

- Verify Installation: After installation, open a terminal or command prompt and run the following commands to verify that Node.js and npm have been installed successfully:

```bash
node -v
npm -v
```

- You should see the version numbers of Node.js and npm in the output.

## Basic NPM Commands

- Initializing a Project
To start a new Node.js project, navigate to your project directory in the terminal and run:

```bash
npm init
```

- Installing Packages
You can use npm to install packages and dependencies for your project. To install a package, run:

```bash 
npm install package-name  or
npm i package-name
```

- Uninstalling Packages
To uninstall a package, use the uninstall command:

```bash 
npm uninstal package-name   or
npm remove package-name
```

- Listing Installed Packages
You can list all installed packages and their versions using the ls or list command:

```bash 
npm ls
```

- Updating Packages
To update packages to their latest versions, run:

```bash 
npm update
```

## Local vs Global Modules

When working with npm (Node Package Manager), you can install packages as either local or global modules. The choice between local and global modules depends on your project's requirements and use cases. Here's a comparison of local and global npm modules:

Local npm Modules:

- Installed in a Specific Project Directory: Local modules are installed in a specific project directory (usually in a node_modules folder within your project's root directory). They are scoped to the project, meaning they are available only for that project.

- Project Dependency: Local modules are typically used for project-specific dependencies. Each project can have its own set of dependencies, isolated from other projects.

- Declared in package.json: Local module dependencies are declared in the project's package.json file. When you share your project with others, they can easily install the same dependencies using npm install by reading the package.json file.

- Scoped to Node.js Environment: Local modules are available only when you are working within the project directory. This ensures that dependencies are consistent across different projects.

- Recommended for Most Use Cases: For most Node.js projects, it's recommended to use local modules. It helps maintain project-specific dependencies and avoids conflicts with different project versions.

Global npm Modules:

- Installed Globally: Global modules are installed globally on your system, outside the scope of any specific project. They are installed in a global directory (e.g., /usr/local/lib/node_modules on Unix-based systems or %AppData%\npm\node_modules on Windows).

- Accessible from Anywhere: Global modules are accessible from any directory or project on your system, making them available for use in various projects or as command-line tools.

- Not Declared in package.json: Global modules are not declared as dependencies in a project's package.json. This means they are not automatically installed for other users or collaborators when they clone your project.

- Useful for Command-Line Tools: Global modules are often used for command-line tools that you want to run from the command prompt regardless of your current project.

- Use with Caution: Installing too many global modules can lead to version conflicts and make it difficult to manage dependencies. It's generally recommended to use local modules for project-specific dependencies.

In summary, local npm modules are the default and recommended choice for most projects. They provide isolation and version control for project-specific dependencies. Global npm modules are suitable for command-line tools and utilities that you want to make available system-wide. However, you should use global modules sparingly to avoid dependency conflicts and maintain a clean development environment.