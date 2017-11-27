import json

class Challenge:
    field_name = None
    guid = None
    label = None
    type = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        self.field_name = parsedJSON["field_name"]
        self.guid = parsedJSON["guid"]
        self.label = parsedJSON["label"]
        self.type = parsedJSON["type"]
