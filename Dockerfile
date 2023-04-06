# Start with the base image
FROM python:3.8-alpine as base

# Install required packages
RUN apk add --no-cache gcc musl-dev linux-headers

# For the Flask app
FROM base as flask-app

# Copy the requirements file into the image
COPY requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

# For Redis
FROM base as redis

# Install Redis
RUN apk add --update redis

# Expose Redis port
EXPOSE 6379

# Final stage
FROM base

# Copy Flask app files from flask-app stage
COPY --from=flask-app /app /app

# Copy installed dependencies from flask-app stage
COPY --from=flask-app /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Copy Redis executable from redis stage
COPY --from=redis /usr/bin/redis-server /usr/bin/redis-server

# Run the Flask app and Redis in the background using a shell script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
