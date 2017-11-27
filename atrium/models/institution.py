import json

class Institution:
    code = None
    name = None
    url = None
    small_logo_url = None
    medium_logo_url = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        self.code = parsedJSON["code"]
        self.name = parsedJSON["name"]
        self.url = parsedJSON["url"]
        self.small_logo_url = parsedJSON["small_logo_url"]
        self.medium_logo_url = parsedJSON["medium_logo_url"]
