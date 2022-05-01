from schemas.base_schema import BaseDBModel


class BinSchema(BaseDBModel):
    key: str
    name: str
