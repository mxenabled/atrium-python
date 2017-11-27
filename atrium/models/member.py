import json

class Member:
    aggregated_at = None
    guid = None
    identifier = None
    institution_code = None
    metadata = None
    name = None
    status = None
    successfully_aggregated_at = None
    user_guid = None
    challenges = None
    has_processed_accounts = None
    has_processed_transactions = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        if "aggregated_at" in parsedJSON:
            self.aggregated_at = parsedJSON["aggregated_at"]
        if "guid" in parsedJSON:
            self.guid = parsedJSON["guid"]
        if "identifier" in parsedJSON:
            self.identifier = parsedJSON["identifier"]
        if "institution_code" in parsedJSON:
            self.institution_code = parsedJSON["institution_code"]
        if "metadata" in parsedJSON:
            self.metadata = parsedJSON["metadata"]
        if "name" in parsedJSON:
            self.name = parsedJSON["name"]
        if "status" in parsedJSON:
            self.status = parsedJSON["status"]
        if "successfully_aggregated_at" in parsedJSON:
            self.successfully_aggregated_at = parsedJSON["successfully_aggregated_at"]
        if "user_guid" in parsedJSON:
            self.user_guid = parsedJSON["user_guid"]
        if "challenges" in parsedJSON:
            self.challenges = parsedJSON["challenges"]
        if "has_processed_accounts" in parsedJSON:
            self.has_processed_accounts = parsedJSON["has_processed_accounts"]
        if "has_processed_transactions" in parsedJSON:
            self.has_processed_transactions = parsedJSON["has_processed_transactions"]
