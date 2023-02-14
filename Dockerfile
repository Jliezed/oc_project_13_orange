# Use an official Python runtime as the base image
FROM python:3.10-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# create root directory for our project in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Upgrade the pip package to latest version
RUN pip3 install --upgrade pip

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install the shell
RUN apk add --no-cache bash

# Install git
RUN apk update && apk add git

# Copy the rest of the app's code to the container
COPY . .

# port where the Django app runs
EXPOSE 8000

# Run the server
# Not mandatory if it's already in the docker-compose
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]