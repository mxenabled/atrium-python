import json
import sys
sys.path.append("..")

from atrium import AtriumClient

atriumClient = AtriumClient("vestibule.mx.com", "YOUR_MX_API_KEY", "YOUR_MX_CLIENT_ID")


print "\n* Creating user *"

user = atriumClient.createUser()
userGUID = user.guid
print("Created user: " + user.guid)


print "\n* Listing institutions with query string \"bank\" *"

institutions = atriumClient.listInstitutions(name = "bank")
for institution in institutions:
    print(institution.name + " : institution code = " + institution.code)


print "\n* Reading institution \"mxbank\" *"
institution = atriumClient.readInstitution("mxbank")
print(institution.name)


print "\n* Reading institution credentials \"mxbank\" *"
credentials = atriumClient.readInstitutionCredentials("mxbank")
for credential in credentials:
    print(credential.guid)


print "\n* Creating member *"

# Create credential JSON object
credentialOne = {}
credentialOne["guid"] = "CRD-9f61fb4c-912c-bd1e-b175-ccc7f0275cc1"
credentialOne["value"] = "test_atrium"

# Create another credential JSON object
credentialTwo = {}
credentialTwo["guid"] = "CRD-e3d7ea81-aac7-05e9-fbdd-4b493c6e474d"
credentialTwo["value"] = "password"

# Create credential array from credential JSON Objects
credentialArray = []
credentialArray.append(credentialOne)
credentialArray.append(credentialTwo)

member = atriumClient.createMember(userGUID, credentialArray, "mxbank")
print("Created member: " + member.guid)


print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
