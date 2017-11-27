import json

class Account:
    apr = None
    apy = None
    available_balance = None
    available_credit = None
    balance = None
    created_at = None
    credit_limit = None
    day_payment_is_due = None
    guid = None
    institution_code = None
    interest_rate = None
    is_closed = None
    last_payment = None
    last_payment_at = None
    matures_on = None
    member_guid = None
    minimum_balance = None
    minimum_payment = None
    name = None
    original_balance = None
    payment_due_at = None
    payoff_balance = None
    started_on = None
    subtype = None
    total_account_value = None
    type = None
    updated_at = None
    user_guid = None

    def __init__(self, response):
        parsedJSON = json.loads(response)
        self.apr = parsedJSON["apr"]
        self.apy = parsedJSON["apy"]
        self.available_balance = parsedJSON["available_balance"]
        self.available_credit = parsedJSON["available_credit"]
        self.balance = parsedJSON["balance"]
        self.created_at = parsedJSON["created_at"]
        self.credit_limit = parsedJSON["credit_limit"]
        self.day_payment_is_due = parsedJSON["day_payment_is_due"]
        self.guid = parsedJSON["guid"]
        self.institution_code = parsedJSON["institution_code"]
        self.interest_rate = parsedJSON["interest_rate"]
        self.is_closed = parsedJSON["is_closed"]
        self.last_payment = parsedJSON["last_payment"]
        self.last_payment_at = parsedJSON["last_payment_at"]
        self.matures_on = parsedJSON["matures_on"]
        self.member_guid = parsedJSON["member_guid"]
        self.minimum_balance = parsedJSON["minimum_balance"]
        self.minimum_payment = parsedJSON["minimum_payment"]
        self.name = parsedJSON["name"]
        self.original_balance = parsedJSON["original_balance"]
        self.payment_due_at = parsedJSON["payment_due_at"]
        self.payoff_balance = parsedJSON["payoff_balance"]
        self.started_on = parsedJSON["started_on"]
        self.subtype = parsedJSON["subtype"]
        self.total_account_value = parsedJSON["total_account_value"]
        self.type = parsedJSON["type"]
        self.updated_at = parsedJSON["updated_at"]
        self.user_guid = parsedJSON["user_guid"]