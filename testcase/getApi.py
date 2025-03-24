import pytest
import httpx
from fastapi import FastAPI 


# Initialize FastAPI app
app = FastAPI()

# Test case example for API requests
@pytest.mark.asyncio
async def test_get_users():
    url = "https://reqres.in/api/users/2" 
   
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url)
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()['data'])== 5
  
