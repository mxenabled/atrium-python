import json

class User:
    guid = None
    identifier = None
    is_disabled = None
    metadata = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        self.guid = parsedJSON["guid"]
        self.identifier = parsedJSON["identifier"]
        self.is_disabled = parsedJSON["is_disabled"]
        self.metadata = parsedJSON["metadata"]
