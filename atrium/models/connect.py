import json

class Connect:
    connect_widget_url = None
    guid = None

    def __init__(self, response):
        self.connect_widget_url = response["connect_widget_url"]
        self.guid = response["guid"]
