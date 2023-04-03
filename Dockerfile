# Set the base image to Ubuntu
FROM ubuntu:latest

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    redis

# Copy the app directory to the image and set it as the working directory
COPY app /app
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
COPY app app
RUN pip3 install -r requirements.txt
ENV PYTHONPATH=/app

# Expose the port that the app will run on
EXPOSE 5000

# Start the app
CMD ["python3", "main.py"]
