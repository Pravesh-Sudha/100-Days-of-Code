# Day 27 of 100DaysofCode

Feeling excited to start Day 27 of 100 DaysOfCode, today, I watched [Flask Tutorial](https://youtu.be/Z1RJmh_OqeA?si=eHFkzl4qqZUKChnS) by <b>FreeCodeCamp</b>. This video contains beginner guide to flask functionalities, how flask projects works and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-27
```

# Flask To-Do List App

This is a simple To-Do List web application built using Flask. It allows you to create, read, update, and delete tasks in your to-do list.

## Features

- Create a new task.
- View your existing tasks.
- Mark tasks as completed.
- Edit task descriptions.
- Delete tasks from your list.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run the Application](#run-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+ installed
- Pip (Python package manager) installed
- Flask framework installed
- A modern web browser

## Getting Started

### Clone the Repository

To get started with this project, clone the repository to your local machine:

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd flask-todo-app
```

### Set Up a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies. You can create one using Python's `venv` module:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install flask flask_sqlalchemy
```

### Run the Application

Start the Flask development server:

```bash
flask run
```

The application should now be running at `http://localhost:5000`. Open your web browser and navigate to this URL to access the To-Do List app.

## Usage

- **Create a Task**: Click the "Add Task" button, enter the task description, and click "Save".
- **View Tasks**: You'll see a list of your tasks on the main page.
- **Complete Task**: Click the checkbox next to a task to mark it as completed.
- **Edit Task**: Click the "Edit" button next to a task to modify its description.
- **Delete Task**: Click the "Delete" button to remove a task from the list.

## Application Structure

- `app.py`: This is the main application file where the Flask app is created. It includes routes for rendering templates and handling task-related operations using SQLAlchemy for database interaction.

- `templates/`: This directory contains the HTML templates used to render the web pages. The main template is `index.html`, which displays the task list and allows users to add, update, and delete tasks.

- `static/css/main.css`: This CSS file is used to style the web pages and center the table on the page.

- `test.db`: This is the SQLite database file where task data is stored.

## Database Model

The `Todo` class is a SQLAlchemy model representing a task. It has the following attributes:

- `id`: An integer representing the task's unique identifier.
- `content`: A string (up to 200 characters) containing the task's description.
- `completed`: An integer (default 0) representing whether the task is completed.
- `data_created`: A datetime field that stores the date and time when the task was created.

## Routes and Functionality

- `GET /`: Displays the list of tasks. Users can add new tasks, delete existing tasks, and update task descriptions.

- `POST /`: Handles the submission of the task creation form. It adds a new task to the database.

- `GET /delete/<int:id>`: Deletes a specific task based on its `id`.

- `GET /update/<int:id>`: Renders a form to update a specific task's description.

- `POST /update/<int:id>`: Handles the submission of the task update form. It updates the task's description.

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

The app will run in debug mode, and you can access it in your web browser at `http://localhost:5000/`.

## Dependencies

- Flask: A Python web framework used for building the web application.
- Flask-SQLAlchemy: An extension for Flask that simplifies database operations with SQLAlchemy.
- SQLAlchemy: An Object-Relational Mapping (ORM) library for working with databases.

## Author

Pravesh-Sudha

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.