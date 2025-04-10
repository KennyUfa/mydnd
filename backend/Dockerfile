# syntax=docker/dockerfile:1

# Use a slim Python base image for efficiency
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /backend

# Copy the requirements file and install dependencies in a virtual environment
COPY requirements.txt requirements.txt
# Установка зависимостей

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt


# Copy the application code into the container
COPY . .

# Set the PATH to include the virtual environment's bin directory
ENV PATH="/backend/.venv/bin:$PATH"

# Expose the port the application runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]