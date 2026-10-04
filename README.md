# Rowdy

Venue management application, built with FastAPI, async SQLAlchemy, PostgreSQL (PostGIS) and Redis.

## Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)
- Docker with Docker Compose

## Getting started

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Start PostgreSQL and Redis:

   ```bash
   docker compose up -d
   ```

3. Install dependencies:

   ```bash
   uv sync
   ```

4. Run the API in development mode:

   ```bash
   uv run fastapi dev app/main.py
   ```

The API runs at <http://localhost:8000>, with interactive docs at <http://localhost:8000/docs>.

## Configuration

Settings are read from environment variables or `.env`:

| Variable       | Example                                                  |
| -------------- | -------------------------------------------------------- |
| `DATABASE_URL` | `postgresql+asyncpg://rowdy:rowdy@localhost:5432/rowdy`  |
| `REDIS_URL`    | `redis://localhost:6379/0`                               |

## Endpoints

- `GET /health`: checks that the API can reach the database.

## Development

```bash
uv run ruff check .
uv run ruff format .
uv run pytest
```
