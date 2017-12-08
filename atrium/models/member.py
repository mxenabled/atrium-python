import json

class Member:
    aggregated_at = None
    guid = None
    identifier = None
    institution_code = None
    is_being_aggregated = None
    metadata = None
    name = None
    status = None
    successfully_aggregated_at = None
    user_guid = None
    challenges = None
    has_processed_accounts = None
    has_processed_transactions = None

    def __init__(self, response):
        if "aggregated_at" in response:
            self.aggregated_at = response["aggregated_at"]
        if "guid" in response:
            self.guid = response["guid"]
        if "identifier" in response:
            self.identifier = response["identifier"]
        if "institution_code" in response:
            self.institution_code = response["institution_code"]
        if "is_being_aggregated" in response:
            self.is_being_aggregated = response["is_being_aggregated"]
        if "metadata" in response:
            self.metadata = response["metadata"]
        if "name" in response:
            self.name = response["name"]
        if "status" in response:
            self.status = response["status"]
        if "successfully_aggregated_at" in response:
            self.successfully_aggregated_at = response["successfully_aggregated_at"]
        if "user_guid" in response:
            self.user_guid = response["user_guid"]
        if "challenges" in response:
            self.challenges = response["challenges"]
        if "has_processed_accounts" in response:
            self.has_processed_accounts = response["has_processed_accounts"]
        if "has_processed_transactions" in response:
            self.has_processed_transactions = response["has_processed_transactions"]
