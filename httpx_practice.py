import httpx
from tools.fakers import get_random_email

payload = {
    "email": get_random_email(),
    "password": "P@ssw0rd",
    "lastName": "kommanch",
    "firstName": "kommanch",
    "middleName": "kommanch"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.json())
print(response.status_code)