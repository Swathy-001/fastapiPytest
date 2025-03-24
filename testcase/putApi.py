import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Initialize FastAPI app
app = FastAPI()

@pytest.mark.asyncio
async def test_update_user():
    url = "https://reqres.in/api/users/2"  
    payload = {
        "name": "Onkar",
        "job": "QA Tester"
    }
    
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.put(url, json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Onkar"
    assert response.json()["job"] == "QA Tester"

    print("Response JSON:", response.json())
    print("Updated successfully")



