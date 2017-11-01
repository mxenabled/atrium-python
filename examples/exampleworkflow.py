import sys
import json
import time
import datetime

from atriumclient import AtriumClient

def checkJobStatus(atriumClient, userGUID, memberGUID):
    print("\n2 second delay...")
    time.sleep(2)

    aggregationResponse = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)

    parsedJSON = json.loads(aggregationResponse)
    code = parsedJSON["member"]["status"]

    print("\nJOB STATUS: " + code)

    if code == "COMPLETED":
        readAggregationData(atriumClient, userGUID, memberGUID)
    elif code == "HALTED" or code == "FAILED":
        currentTime = datetime.datetime.now().isoformat()[:19] + "+00:00"

        statusResponse = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
        parsedJSON = json.loads(statusResponse)
        lastSuccessTime = parsedJSON["member"]["successfully_aggregated_at"]

        # Check if last successful aggregation over 3 days aggregation
        if not lastSuccessTime == None and (abs(currentTime[8:10] - lastSuccessTime[8:10]) > 3 or abs(currentTime[5:7] - lastSuccessTime[5:7]) > 0 or abs(currentTime[0:4] - lastSuccessTime[0:4]) > 0):
            print("\nClient should contact MX Support to resolve issue.")
        else:
            print("\nAn update is currently unavailable. Please try again tomorrow")
    elif code == "CREATED" or code == "UPDATED" or code == "RESUMED" or code == "CONNECTED" or code == "DEGRADED" or code == "DELAYED" or code == "INITIATED" or code == "REQUESTED" or code == "AUTHENTICATED" or code == "RECEIVED" or code == "TRANSFERRED":
        checkJobStatus(atriumClient, userGUID, memberGUID)
    elif code == "PREVENTED" or code == "DENIED" or code == "IMPAIRED":
        readMemberData = atriumClient.readMember(userGUID, memberGUID)
        parsedJSON = json.loads(readMemberData)
        institutionCode = parsedJSON["member"]["institution_code"]

        print("\nPlease update credentials")
        requiredCredentials = atriumClient.readInstitutionCredentials(institutionCode, "", "")
        parsedJSON = json.loads(requiredCredentials)
        JSONArray = parsedJSON["credentials"]
        credentials = []
        for credential in JSONArray:
            print("\nPlease enter in " + credential["label"] + ":")
            cred = sys.stdin.readline().strip()
            credPair = {}
            credPair["guid"] = credential["guid"]
            credPair["value"] = cred
            credentials.append(credPair)

        atriumClient.updateMember(userGUID, memberGUID, credentials, "", "")

        checkJobStatus(atriumClient, userGUID, memberGUID)
    elif code == "CHALLENGED":
        print ("\nPlease answer the following challenges:")
        challengeResponse = atriumClient.listMemberMFAChallenges(userGUID, memberGUID, "", "")
        parsedJSON = json.loads(challengeResponse)
        JSONArray = parsedJSON["challenges"]
        challenges = []
        for challenge in JSONArray:
            print(challenge["label"] + ":")
            ans = sys.stdin.readline().strip()
            credPair = {}
            credPair["guid"] = challenge["guid"]
            credPair["value"] = ans
            challenges.append(credPair)
        inner = {}
        inner["challenges"] = challenges
        outer = {}
        outer["member"] = inner
        answer = json.dumps(outer)

        atriumClient.resumeMemberAggregation(userGUID, memberGUID, answer)

        checkJobStatus(atriumClient, userGUID, memberGUID)
    elif code == "REJECTED":
        atriumClient.aggregateMember(userGUID, memberGUID)

        checkJobStatus(atriumClient, userGUID, memberGUID)
    elif code == "EXPIRED":
        print("\nUser did not answer MFA in time. Please try again tomorrow.")
    elif code == "LOCKED":
        print("\nUser's account is locked at FI")
    elif code == "IMPEDED":
        print("\nUser's attention is required at FI website in order for aggregation to complete")
    elif code == "DISCONTINUED":
        print("\nConnection to institution is no longer available.")
    elif code == "CLOSED" or code == "DISABLED":
        print("\nAggregation is purposely turned off for this user.")
    elif code == "TERMINATED" or code == "ABORTED" or code == "STOPPED" or code == "THROTTLED" or code == "SUSPENDED" or code == "ERRORED":
        # Check JobStatus() an additional 2 times to see if status changed
        if counter < 3:
            counter = counter + 1
            checkJobStatus(atriumClient, userGUID, memberGUID)
        else:
            print("\nAn update is currently unavailable. Please try again tomorrow and contact support if unsuccessful after 3 days.")
            counter = 0
    else:
        print(code)

def readAggregationData(atriumClient, userGUID, memberGUID):
    atriumClient.readMember(userGUID, memberGUID)

    print("\n* Listing All Member Accounts *")
    accountsResponse = atriumClient.listMemberAccounts(userGUID, memberGUID, "", "")
    parsedJSON = json.loads(accountsResponse)
    JSONArray = parsedJSON["accounts"]
    for item in JSONArray:
        print("Type: " + str(item["type"]) + "\tName: " + str(item["name"]) + "\tAvailable Balance: " + str(item["available_balance"]) + "\tAvailable Credit: " + str(item["available_credit"]))

    print("\n* Listing All Member Transactions *")
    transactionsResponse = atriumClient.listMemberTransactions(userGUID, memberGUID, "", "", "", "")
    parsedJSON = json.loads(transactionsResponse)
    JSONArray = parsedJSON["transactions"]
    for item in JSONArray:
        print("Date: " + str(item["date"]) + "\tDescription: " + str(item["description"]) + "\tAmount: " + str(item["amount"]))


# Main #
counter = 0


if len(sys.argv) < 4 or len(sys.argv) > 4:
    print("\nIncorrect usage. Correct usage is: python ExampleWorkflow.py YOUR_DESIRED_ENVIRONMENT YOUR_MX_API_KEY YOUR_MX_CLIENT_ID")
    sys.exit(0)

atriumClient = AtriumClient(sys.argv[1], sys.argv[2], sys.argv[3])

userGUID = ""
memberGUID = ""
endUserPresent = ""

print("Please enter in user GUID. If not yet created just press enter key: ")
userGUID = sys.stdin.readline().strip()

print("\nPlease enter in member GUID. If not yet created just press enter key: ")
memberGUID = sys.stdin.readline().strip()

print("\nPlease enter in if end user is present (true or false): ")
endUserPresent = sys.stdin.readline().strip()


if userGUID == "" and not memberGUID == "":
    print("\nMust include user GUID when member GUID is entered.")
    sys.exit(0)

if userGUID == "" and endUserPresent == "true":
    print("\n* NEW USER CREATION *")

    print("\nPlease enter in an unique id: ")
    identifier = sys.stdin.readline().strip()

    userResponse = atriumClient.createUser(identifier, "", "")
    parsedJSON = json.loads(userResponse)
    userGUID = parsedJSON["user"]["guid"]

if not memberGUID == "" and endUserPresent == "true":
    atriumClient.aggregateMember(userGUID, memberGUID)
    checkJobStatus(atriumClient, userGUID, memberGUID)
elif not memberGUID == "":
    readAggregationData(atriumClient, userGUID, memberGUID)
elif endUserPresent == "true":
    print ("\n* NEW MEMBER CREATION *")

    print("Please enter in a keyword to search for an institution: ")
    institution = sys.stdin.readline().strip()
    institutions = atriumClient.listInstitutions(institution, "", "")

    parsedJSON = json.loads(institutions)
    JSONArray = parsedJSON["institutions"]
    for item in JSONArray:
        print(item["name"] + " : institution code = " + item["code"])

    print("\nPlease enter in desired institution code: ")
    institutionCode = sys.stdin.readline().strip()

    requiredCredentials = atriumClient.readInstitutionCredentials(institutionCode, "", "")
    parsedJSON = json.loads(requiredCredentials)
    JSONArray = parsedJSON["credentials"]
    credentials = []
    for credential in JSONArray:
        print("\nPlease enter in " + credential["label"] + ":")
        cred = sys.stdin.readline().strip()
        credPair = {}
        credPair["guid"] = credential["guid"]
        credPair["value"] = cred
        credentials.append(credPair)

    memberResponse = atriumClient.createMember(userGUID, credentials, institutionCode, "", "")

    parsedJSON = json.loads(memberResponse)
    memberGUID = parsedJSON["member"]["guid"]
    checkJobStatus(atriumClient, userGUID, memberGUID)
else:
    print("\nEnd user must be present to create a new member")
    sys.exit(0)
