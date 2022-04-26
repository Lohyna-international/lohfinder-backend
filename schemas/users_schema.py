from schemas.base_schema import BaseDBModel, OID
from typing import Optional


class UserSchema(BaseDBModel):
    id: Optional[OID]
    username: str
    city: str


# add your model schemas here. Schema is used for validation.
