from uuid import uuid4
from fastapi import FastAPI, HTTPException
import bcrypt
from schemas.userSchema import UserAuth, UserRegister
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client.user_db
collection = db["user_collection"]

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def is_email_registered(email: str) -> bool:
    return collection.find_one({"email": email}) is not None

def is_username_registered(username: str) -> bool:
    return collection.find_one({"username": username}) is not None

def is_user_registered(email: str, password: str) -> bool:
    user = collection.find_one({"email": email})
    if not user:
        return False

    return bcrypt.checkpw(password.encode(), user['password'].encode())

@app.post("/register")
async def register(user_data: UserRegister):
    if is_username_registered(user_data.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if is_email_registered(user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user_data.password)
    user_id = str(uuid4())
    new_user = {
        "user_id": user_id,
        "username": user_data.username,
        "email": user_data.email,
        "password": hashed_password,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
    }
    collection.insert_one(new_user)

    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user_data: UserAuth):
    user = collection.find_one({"email": user_data.email}, {"email": 1})
    if user is None or not is_user_registered(user_data.email, user_data.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"message": "Login successful", "user": user}
