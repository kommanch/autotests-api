import httpx
from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "P@ssw0rd",
    "lastName": "kommanch",
    "firstName": "kommanch",
    "middleName": "kommanch"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()
print("Create user data: ", create_user_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response_delete = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_delete_data = login_response_delete.json()

print("Login response: ", login_response_delete_data)

headers_put = {
    "Authorization": f"Bearer {login_response_delete_data["token"]["accessToken"]}"
}
put_payload = {
    "email": get_random_email(),
    "lastName": "kommanch1",
    "firstName": "kommanch1",
    "middleName": "kommanch1"
}

patch_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}",
    headers=headers_put,
    json=put_payload
)
print(patch_user_response.json())
print(patch_user_response.status_code)
