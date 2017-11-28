import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")

print("\n* Creating test user and member *")
user = atriumClient.createUser()
userGUID = user.guid
print("Created user: " + userGUID)

credentials = [
    {
        "guid": "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1",
        "value": "test_atrium"
    },
    {
        "guid": "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d",
        "value": "password"
    }
]

member = atriumClient.createMember(userGUID, credentials, "mxbank")

memberGUID = member.guid
print("Created member: " + memberGUID)

time.sleep(1)


print("\n* Aggregating member *")
member = atriumClient.aggregateMember(userGUID, memberGUID)

time.sleep(10)
print("Member aggregation status: " + member.status)


print("\n* Listing all member accounts and transactions *")
accounts = atriumClient.listMemberAccounts(userGUID, memberGUID)
for account in accounts:
    print("Type: " + account.type + "\tName: " + account.name + "\tAvailable Balance: " + str(account.available_balance) + "\tAvailable Credit: " + str(account.available_credit))
    print("Transactions")
    transactions = atriumClient.listAccountTransactions(userGUID, account.guid)
    for transaction in transactions:
        print("\tDate: " + transaction.date + "\tDescription: " + transaction.description + "\tAmount: " + str(transaction.amount))
    print("\n")


print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
