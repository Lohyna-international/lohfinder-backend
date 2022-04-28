from fastapi import APIRouter, Depends, HTTPException, status
from db import get_database, DatabaseManager
from fastapi.security import OAuth2PasswordRequestForm
from core.security import authenticate_user


from core.security import signJWT, JWTBearer

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/me", dependencies=[Depends(JWTBearer())])
async def get_me():
    print("Aaaa")
    return {"MES": "i"}


@router.get("/")
async def get_users(db: DatabaseManager = Depends(get_database)):
    users = await db.get_users_list()
    return users


@router.post("/token")
async def login_for_access_token(
    db: DatabaseManager = Depends(get_database),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    users = await db.get_users_list()
    user = authenticate_user(users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = signJWT(user.username)
    return {"access_token": access_token, "token_type": "bearer"}
