# my-first-agent

<!-- Ahoy matey! This README charts the course for running the API vessel. -->

FastAPI service to read and write JSON via `https://jsonplaceholder.typicode.com/`.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- `GET /posts/{post_id}` — Arrr! Reads a post from JSONPlaceholder.
- `POST /posts` — Avast! Writes JSON payload to JSONPlaceholder.