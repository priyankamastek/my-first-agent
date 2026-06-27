"""Ahoy matey! This FastAPI vessel proxies read/write JSON requests."""

from typing import Any, Dict

import httpx
from fastapi import FastAPI, HTTPException


app = FastAPI(title="JSONPlaceholder Proxy API")
BASE_URL = "https://jsonplaceholder.typicode.com"


@app.get("/posts/{post_id}")
async def read_post(post_id: int) -> Dict[str, Any]:
    # Arrr! Fetch a post from the upstream harbor.
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"{BASE_URL}/posts/{post_id}")

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to read JSON from upstream API.",
        )

    return response.json()


@app.post("/posts")
async def write_post(payload: Dict[str, Any]) -> Dict[str, Any]:
    # Avast! Send JSON cargo to the upstream API.
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(f"{BASE_URL}/posts", json=payload)

    if response.status_code not in (200, 201):
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to write JSON to upstream API.",
        )

    return response.json()
