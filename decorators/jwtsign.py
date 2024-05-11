import jwt
from fastapi import HTTPException, status
import secrets
from pydantic import BaseModel

JWT_SECRET = secrets.token_hex(16)
JWT_ALGORITHM = "HS256"
print(JWT_SECRET)


class Utilty(BaseModel):
    def sign(email):
        payload = {"email": email}
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    def decode(token):
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")



