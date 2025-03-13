from fastapi import APIRouter
from app.models import Laureate
from app.database import es

router = APIRouter()

@router.post("/laureate")
def add_laureate(laureate: Laureate):
    doc = laureate.dict()
    res = es.index(index="nobel_prizes", document=doc)
    return res

@router.get("/search")
def search_laureates(query: str):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["firstname", "surname", "category", "motivation"],
                "fuzziness": "AUTO"
            }
        }
    }
    res = es.search(index="nobel_prizes", body=search_body)
    return res["hits"]["hits"]

