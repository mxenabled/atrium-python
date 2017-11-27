import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")


print("\n* Creating test user and member with \"CHALLENGED\" aggregation status *")
user = atriumClient.createUser()
userGUID = user.guid
print("Created user: " + userGUID)

credentialOne = {}
credentialOne["guid"] = "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1"
credentialOne["value"] = "test_atrium"

credentialTwo = {}
credentialTwo["guid"] = "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d"
credentialTwo["value"] = "challenge"

credentialArray = []
credentialArray.append(credentialOne)
credentialArray.append(credentialTwo)

member = atriumClient.createMember(userGUID, credentialArray, "mxbank")

memberGUID = member.guid
print("Created member: " + memberGUID)

time.sleep(1)


print("\n* Retrieving member aggregation status *")
member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
print("Member aggregation status: " + member.status)


print("\n* MFA challenge *")
challenges = atriumClient.listMemberMFAChallenges(userGUID, memberGUID)
for challenge in challenges:
    print challenge.label

credential = {}
credential["guid"] = challenges[0].guid
credential["value"] = "correct"
responses = []
responses.append(credential)


print("\n* MFA answered correctly, resuming aggregation *")
atriumClient.resumeMemberAggregation(userGUID, memberGUID, responses)

time.sleep(1)


print("\n* Retrieving member aggregation status *")
member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
print("Member aggregation status: " + member.status)


print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
