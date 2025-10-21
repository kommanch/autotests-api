import httpx

login_payload = {
    "email": "kommanch@123.com",
    "password": "P@ssw0rd"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data['token']['accessToken'])
print("Status code:", login_response.status_code)

token = login_response_data['token']['accessToken']
headers = {
    "Authorization": f"Bearer {token}"
}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print("User response:", user_response.json())
print("Status code:", user_response.status_code)
