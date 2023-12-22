# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app/
COPY requirements.txt /usr/src/app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app/
COPY . /usr/src/app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
