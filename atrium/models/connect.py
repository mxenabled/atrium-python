import json

class Connect:
    connect_widget_url = None
    guid = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        self.connect_widget_url = parsedJSON["connect_widget_url"]
        self.guid = parsedJSON["guid"]
