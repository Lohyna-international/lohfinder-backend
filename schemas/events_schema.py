from schemas.base_schema import BaseDBModel, OID
from typing import Optional

class EventsSchema(BaseDBModel):
    id: Optional[OID]
    created_by: str
    city: str
    title: str
    main_photo: str
    photos: str
    description: str

