import httpx

response = httpx.get("http://127.0.0.1:8000/analytics", params={"limit": 5})
print(response.status_code)
print(response.json())
