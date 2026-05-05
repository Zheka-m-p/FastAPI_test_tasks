from pydantic import BaseModel

class UrlAddSchema(BaseModel):
    url: str
    short_url: str


class URLSchema(UrlAddSchema):
    id: int

