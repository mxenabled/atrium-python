import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")

transactions = {
    "transactions": [
        {
            "amount": 11.22,
            "description": "BEER BAR 65000000764SALT LAKE C",
            "id": "12",
            "type": "DEBIT"
        },
        {
            "amount": 21.33,
            "description": "IN-N-OUT BURGER #239AMERICAN FO",
            "id": "13",
            "type": "DEBIT"
        },
        {
            "amount": 1595.33,
            "description": "ONLINE PAYMENT - THANK YOU",
            "id": "14",
            "type": "CREDIT"
        }
    ]
}

categorized_transactions = atriumClient.categorizeAndDescribeTransactions(transactions)
print(categorized_transactions.__dict__)
