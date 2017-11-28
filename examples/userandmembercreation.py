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
print("Created member: " + member.guid)


print("\n* Deleting test user *")
atriumClient.deleteUser(userGUID)
print("Deleted user: " + userGUID)
