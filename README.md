# Flask Redis User Management API

A simple user management RESTful API built with Flask and Redis.

## Features

- Welcome message
- Health check
- Create a user
- Retrieve a user
- Retrieve all users
- Update a user
- Delete a user


## Requirements

- Python 3.7+
- Flask
- Flask-Redis
- pytest (for testing)

## Installation

1. Clone the repository:

```git clone https://github.com/yourusername/my_project.git```

2. Change into the project directory:

```cd project```


3. Install the dependencies:

```pip install -r requirements.txt```


## Running the Application

Start the application using the following command:

```python run.py``` or ```python3 run.py```


The application will be accessible at `http://127.0.0.1:5000`.

## Running the Tests

Run the tests using the following command:

```pytest tests -v```


## API Endpoints

- Welcome message: `GET /`
- Health check: `GET /healthcheck`
- Retrieve all users: `GET /users`
- Create a user: `POST /users`
- Retrieve a user: `GET /users/<int:user_id>`
- Update a user: `PUT /users/<int:user_id>`
- Delete a user: `DELETE /users/<int:user_id>`

## License

This project is created by Ismail DAOUDI & Kim Duy NGUYEN




