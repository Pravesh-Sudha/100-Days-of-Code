# Day 30 of 100DaysofCode

Feeling excited to start Day 30 of 100 DaysOfCode, today, I watched [Microservice Architecture and System Design with Python & Kubernetes – Full Course](https://youtu.be/hmkF77F9TLw?si=9v395dfmBrZvUxrX) Part-3 by <b>FreeCodeCamp</b>. This video contains beginner guide to Convertor Service Deployment, Notification service code, Notification Service Deployment and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-30
```

## Consumer.py Explaination

`consumer.py` is a Python script that serves as a consumer for processing messages from a message queue using the RabbitMQ message broker. It takes incoming messages, processes them, and stores the results in a MongoDB database.

### Prerequisites

Before running `consumer.py`, make sure you have the following dependencies installed:

- [pika](https://pypi.org/project/pika/): A Python library for interacting with RabbitMQ.
- [pymongo](https://pypi.org/project/pymongo/): A Python driver for MongoDB.
- [gridfs](https://pypi.org/project/gridfs/): A module for working with MongoDB's GridFS, used for storing binary data such as video files.
- [convert](#): An external module (`to_mp3.py`) that provides functionality for converting videos to MP3 format.

### How it Works

1. **MongoDB Setup**:

   - The script connects to a MongoDB server running at `host.minikube.internal` on port `27017`.
   - It interacts with two MongoDB databases: `videos` and `mp3s`.

2. **RabbitMQ Connection**:

   - The script establishes a connection to the RabbitMQ message broker running at the `rabbitmq` host.
   - The connection is set up using `pika.BlockingConnection` with the appropriate connection parameters.

3. **Message Consumption**:

   - The script defines a `callback` function that is executed when a message is received from the message queue.
   - Inside the `callback` function, it invokes the `to_mp3.start` function to process the incoming message.
   - If processing succeeds (`to_mp3.start` returns no errors), the script acknowledges the message using `ch.basic_ack`.
   - If there is an error during processing, the script rejects the message using `ch.basic_nack`.

4. **Queue Consumption**:

   - The script consumes messages from a queue specified in the environment variable `VIDEO_QUEUE`.
   - Messages are processed one by one as they arrive, and the script continuously waits for new messages.

5. **Running the Script**:

   - The script is designed to run as a standalone consumer. To start consuming messages, execute the `main` function.
   - To gracefully exit the script, press `CTRL+C`.

### Usage

To use `consumer.py`:

1. Install the required dependencies as mentioned in the "Prerequisites" section.
2. Set the `VIDEO_QUEUE` environment variable to specify the name of the queue from which the script should consume messages.
3. Run the script using Python:

   ```bash
   python consumer.py
   ```

## Gateway/server.py Explaination

`server.py` is a Python script that implements a server using the Flask framework. This server provides endpoints for user authentication, file uploads, and potentially file downloads (although the implementation for file downloads is pending). It interacts with a MongoDB database for user authentication and a RabbitMQ message broker for file uploads.

### Prerequisites

Before running `server.py`, make sure you have the following dependencies installed:

- [Flask](https://flask.palletsprojects.com/): A web framework for Python.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/): An extension for Flask that simplifies interaction with MongoDB.
- [pika](https://pika.readthedocs.io/en/stable/): A Python library for interacting with RabbitMQ.
- [MongoDB](https://www.mongodb.com/): A NoSQL database used for user authentication.
- [RabbitMQ](https://www.rabbitmq.com/): A message broker used for handling file uploads.

### How it Works

1. **Flask Server Setup**:

   - The script creates a Flask server instance named `server`.
   - It configures the MongoDB connection URI to `"mongodb://host.minikube.internal:27017/videos"`.

2. **MongoDB and GridFS**:

   - The script uses `Flask-PyMongo` to set up a connection to the MongoDB database.
   - It initializes a `GridFS` object named `fs` for working with MongoDB's GridFS, which is used for storing binary data, such as video files.

3. **RabbitMQ Connection**:

   - The script establishes a connection to the RabbitMQ message broker using `pika`.
   - It creates a channel named `channel` for communication with RabbitMQ.

4. **User Authentication**:

   - The `/login` endpoint handles user authentication. It validates user credentials using the `access.login` function.
   - If authentication is successful, it returns a token; otherwise, it returns an error message.

5. **File Upload**:

   - The `/upload` endpoint handles file uploads. It requires a valid access token.
   - If the user has admin privileges (`access['admin']`), it expects exactly one file to be uploaded.
   - It uses the `util.upload` function to upload the file to GridFS and send a message to RabbitMQ for further processing.
   - It returns "Success" on successful upload or an error message on failure.

6. **File Download**:

   - The `/download` endpoint is a placeholder for file download functionality and is not yet implemented.

7. **Running the Server**:

   - If the script is executed directly (not imported as a module), it starts the Flask server to listen on `0.0.0.0` (all available network interfaces) and port `8080`.

### Usage

To use `server.py`:

1. Install the required dependencies as mentioned in the "Prerequisites" section.
2. Ensure that MongoDB and RabbitMQ servers are running and accessible.
3. Make sure to set up the MongoDB connection URI (`MONGO_URI`) according to your MongoDB server configuration.
4. Run the script using Python:

   ```bash
   python server.py
    ```

## Validate.py Explanation
`validate.py` is a Python script that provides a function for validating authentication tokens. It checks the validity of a provided token by sending a request to an authentication service and verifying the response.

### Usage

To use `validate.py` in your project:

1. Ensure you have the necessary dependencies installed:

   - [os](https://docs.python.org/3/library/os.html): A Python standard library module for interacting with the operating system.
   - [requests](https://docs.python-requests.org/en/master/): A Python library for making HTTP requests.

2. Import the `token` function from `validate.py` into your project.

3. Call the `token` function with a request object that contains the authentication token in the headers.

   ```python
   from validate import token

   # Example usage:
   auth_token = request.headers.get("Authorization")
   access, error = token(request)
   if not error:
       # The token is valid, and 'access' contains the response text.
   else:
       # An error occurred during token validation, and 'error' contains the error message and status code.
   ```

### Function Explanation

The `token` function in `validate.py` performs the following steps:

1. **Check for Authorization Header**:

   - It first checks if the "Authorization" header is present in the provided request.

2. **Token Retrieval**:

   - If the "Authorization" header is found, it retrieves the token from the header.

3. **Token Validation**:

   - It sends an HTTP POST request to an authentication service, which is specified by the `AUTH_SVC_ADDRESS` environment variable.
   - The token is included in the request headers.
   - It expects a response with a status code of 200 for a successful validation.
   - If the response status code is 200, it returns the response text (the validated access) and no error.
   - If the response status code is not 200, it returns no access and an error containing the response text and status code.

## Access.py Explanation

`access.py` is a Python script that provides a function for user authentication. It takes user credentials in the form of Basic Authentication and sends a request to an authentication service to verify the provided credentials.

### Usage

To use `access.py` in your project:

1. Ensure you have the necessary dependencies installed:

   - [os](https://docs.python.org/3/library/os.html): A Python standard library module for interacting with the operating system.
   - [requests](https://docs.python-requests.org/en/master/): A Python library for making HTTP requests.

2. Import the `login` function from `access.py` into your project.

3. Call the `login` function with a request object that contains the user's credentials in the `Authorization` header.

   ```python
   from access import login

   # Example usage:
   auth_credentials = request.authorization
   token, error = login(request)
   if not error:
       # User authentication is successful, and 'token' contains the response text.
   else:
       # An error occurred during authentication, and 'error' contains the error message and status code.
   ```

### Function Explanation

The `login` function in `access.py` performs the following steps:

1. **Check for Authorization Credentials**:

   - It first checks if the request contains valid Basic Authentication credentials in the `Authorization` header.

2. **Basic Authentication**:

   - If valid credentials are found, it extracts the username and password from the `Authorization` header.
   - It constructs a Basic Authentication tuple `(username, password)` for use in the HTTP request.

3. **Authentication Request**:

   - It sends an HTTP POST request to an authentication service, which is specified by the `AUTH_SVC_ADDRESS` environment variable.
   - The Basic Authentication tuple is included in the request.
   - It expects a response with a status code of 200 for successful authentication.
   - If the response status code is 200, it returns the response text (the authentication token) and no error.
   - If the response status code is not 200, it returns an error containing the response text and status code.
