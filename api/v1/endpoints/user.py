from fastapi import APIRouter, Body, Depends, HTTPException, status
from db import get_database, DatabaseManager
from fastapi.security import OAuth2PasswordRequestForm
from core.security import authenticate_user, decodeJWT, get_password_hash

from core.security import signJWT, JWTBearer
from schemas.users_schema import UserSchema, UserBaseSchema

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/me")
async def get_current_user(db: DatabaseManager = Depends(get_database), token = Depends(JWTBearer())):
    token_info = decodeJWT(token)
    current_user = await db.get_user_by_username(token_info["user_id"])
    return current_user


@router.get("/", dependencies=[Depends(JWTBearer())])
async def get_users(db: DatabaseManager = Depends(get_database)):
    users = await db.get_users_list()
    return users


@router.post("/login")
async def login_for_access_token(
    db: DatabaseManager = Depends(get_database),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = signJWT(user.username)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup")
async def signup(db: DatabaseManager = Depends(get_database), user_info: UserBaseSchema = Body(...)):
    user_info.password = get_password_hash(user_info.password)
    await db.create_user(user_info.dict())
    access_token = signJWT(user_info.username)
    return {"access_token": access_token, "token_type": "bearer"}