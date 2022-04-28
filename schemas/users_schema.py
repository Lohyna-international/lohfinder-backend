from schemas.base_schema import BaseDBModel, OID
from typing import Optional


class UserSchema(BaseDBModel):
    id: Optional[OID]
    password_hash: str
    username: str
    full_name: str
    city: str


class Token(BaseDBModel):
    id: Optional[OID]
    access_token: str
    token_type: str
