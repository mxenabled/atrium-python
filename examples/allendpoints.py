import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")

print "\n************************** Create User **************************"
user = atriumClient.createUser(identifier = "unique_id", metadata = "{\"first_name\": \"Steven\"}")
print user.__dict__
print json.dumps(user.__dict__)
userGUID = user.guid

print "\n************************** Read User **************************"
user = atriumClient.readUser(userGUID)
print user.__dict__

print "\n************************** Update User **************************"
user = atriumClient.updateUser(userGUID, metadata = "{\"first_name\": \"Steven\", \"last_name\": \"Universe\"}")
print user.__dict__

print "\n************************** List Users **************************"
users = atriumClient.listUsers()
print users
for user in users:
    print user.__dict__

print "\n************************** List Institutions **************************"
institutions = atriumClient.listInstitutions(name = "bank")
for institution in institutions:
    print institution.__dict__

print "\n************************** Read Institution **************************"
institution = atriumClient.readInstitution("mxbank")
print institution.__dict__

print "\n************************** Read Institution Credentials************************** "
credentials = atriumClient.readInstitutionCredentials("mxbank")
for credential in credentials:
    print credential.__dict__

print "\n************************** Create Member **************************"
credentials = [
    {
        "guid": "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1",
        "value": "test_atrium1"
    },
    {
        "guid": "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d",
        "value": "challenge1"
    }
]

member = atriumClient.createMember(userGUID, credentials, "mxbank")
print member.__dict__
memberGUID = member.guid

print "\n************************** Read Member **************************"
member = atriumClient.readMember(userGUID, memberGUID)
print member.__dict__

print "\n************************** Update Member **************************"
credentials = [
    {
        "guid": "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1",
        "value": "test_atrium"
    },
    {
        "guid": "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d",
        "value": "challenge"
    }
]

member = atriumClient.updateMember(userGUID, memberGUID, credentials = credentials, metadata = "{\"credentials_last_refreshed_at\": \"2015-10-16\"}")
print member.__dict__

print "\n************************** List Members **************************"
members = atriumClient.listMembers(userGUID)
for member in members:
    print member.__dict__

print "\n************************** Aggregate Member **************************"
member = atriumClient.aggregateMember(userGUID, memberGUID)
print member.__dict__

print "\n************************** Read Member Status **************************"
member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
print member.__dict__

print "\n************************** List Member MFA Challenges **************************"
time.sleep(3)
challenges = atriumClient.listMemberMFAChallenges(userGUID, memberGUID)
challengeGUID = None
for challenge in challenges:
    print challenge.__dict__
    challengeGUID = challenge.guid

print "\n************************** Resume Aggregation **************************"
credentials = [
    {
        "guid": challengeGUID,
        "value": "correct"
    }
]

member = atriumClient.resumeMemberAggregation(userGUID, memberGUID, credentials)
print member.__dict__

print "\n************************** List Member Credentials **************************"
credentials = atriumClient.listMemberCredentials(userGUID, memberGUID)
for credential in credentials:
    print credential.__dict__

print "\n************************** List Member Accounts **************************"
time.sleep(5)
accounts = atriumClient.listMemberAccounts(userGUID, memberGUID)
accountGUID = None
for account in accounts:
    print account.__dict__
    accountGUID = account.guid

print "\n************************** List Member Transactions **************************"
transactions = atriumClient.listMemberTransactions(userGUID, memberGUID)
for transaction in transactions:
    print transaction.__dict__

print "\n************************** Read Account **************************"
account = atriumClient.readAccount(userGUID, accountGUID)
print account.__dict__

print "\n************************** List Accounts for User **************************"
accounts = atriumClient.listAccounts(userGUID)
for account in accounts:
    print account.__dict__

print "\n************************** List Account Transactions **************************"
transactions = atriumClient.listAccountTransactions(userGUID, accountGUID)
transactionGUID = None
for transaction in transactions:
    print transaction.__dict__
    transactionGUID = transaction.guid

print "\n************************** Read a Transaction **************************"
transaction = atriumClient.readTransaction(userGUID, transactionGUID)
print transaction.__dict__

print "\n************************** List Transactions **************************"
transactions = atriumClient.listTransactions(userGUID)
for transaction in transactions:
    print transaction.__dict__

print "\n************************** Connect Widget **************************"
connect = atriumClient.createWidget(userGUID)
print connect.__dict__

print "\n************************** Delete Member **************************"
response = atriumClient.deleteMember(userGUID, memberGUID)
print response

print "\n************************** Delete User **************************"
response = atriumClient.deleteUser(userGUID)
print response
