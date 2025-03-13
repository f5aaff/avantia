from pydantic import BaseModel

class Laureate(BaseModel):
    firstname: str
    surname: str = None
    category: str
    year: str
    motivation: str
