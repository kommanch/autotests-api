import httpx


login_payload = {
    "email": 'kommanch@123.com',
    "password": 'P@ssw0rd'
}

login_response_delete = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_delete_data = login_response_delete.json()

print("Login response: ", login_response_delete_data)

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=10,
    headers={"Authorization": f"Bearer {login_response_delete_data["token"]["accessToken"]}"}
)

response = client.get("/api/v1/users/me")
response_data = response.json()

print(response_data)