import logging
from elasticsearch import Elasticsearch, helpers
import ijson

# basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


# Connect to the Elasticsearch instance
es = Elasticsearch("http://localhost:9200")

# Function to initialize the index (Create if it doesn't exist)
def initialize_index(es, index_name):
    if es.indices.exists(index=index_name):
        log.info(f"Index {index_name} already exists.")
    else:
        # Define the index settings and mappings (optional, depending on your needs)
        index_settings = {
            "settings": {
                "number_of_shards": 1,  # Number of primary shards (you can adjust based on your data size)
                "number_of_replicas": 1  # Number of replicas
            },
            "mappings": {
                "properties": {
                    "year": {"type": "keyword"},
                    "category": {"type": "keyword"},
                    "laureates": {
                        "type": "nested",  # Nested type for laureates (array of objects)
                        "properties": {
                            "id": {"type": "keyword"},
                            "firstname": {"type": "text"},
                            "surname": {"type": "text"},
                            "motivation": {"type": "text"},
                            "share": {"type": "keyword"}
                        }
                    }
                }
            }
        }

        # Create the index
        es.indices.create(index=index_name, body=index_settings)
        log.info(f"Index {index_name} created successfully.")



# Name of the index
index_name = "nobel_prizes"

actions = []

# open the prize data file in read mode
with open('./data/prize.json', 'r') as file:
    # use ijson to stream the items from the prizes array from the json file
    objs = ijson.items(file, 'prizes.item')
    # for every prize, and for every laureate, create an action to insert
    # into elasticsearch.
    for p in objs:
        # if they do not have any laureates, assign an empty array in place of the array from the json.
        # this is to ensure a complete representation of the dataset.
        if 'laureates' not in p:
            log.warning(f"prize {p['year']} {p['category']} has no laureates. Adding empty array.")
            p['laureates'] = []
        for l in p['laureates']:
            action = {
                    "_op_type": "index",
                    "_index": index_name,
                    "source": {
                        "year": p['year'],
                        "category": p['category'],
                        "laureate": l
                        }
                    }
            actions.append(action)

    # group records in lots of 100
    if len(actions) >= 100:
        success,failed = helpers.bulk(es,actions)
        log.info(f"successfully indexed {success} docs.")
        log.warning(f"failed to index {failed} docs.")
    # if any actions still remain, i.e the source isn't divisible by 100,
    # complete the remaining actions.
    if actions:
        success,failed = helpers.bulk(es,actions)
        log.info(f"successfully indexed {success} docs.")
        log.warning(f"failed to index {failed} docs.")

