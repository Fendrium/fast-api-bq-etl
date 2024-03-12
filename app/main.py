from fastapi import FastAPI
from faker import Faker
from random import randint

app = FastAPI()
fake = Faker()


# Home
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Generate fake user
def fake_user():
    return {
        "first name": fake.first_name(),
        "last name": fake.last_name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "website": fake.url(),
        "score": randint(0, 100),
    }


# Generate number of fake users
@app.get("/fake-users/{number}")
async def fake_users(number: int):
    users = {}
    for i in range(number):
        user = fake_user()
        users[i] = user
    return users
