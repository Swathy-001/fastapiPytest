from fastapi import FastAPI
import pytest
import httpx

# Initialize FastAPI app
app = FastAPI()

@pytest.mark.asyncio()
async def test_create_users():
    url = "https://reqres.in/api/users"  
    payload = {
        "name": "Swathy",
        "job": "QA Tester"
    }
    
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(url, json=payload)

    print("Response JSON:", response.json())

    assert response.status_code == 201
    assert response.json()["name"] == "Swathy"
    assert response.json()["job"] == "QA Tester"

    print("Response JSON:", response.json())
    print("Created successfully")

