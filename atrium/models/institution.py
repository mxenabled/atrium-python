import json

class Institution:
    code = None
    name = None
    url = None
    small_logo_url = None
    medium_logo_url = None

    def __init__(self, response):
        self.code = response["code"]
        self.name = response["name"]
        self.url = response["url"]
        self.small_logo_url = response["small_logo_url"]
        self.medium_logo_url = response["medium_logo_url"]
