class AccountNumber:
    account_guid = None
    account_number = None
    guid = None
    member_guid = None
    routing_number = None
    user_guid = None

    def __init__(self, response):
        self.account_guid = response["account_guid"]
        self.account_number = response["account_number"]
        self.guid = response["guid"]
        self.member_guid = response["member_guid"]
        self.routing_number = response["routing_number"]
        self.user_guid = response["user_guid"]
