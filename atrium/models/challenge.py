import json

class Challenge:
    field_name = None
    guid = None
    label = None
    type = None
    image_data = None
    options = None

    def __init__(self, response):
        self.field_name = response["field_name"]
        self.guid = response["guid"]
        self.label = response["label"]
        self.type = response["type"]
        if "image_data" in response:
            self.image_data = response["image_data"]
        if "options" in response:
            self.options = response["options"]
