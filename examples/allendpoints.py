import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")

print "\n************************** Create User **************************"
user = atriumClient.createUser(identifier = "unique_id", metadata = "{\"first_name\": \"Steven\"}")
print user.guid
userGUID = user.guid

print "\n************************** Read User **************************"
user = atriumClient.readUser(userGUID)
print user.guid

print "\n************************** Update User **************************"
user = atriumClient.updateUser(userGUID, metadata = "{\"first_name\": \"Steven\", \"last_name\": \"Universe\"}")
print user.guid

print "\n************************** List Users **************************"
users = atriumClient.listUsers()
for user in users:
    print user.guid

print "\n************************** List Institutions **************************"
institutions = atriumClient.listInstitutions(name = "bank")
for institution in institutions:
    print institution.name

print "\n************************** Read Institution **************************"
institution = atriumClient.readInstitution("mxbank")
print institution.name

print "\n************************** Read Institution Credentials************************** "
credentials = atriumClient.readInstitutionCredentials("mxbank")
for credential in credentials:
    print credential.guid

print "\n************************** Create Member **************************"
# Create credential JSON object
credentialOne = {}
credentialOne["guid"] = "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1"
credentialOne["value"] = "test_atrium1"

# Create another credential JSON object
credentialTwo = {}
credentialTwo["guid"] = "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d"
credentialTwo["value"] = "challenge1"

# Create credential array from credential JSON Objects
credentialArray = []
credentialArray.append(credentialOne)
credentialArray.append(credentialTwo)

member = atriumClient.createMember(userGUID, credentialArray, "mxbank")
print member.guid
memberGUID = member.guid

print "\n************************** Read Member **************************"
member = atriumClient.readMember(userGUID, memberGUID)
print member.guid

print "\n************************** Update Member **************************"
# Create credential JSON object
credentialOne = {}
credentialOne["guid"] = "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1"
credentialOne["value"] = "test_atrium"

# Create another credential JSON object
credentialTwo = {}
credentialTwo["guid"] = "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d"
credentialTwo["value"] = "challenge"

# Create credential array from credential JSON Objects
credentialArray = []
credentialArray.append(credentialOne)
credentialArray.append(credentialTwo)

member = atriumClient.updateMember(userGUID, memberGUID, credentials = credentialArray, metadata = "{\"credentials_last_refreshed_at\": \"2015-10-16\"}")
print member.guid

print "\n************************** List Members **************************"
members = atriumClient.listMembers(userGUID)
for member in members:
    print member.guid

print "\n************************** Aggregate Member **************************"
member = atriumClient.aggregateMember(userGUID, memberGUID)
print member.status

print "\n************************** Read Member Status **************************"
member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
print member.status

print "\n************************** List Member MFA Challenges **************************"
time.sleep(3)
challenges = atriumClient.listMemberMFAChallenges(userGUID, memberGUID)
challengeGUID = None
for challenge in challenges:
    print challenge.guid
    challengeGUID = challenge.guid

print "\n************************** Resume Aggregation **************************"
# Create credential JSON object
credentialOne = {}
credentialOne["guid"] = challengeGUID
credentialOne["value"] = "correct"

# Create credential array from credential JSON Objects
credentialArray = []
credentialArray.append(credentialOne)

member = atriumClient.resumeMemberAggregation(userGUID, memberGUID, credentialArray)
print member.status

print "\n************************** List Member Credentials **************************"
credentials = atriumClient.listMemberCredentials(userGUID, memberGUID)
for credential in credentials:
    print credential.guid

print "\n************************** List Member Accounts **************************"
time.sleep(5)
accounts = atriumClient.listMemberAccounts(userGUID, memberGUID)
accountGUID = None
for account in accounts:
    print account.guid
    accountGUID = account.guid

print "\n************************** List Member Transactions **************************"
transactions = atriumClient.listMemberTransactions(userGUID, memberGUID)
for transaction in transactions:
    print transaction.guid

print "\n************************** Read Account **************************"
account = atriumClient.readAccount(userGUID, accountGUID)
print account.guid

print "\n************************** List Accounts for User **************************"
accounts = atriumClient.listAccounts(userGUID)
for account in accounts:
    print account.guid

print "\n************************** List Account Transactions **************************"
transactions = atriumClient.listAccountTransactions(userGUID, accountGUID)
transactionGUID = None
for transaction in transactions:
    print transaction.guid
    transactionGUID = transaction.guid

print "\n************************** Read a Transaction **************************"
transaction = atriumClient.readTransaction(userGUID, transactionGUID)
print transaction.guid

print "\n************************** List Transactions **************************"
transactions = atriumClient.listTransactions(userGUID)
for transaction in transactions:
    print transaction.guid

print "\n************************** Connect Widget **************************"
connect = atriumClient.createWidget(userGUID)
print connect.guid

print "\n************************** Delete Member **************************"
response = atriumClient.deleteMember(userGUID, memberGUID)
print response

print "\n************************** Delete User **************************"
response = atriumClient.deleteUser(userGUID)
print response
