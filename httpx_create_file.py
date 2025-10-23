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

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response: ", login_response_data)

create_files_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
create_files_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data = {"filename": "new_image.png", "directory": "courses_data"},
    files={"upload_file": open("./testdata/files/image.png", "rb")},
    headers=create_files_header
)
create_files_data = create_files_response.json()
print("Create files data: ", create_files_data)