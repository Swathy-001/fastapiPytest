import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Initialize FastAPI app
app = FastAPI()

@pytest.mark.asyncio
async def test_create_user():
    url = "https://reqres.in/api/users"  
    payload = {
        "name": "Swathy",
        "job": "QA Tester"
    }
    
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(url, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Swathy"
    assert response.json()["job"] == "QA Tester"

