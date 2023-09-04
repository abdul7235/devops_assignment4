from pydantic import BaseModel

class RequestData(BaseModel):
    name: str
    age: int
    location: str


