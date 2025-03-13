# Brief

*Your task is to ingest a publicly available dataset of Nobel Prize winners and create a tool which is capable of searching this data using python. You can use any library or techniques, as long as it is available for free online and can be ran in a (or multiple) docker containers.*

Please take the JSON dataset available at:

https://api.nobelprize.org/v1/prize.json

and load it into a searchable database, such as ElasticSearch or MongoDB.
Then, develop a small web application (a frontend is not required) using any python web framework (e.g. Flask/FastAPI etc) to enable searching through the dataset.
The application should support text-based searches for a Laureate by their name, category, or motivation.

I would like to be able to do partial searches eg: a search for "Albret Enstein" should return a top result of "Albert Einstein".
This functionality should be accessible via HTTP endpoints (such as, /search/name= or /search/motivation=).
The exact implementation details of how you populate the database and the search API interface are up to you.
We encourage you to be creative with the search capabilities.

It is recommended that the database and web application be containerized using Docker, with the ability to communicate with each other.
You can use Docker Compose to facilitate this if you prefer.
Please provide brief instructions in a README file on how to launch the application (especially if you are not using Docker).

If time permits, consider adding an endpoint to add/amend records considering things like input validation (we use pydantic extensively for this kind of thing)
A particular focus for this technical assessment is on the ease of use, we'd like to be able to run the full application easily with a single command such as a docker run command or shell script.
