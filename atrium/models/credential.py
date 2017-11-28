import json

class Credential:
    field_name = None
    guid = None
    label = None
    type = None

    def __init__(self, response):
        self.field_name = response["field_name"]
        self.guid = response["guid"]
        self.label = response["label"]
        self.type = response["type"]
