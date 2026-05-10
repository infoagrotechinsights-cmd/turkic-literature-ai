import json
from core.vector_db import add_poem

def load_dataset():

    with open("data/poems.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for i, item in enumerate(data):

        add_poem(
            id=i,
            text=item["text"],
            metadata={
                "poet": item.get("poet"),
                "era": item.get("era")
            }
        )
