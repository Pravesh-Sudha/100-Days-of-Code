# Day 28 of 100DaysofCode

Feeling excited to start Day 28 of 100 DaysOfCode, today, I watched [Microservice Architecture and System Design with Python & Kubernetes – Full Course](https://youtu.be/hmkF77F9TLw?si=9v395dfmBrZvUxrX) Part-1 by <b>FreeCodeCamp</b>. This video contains beginner guide to Auth Service Code,  Auth Flow Overview, MongoDB & GridFs Auth Service Deployment and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-28
```

## Installation

## 1. Install Docker

Docker is a containerization platform that allows you to create and manage containers. Follow these steps to install Docker:

### Debian/Ubuntu:

```bash
sudo apt update
sudo apt install docker.io
```

### Red Hat/CentOS:

```bash
sudo yum install docker
```

Start and enable the Docker service:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

## 2. Install kubectl

kubectl is the command-line tool for interacting with Kubernetes clusters.

### Debian/Ubuntu:

```bash
sudo apt update
sudo apt install kubectl
```

### Red Hat/CentOS:

```bash
sudo yum install kubectl
```

## 3. Install Minikube

Minikube is a tool that allows you to run a local Kubernetes cluster for development and testing purposes.

### Install kubectl (if not already installed):

Follow the previous step to install kubectl if you haven't already.

### Install Minikube:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

## 4. Install MySQL

MySQL is a popular relational database management system.

### Debian/Ubuntu:

```bash
sudo apt update
sudo apt install mysql-server
```

### Red Hat/CentOS:

```bash
sudo yum install mysql-server
```

Secure your MySQL installation:

```bash
sudo mysql_secure_installation
```

Follow the on-screen prompts to set a root password and secure your MySQL installation.

## Verification

To verify that your installations were successful, you can run the following commands:

- Check Docker version:

```bash
docker --version
```

- Check kubectl version:

```bash
kubectl version --client
```

- Check Minikube version:

```bash
minikube version
```

- Check MySQL status:

```bash
sudo systemctl status mysql
```

## Auth Service Code

Here's an explanation of the `server.py` file you provided:

```python
# Import necessary libraries
import jwt
import datetime
import os
from flask import Flask, request
from flask_mysqldb import MySQL 

# Create a Flask web server instance
server = Flask(__name__)

# Initialize MySQL database connection
mysql = MySQL(server)

# Configuration settings for MySQL
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")
```

This Python script creates a Flask web server and configures a MySQL database connection using the Flask-MySQLdb extension. It reads MySQL configuration details (host, user, password, database name, and port) from environment variables.

```python
@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    # Check if authentication credentials are provided
    if not auth:
        return "Missing credentials", 401

    # Check the database for the provided username (email) and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        # Compare the provided username and password with database values
        if auth.username != email or auth.password != password:
            return "Invalid credentials", 401
        else:
            # If credentials are valid, create and return a JSON Web Token (JWT)
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "Invalid credentials", 401
```

This code defines a route `/login` that listens for HTTP POST requests. It expects authentication credentials (username and password) in the request's `Authorization` header.

- It first checks if authentication credentials are provided. If not, it returns a "Missing credentials" response with a status code of 401 (Unauthorized).

- It then queries a MySQL database for the provided username (email) and password. The SQL query is parameterized to prevent SQL injection.

- If a matching record is found in the database, it retrieves the email and password from the database.

- It compares the provided credentials with the database values. If they match, it generates a JSON Web Token (JWT) using a `createJWT` function (not shown in the provided code) and returns it with a status code of 200 (OK).

- If the provided credentials are incorrect or not found in the database, it returns an "Invalid credentials" response with a status code of 401 (Unauthorized).


```python
# Function to create a JSON Web Token (JWT)
def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )
```

The `createJWT` function generates a JSON Web Token (JWT) based on the provided `username`, `secret` (a secret key), and `authz` (a boolean indicating authorization level). The JWT includes:

- `"username"`: The provided username.
- `"exp"` (Expiration Time): The token's expiration time, set to one day (24 hours) from the current time in UTC.
- `"iat"` (Issued At): The time at which the token was issued, in UTC.
- `"admin"`: An authorization flag that indicates whether the user is an admin (as specified by the `authz` parameter).

```python
@server.route('/validate', methods=['POST'])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "Missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]
    try:
        decoded = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
        )
    except Exception as e:
        return f"Not authorized: {e}", 403

    return decoded, 200
```

The `/validate` route is defined to validate a JWT provided in the `Authorization` header of an HTTP POST request. Here's how it works:

- It extracts the JWT from the `Authorization` header, assuming it follows the format `"Bearer <token>"`.

- It attempts to decode the JWT using the specified secret key (`os.environ.get("JWT_SECRET")`) and the HS256 algorithm. If the decoding is successful, it returns the decoded JWT payload (claims) as a response with a status code of 200 (OK).

- If the JWT is missing or cannot be decoded (e.g., due to an invalid signature), it returns a "Missing credentials" response with a status code of 401 (Unauthorized) or a "Not authorized" response with a status code of 403 (Forbidden), depending on the error encountered.

```python
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)
```

The script's main block ensures that the Flask server (`server`) runs when the script is executed directly (not when it's imported as a module). It runs the server on all available network interfaces (`0.0.0.0`) and listens on port 5000.

Make sure to configure the necessary environment variables (e.g., `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB`, `MYSQL_PORT`, and `JWT_SECRET`) before running this Flask application. Additionally, you should handle database connections and implement the required endpoints and database schema (`user` table) for this code to work correctly in a production environment.

## Dockerfile

```markdown
### Base Image Selection

```dockerfile
FROM python:3.10-slim-bullseye
```

- This Dockerfile starts with a base image of Python 3.10 based on the `slim-bullseye` variant. The base image provides the Python runtime and essential libraries needed for your application.

### Package Installation

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
       build-essential default-libmysqlclient-dev pkg-config \
    && pip install --no-cache-dir --upgrade pip
```

- This section updates the package list and installs necessary system packages using `apt-get`. Here's what's being installed:
  - `build-essential`: A package containing essential build tools and libraries.
  - `default-libmysqlclient-dev`: Development files for the MySQL client library.
  - `pkg-config`: A tool used to manage compile and link flags for libraries.

- After installing system packages, it upgrades `pip` to the latest version using `pip install`.

### Working Directory

```dockerfile
WORKDIR /app
```

- The `WORKDIR` instruction sets the working directory inside the Docker container to `/app`. This is where your application code and files will be placed.

### Application Setup

```dockerfile
COPY ./requirements.txt /app
```

- This command copies the `requirements.txt` file from your local directory to the `/app` directory in the container. The `requirements.txt` file typically contains a list of Python packages and their versions required for your application.

```dockerfile
RUN pip install --no-cache-dir --requirement /app/requirements.txt
```

- Here, the Dockerfile uses `pip` to install the Python packages specified in the `requirements.txt` file. The `--no-cache-dir` option ensures that cached package files are not used, which can help reduce image size.

```dockerfile
COPY . /app
```

- This command copies the entire content of your local directory (where the Dockerfile is located) into the `/app` directory within the container. This includes your application code, scripts, and any other files needed to run your application.

### Exposing a Port

```dockerfile
EXPOSE 5000
```

- The `EXPOSE` instruction informs Docker that the container will listen on port 5000. However, this instruction does not actually publish the port; it's a form of documentation to indicate which ports are intended to be used by the container.

### Running the Application

```dockerfile
CMD [ "python3", "server.py" ]
```

- Finally, the `CMD` instruction specifies the command that will be executed when the container starts. In this case, it runs a Python script named `server.py` using the Python 3 interpreter.

This Dockerfile is intended to create a containerized environment for your Python application, ensuring that all required dependencies are properly installed.

