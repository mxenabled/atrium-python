import json

class User:
    guid = None
    identifier = None
    is_disabled = None
    metadata = None

    def __init__(self, response):
        self.guid = response["guid"]
        self.identifier = response["identifier"]
        self.is_disabled = response["is_disabled"]
        self.metadata = response["metadata"]
