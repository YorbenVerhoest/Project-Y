# Use the official Python image as the base image
FROM python:3.9.7

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port your application will run on
EXPOSE 8080

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
