from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True


user1 = User(
    id=1,
    name="user1",
    email="asd@mail.ru",
    address=Address(city="Moscow", zip_code="12312123")
)

print(user1.model_dump())
print(user1.model_dump_json())
