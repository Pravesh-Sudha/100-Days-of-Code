# Day 71 of 100DaysOfCode

Feeling excited to start Day 71 of 100 DaysOfCode, today, I created a Flask todo app. In this project, I revised basics of Flask, backend, python, sqlite and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-71
```

# Flask ToDo App

Welcome to the Flask ToDo app! This project is designed to help you build a simple ToDo list application using Flask, SQLite, and a structured code organization. Before diving into the code, let's go through some planning and considerations.

### User Functionalities
The ToDo app supports the following basic functionalities:
- Create an item
- Delete an item
- Mark an item as done
- Update an item

Additional features include:
- Categorizing ToDo items (work, personal, etc.)
- Tagging items
- Prioritizing items
- Reminder for overdue items

### Data Structure
The data for each ToDo item is structured as follows:
- Create an Item: Title, Description, CreatedOn, DueDate
- Delete an Item: _is_deleted (soft delete)
- Mark an Item Done: _is_done

### Database Schema
The SQLite database schema consists of two main tables:

1. `User`
   - Name (Text)
   - Email (Email)
   - Id (Primary Key)

2. `ToDo_Items`
   - Id (Primary Key)
   - Title (Text)
   - Description (Text)
   - CreatedOn (Date)
   - DueDate (Date)
   - _is_deleted (Boolean)
   - _is_done (Boolean)
   - CreatedBy (Foreign Key referencing User Id)

## Code Structure
To maintain code organization and follow industry standards, the code is divided into three files:

1. **app.py** - The entry and exit point to the application.
2. **service.py** - Converts requests into responses and contains business logic.
3. **models.py** - Handles database-related operations and schema definition.

### Why Three Separate Files?
- **Standards:** Following the MVC (Model View Controller) pattern for better code organization.
- **Code Maintainability:** Easier modification of specific components without affecting the entire codebase.

## Getting Started
To set up the application, follow these steps:

1. Run the SQLite database schema creation by executing the `Schema` class in `models.py`.
2. Start the application with `app.py`.

```python
# Example commands
# 1. import sqlite
import sqlite3
# 2. create a connection to DB     
conn = sqlite3.connect('todo.db')
# 3. Write your sql query   
query = "<SQLite Query goes here>"
# 4. execute the query
result = conn.execute(query)
```

## Creating Tables
Tables are created using the `Schema` class in `models.py`. Ensure that the `User` table is created before the `ToDo_Items` table.

## ToDo Operations
The `ToDoModel` class in `models.py` provides methods for CRUD operations on the ToDo table.

## Service Methods
The `ToDoService` class in `service.py` contains methods for handling ToDo-related business logic.

## View Functions
The `app.py` file contains view functions, which serve as the entry and exit points for the system. They handle user input, authentication, and logging.

## Testing the Application
1. Make sure your `app.py` is running.
2. Use Python or Postman to consume the API.

```python
# Example using Python requests
import requests
requests.post("http://localhost:5000/todo", json={"Title":"my first todo", "Description":"my first todo"})
```
