# This file will handle routing operations such as the registration and signing-in of users.
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])

users = {}


@user_router.get("/")
async def get_users() -> dict:
    return {"message": f"{users}"}


@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is alredy in use"
        )
    users[data.email] = data
    return {"message": "data added"}


@user_router.post("/signin")
async def sign_in_user(data: UserSignIn) -> dict:
    if data.email not in users:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="user not found!"
        )

    if users[data.email].password != data.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="please check your crudentials",
        )

    return {"message": f"welcome {data.email}"}
