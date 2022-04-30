from schemas.base_schema import BaseDBModel, OID
from typing import Optional


class UserBaseSchema(BaseDBModel):
    password: str
    username: str
    fullName: str
    city: str


class UserSchema(UserBaseSchema):
    id: Optional[OID]


class Token(BaseDBModel):
    id: Optional[OID]
    accessToken: str
    tokenType: str
