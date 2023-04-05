# Flask Redis User Management API

A simple user management RESTful API built with Flask and Redis running on an EC2(AWS) instance. (Note : if you want to test the application please let us know so that we launch the instance)

## Features

- Welcome message
- Health check
- Retrieve all users
- Create a user
- Retrieve a user
- Update a user
- Delete a user


## API Endpoints

- Welcome message: `GET /`
- Health check: `GET /healthcheck`
- Retrieve all users: `GET /users`
- Create a user: `POST /users`
- Retrieve a user: `GET /users/<int:user_id>`
- Update a user: `PUT /users/<int:user_id>`
- Delete a user: `DELETE /users/<int:user_id>`


## Requirements

- Python 3.7+
- Flask
- Flask-Redis
- pytest (for testing)
- Docker desktop (for running the application locally)

## Installation

1. Clone the repository:

```git clone https://github.com/ismaildaoudi21/Devops-Project-Ismail-Kim.git```

2. Change into the project directory:

```cd project```


3. Install the dependencies:

```pip install -r requirements.txt```


## Running the Application Locally

Start the application using the following command:

```python run.py``` or ```python3 run.py```


The application will be accessible at `http://127.0.0.1:5000` if you run it locally.

## Running the Tests

Run the tests using the following command:

```pytest tests -v```


## Running the Application using Vagrant

To run the application make sure you are in the correct folder using the following command:

```cd iac``` it's where the Vagrantfile is stored.

Then run the following command to start the VM & run the application:

```vagrant up```

You can also ssh into the VM using the command:

```vagrant ssh```

You can find the application's folder ```cd /project```


The application will be accessible at `http://192.168.56.11:5000/`.


## Running the Application using Docker

Open Docker Desktop and make sure it's running.

Then run the following command to build the image:

```docker build -t flask-redis-user-management-api .```

Then run the following command to run the container:

```docker run -p 5000:5000 flask-redis-user-management-api```

The application will be accessible at `http://[LOCAL_HOST_IP]:5000/`.

## Push the image to Docker Hub

To push the image to Docker Hub, you need to create an account on Docker Hub and create a repository.

Login to Docker Hub using the following command:

```docker login```

Then run the following command to tag the image:

```docker tag flask-redis-user-management-api [DOCKER_HUB_USERNAME]/devops-project-dsti-a22```

Then run the following command to push the image to Docker Hub:

```docker push [DOCKER_HUB_USERNAME]/devops-project-dsti-a22```

My full commands for the image pushing are:

```docker login``` (I used my Docker Hub credentials)

```docker tag flask-redis-user-management-api nguyenkduy/devops-project-dsti-a22```

```docker push nguyenkduy/devops-project-dsti-a22```

(Remember you need to create a docker image as described in the previous section)

You can check the repository on Docker Hub using the following link:

https://hub.docker.com/repository/docker/nguyenkduy/devops-project-dsti-a22

## Running the Application using Docker Compose

Open Docker Desktop and make sure it's running.

Then run the following command to build the image and run the container:

```docker compose up```

The application will be accessible at `http://[LOCAL_HOST_IP]:5000/`.

## License

This project is created by Ismail DAOUDI & Kim Duy NGUYEN





