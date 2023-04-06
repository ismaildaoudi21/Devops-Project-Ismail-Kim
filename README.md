# Flask Redis User Management API

A simple user management RESTful API built with Flask and Redis.

## Features

- Welcome message
- Health check
- Retrieve all users
- Create a user
- Retrieve a user
- Update a user
- Delete a user


## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

```git clone https://github.com/ismaildaoudi21/Devops-Project-Ismail-Kim.git```

2. Change into the project directory:

```cd project```


3. Start the application using Docker Compose:

```docker-compose up```


The application will be accessible at `http://127.0.0.1:5000`.

## Running the Tests

Tests automatically run when pushing to GitHub main branch. (or you can run them locally)


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




