import json
import time
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")


print("\n* Creating user and member with \"DENIED\" aggregation status *")
user = atriumClient.createUser()
userGUID = user.guid
print("Created user: " + userGUID)

credentialOne = {}
credentialOne["guid"] = "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1"
credentialOne["value"] = "test_atrium"

credentialTwo = {}
credentialTwo["guid"] = "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d"
credentialTwo["value"] = "INVALID"

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


member = atriumClient.readMember(userGUID, memberGUID)
institutionCode = member.institution_code

print("\n* Updating credentials *")
credentials = atriumClient.readInstitutionCredentials(institutionCode)
updatedCredentials = []

usernameCredential = {}
usernameCredential["guid"] = credentials[0].guid
usernameCredential["value"] = "test_atrium"
updatedCredentials.append(usernameCredential)

passwordCredential = {}
passwordCredential["guid"] = credentials[1].guid
passwordCredential["value"] = "password"
updatedCredentials.append(passwordCredential)

atriumClient.updateMember(userGUID, memberGUID, updatedCredentials)


time.sleep(1)

print("\n* Retrieving member aggregation status *")
member = atriumClient.readMemberAggregationStatus(userGUID, memberGUID)
print("Member aggregation status: " + member.status)


print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
