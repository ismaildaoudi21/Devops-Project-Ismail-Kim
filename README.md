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

Start the application using the following command:

```vagrant up```

The application will be accessible at `http://192.168.56.11:5000/`.





## License

This project is created by Ismail DAOUDI & Kim Duy NGUYEN





