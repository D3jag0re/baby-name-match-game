# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV FLASK_APP=app/__init__.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Expose the port the app runs on
EXPOSE 8000

# Specify the command to run the application
#CMD ["gunicorn", "--bind=0.0.0.0:8000", "--timeout", "600", "--chdir", "app", "__init__:app"]

#not using gunicorn this works on port 5000
CMD ["flask", "run", "--host", "0.0.0.0"]