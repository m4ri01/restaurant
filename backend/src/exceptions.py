from fastapi import HTTPException,status

incorrect_password = HTTPException(status_code=400, detail="Incorrect password")
username_already_exists = HTTPException(status_code=400, detail="username already exists")
email_already_exists = HTTPException(status_code=400, detail="email already exists")
invalid_token = HTTPException(status_code=401, detail="Invalid token")