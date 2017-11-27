import sys
import json
import time
import datetime
sys.path.append("..")

from atrium import AtriumClient

def checkJobStatus(atriumClient, counter, userGUID, memberGUID):
    print("\n2 second delay...")
    time.sleep(2)

    member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
    status = member.status

    print("\nJOB STATUS: " + status)

    if status == "COMPLETED":
        readAggregationData(atriumClient, userGUID, memberGUID)
    elif status == "HALTED" or status == "FAILED":
        currentTime = datetime.datetime.now().isoformat()[:19] + "+00:00"

        member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
        lastSuccessTime = member.successfully_aggregated_at

        # Check if last successful aggregation over 3 days aggregation
        if lastSuccessTime != None and (abs(currentTime[8:10] - lastSuccessTime[8:10]) > 3 or abs(currentTime[5:7] - lastSuccessTime[5:7]) > 0 or abs(currentTime[0:4] - lastSuccessTime[0:4]) > 0):
            print("\nClient should contact MX Support to resolve issue.")
        else:
            print("\nAn update is currently unavailable. Please try again tomorrow")
    elif status == "CREATED" or status == "UPDATED" or status == "RESUMED" or status == "CONNECTED" or status == "DEGRADED" or status == "DELAYED" or status == "INITIATED" or status == "REQUESTED" or status == "AUTHENTICATED" or status == "RECEIVED" or status == "TRANSFERRED":
        checkJobStatus(atriumClient, counter, userGUID, memberGUID)
    elif status == "PREVENTED" or status == "DENIED" or status == "IMPAIRED":
        member = atriumClient.readMember(userGUID, memberGUID)
        institutionCode = member.institution_code

        print("\nPlease update credentials")
        credentials = atriumClient.readInstitutionCredentials(institutionCode)
        updatedCredentials = []
        for credential in credentials:
            print("\nPlease enter in " + credential.label + ":")
            cred = sys.stdin.readline().strip()
            credPair = {}
            credPair["guid"] = credential.guid
            credPair["value"] = cred
            updatedCredentials.append(credPair)

        atriumClient.updateMember(userGUID, memberGUID, credentials = updatedCredentials)

        checkJobStatus(atriumClient, counter, userGUID, memberGUID)
    elif status == "CHALLENGED":
        print ("\nPlease answer the following challenges:")
        challenges = atriumClient.listMemberMFAChallenges(userGUID, memberGUID)
        updatedChallenges = []
        for challenge in challenges:
            print(challenge.label + ":")
            ans = sys.stdin.readline().strip()
            credPair = {}
            credPair["guid"] = challenge.guid
            credPair["value"] = ans
            updatedChallenges.append(credPair)

        atriumClient.resumeMemberAggregation(userGUID, memberGUID, updatedChallenges)

        checkJobStatus(atriumClient, counter, userGUID, memberGUID)
    elif status == "REJECTED":
        atriumClient.aggregateMember(userGUID, memberGUID)

        checkJobStatus(atriumClient, counter, userGUID, memberGUID)
    elif status == "EXPIRED":
        print("\nUser did not answer MFA in time. Please try again tomorrow.")
    elif status == "LOCKED":
        print("\nUser's account is locked at FI")
    elif status == "IMPEDED":
        print("\nUser's attention is required at FI website in order for aggregation to complete")
    elif status == "DISCONTINUED":
        print("\nConnection to institution is no longer available.")
    elif status == "CLOSED" or status == "DISABLED":
        print("\nAggregation is purposely turned off for this user.")
    elif status == "TERMINATED" or status == "ABORTED" or status == "STOPPED" or status == "THROTTLED" or status == "SUSPENDED" or status == "ERRORED":
        # Check JobStatus() an additional 2 times to see if status changed
        if counter < 3:
            counter = counter + 1
            checkJobStatus(atriumClient, counter, userGUID, memberGUID)
        else:
            print("\nAn update is currently unavailable. Please try again tomorrow and contact support if unsuccessful after 3 days.")
    else:
        print(status)

def readAggregationData(atriumClient, userGUID, memberGUID):
    atriumClient.readMember(userGUID, memberGUID)

    print("\n* Listing all member accounts and transactions *")
    accounts = atriumClient.listMemberAccounts(userGUID, memberGUID)
    for account in accounts:
        print("Type: " + account.type + "\tName: " + account.name + "\tAvailable Balance: " + str(
            account.available_balance) + "\tAvailable Credit: " + str(account.available_credit))
        print("Transactions")
        transactions = atriumClient.listAccountTransactions(userGUID, account.guid)
        for transaction in transactions:
            print("\tDate: " + transaction.date + "\tDescription: " + transaction.description + "\tAmount: " + str(
                transaction.amount))
        print("\n")


atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")
counter = 0

print("Please enter in user GUID. If not yet created just press enter key: ")
userGUID = sys.stdin.readline().strip()

print("\nPlease enter in member GUID. If not yet created just press enter key: ")
memberGUID = sys.stdin.readline().strip()

print("\nPlease enter in if end user is present (true or false): ")
endUserPresent = sys.stdin.readline().strip()

if userGUID == "" and memberGUID != "":
    print("\nMust include user GUID when member GUID is entered.")
    sys.exit(0)

if userGUID == "" and endUserPresent == "true":
    print("\n* Creating user *")

    print("\nPlease enter in an unique id for new user: ")
    identifier = sys.stdin.readline().strip()

    user = atriumClient.createUser(identifier = identifier)
    userGUID = user.guid

    print("\nCreated user: " + userGUID)

if memberGUID != "" and endUserPresent == "true":
    atriumClient.aggregateMember(userGUID, memberGUID)
    checkJobStatus(atriumClient, counter, userGUID, memberGUID)
elif memberGUID != "":
    readAggregationData(atriumClient, userGUID, memberGUID)
elif endUserPresent == "true":
    print ("\n* Creating member *")

    print ("\n* Listing top 15 institutions *")
    institutions = atriumClient.listInstitutions()
    for institution in institutions:
        print(institution.name + " : institution code = " + institution.code)

    print("\nPlease enter in desired institution code: ")
    institutionCode = sys.stdin.readline().strip()

    credentials = atriumClient.readInstitutionCredentials(institutionCode)
    updatedCredentials = []
    for credential in credentials:
        print("\nPlease enter in " + credential.label + ":")
        cred = sys.stdin.readline().strip()
        credPair = {}
        credPair["guid"] = credential.guid
        credPair["value"] = cred
        updatedCredentials.append(credPair)

    member = atriumClient.createMember(userGUID, updatedCredentials, institutionCode)
    memberGUID = member.guid

    print("\nCreated member: " + memberGUID)

    checkJobStatus(atriumClient, counter, userGUID, memberGUID)
else:
    print("\nEnd user must be present to create a new member")
    sys.exit(0)

print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
