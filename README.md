# Setting up containers

enter the src directory and run the following:

```bash
docker-compose up --build
```

this will build the containers, and start them.


the end points are provided using fastAPI, and the docs can be accessed by navigating to
[localhost:8000/docs](http://localhost:8000/docs).

there is a post endpoint for adding a laureate, accepting a json object with the following structure:
```json
{
  "firstname": "bob",
  "surname": "smith",
  "category": "stuff",
  "year": "1970",
  "motivation": "really good at stuff"
}
```


there is a get endpoint expecting a string query, an example of such a query would be the following:
```http://localhost:8000/search?query=bob```.


this should respond with a response body like the following:

```json
[
  {
    "_index": "nobel_prizes",
    "_id": "n131j5UBdgKcb9cePt5x",
    "_score": 0.2876821,
    "_source": {
      "firstname": "bob",
      "surname": "smith",
      "category": "stuff",
      "year": "1970",
      "motivation": "really good at stuff"
    }
  }
]
```
