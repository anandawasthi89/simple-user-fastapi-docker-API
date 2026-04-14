# FastAPI Docker CRUD App

A minimal FastAPI application scaffolded for user management and transaction routing, built to run locally or inside Docker.

## Project Overview

This repository shows a modular FastAPI app with:
- `FastAPI` for API routing
- `SQLAlchemy` for ORM and database handling
- `python-dotenv` for environment configuration
- `Docker` and `docker-compose` for containerized development
- Custom validation and exception handling

The application currently supports a user CRUD service backed by a SQLite database and a placeholder transaction API.

## Repository Structure

- `Dockerfile` - builds the Python/FastAPI image
- `docker-compose.yml` - service configuration and local volume mapping
- `.env` - environment variables for database connection
- `requirements.txt` - Python dependencies
- `app/main.py` - FastAPI app entrypoint
- `app/core/db/DBConnection.py` - SQLAlchemy database connection
- `app/core/global_exceptions/` - global exception handlers
- `app/core/users/` - user routes, schemas, database models, services
- `app/core/transactions/` - transaction routes and request schema
- `data/` - local database storage
- `tests/` - placeholder for tests

## Key Features

- User creation, retrieval, update, and deletion APIs
- Pydantic request validation for user input
- Custom global exception handling for validation and user errors
- SQLite database configured via `.env`
- Docker-ready development environment

## Requirements

- Python 3.11+
- Docker Engine
- Docker Compose

Install Python dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Configuration

The project reads its database connection from `.env`:

```env
DB_PATH_USER="sqlite:///data/users.db"
```

If you want to switch to another database backend, update `DB_PATH_USER` accordingly.

## Running Locally

Start the app locally with Uvicorn:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then visit:

- `http://127.0.0.1:8000/docs` for the interactive Swagger UI
- `http://127.0.0.1:8000/redoc` for ReDoc documentation

## Running with Docker

Build and start the service with Docker Compose:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### User Endpoints

- `GET /users/`
  - Health check for the user service

- `GET /users/getUser?user_id={id}`
  - Retrieve a user by ID

- `POST /users/createUser`
  - Create a new user
  - Example request body:

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "bank_id": "BANK123",
  "bank_account": "1234567890",
  "email": "jane.doe@example.com"
}
```

- `PUT /users/updateUser?user_id={id}`
  - Update an existing user by ID

- `DELETE /users/deleteUser?user_id={id}`
  - Delete a user by ID

### Transaction Endpoints

- `GET /transactions/is_alive`
  - Health check for the transaction service

- `GET /transactions/get_incomplete_transactions`
  - Returns placeholder incomplete transaction data

- `POST /transactions/new_transaction`
  - Create a new transaction (placeholder implementation)

- `PUT /transactions/update_transaction/{transaction_id}`
  - Update a transaction (placeholder implementation)

- `DELETE /transactions/delete_transaction/{transaction_id}`
  - Delete a transaction (placeholder implementation)

## Notes

- The current transaction routes are placeholders and do not persist transaction records yet.
- The user service persists data to SQLite via `data/users.db`.
- The included `psycopg2-binary` dependency can be used later if switching to PostgreSQL.

## Future Improvements

- Implement full transaction persistence and business logic
- Add user listing, pagination, and search
- Add automated test coverage in `tests/`
- Add authentication and authorization
- Replace string timestamps with proper datetime fields

## License

This repository is ready for GitHub and can be extended to support production-ready CRUD workflows.
