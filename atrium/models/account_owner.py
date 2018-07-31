class AccountOwner:
    address = None
    account_guid = None
    city = None
    country = None
    email = None
    guid = None
    member_guid = None
    owner_name = None
    phone = None
    postal_code = None
    state = None
    user_guid = None

    def __init__(self, response):
        self.address = response["address"]
        self.account_guid = response["account_guid"]
        self.city = response["city"]
        self.country = response["country"]
        self.email = response["email"]
        self.guid = response["guid"]
        self.member_guid = response["member_guid"]
        self.owner_name = response["owner_name"]
        self.phone = response["phone"]
        self.postal_code = response["postal_code"]
        self.state = response["state"]
        self.user_guid = response["user_guid"]
