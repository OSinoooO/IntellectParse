from pydantic import BaseModel


class GneItem(BaseModel):
    html: str
    url: str

