from httplib import HTTPSConnection
import json
import sys

from models import *

class AtriumClient:
    environment = ""
    mxAPIKEY = ""
    mxCLIENTID = ""

    # Required Parameters: environment, mxAPIKEY, mxCLIENTID
    # Optional Parameters: None
    def __init__(self, environment, mxAPIKEY, mxCLIENTID):
        self.environment = environment
        self.mxAPIKEY = mxAPIKEY
        self.mxCLIENTID = mxCLIENTID


    # USER

    # Required Parameters: None
    # Optional Parameters: identifier, is_disabled, metadata
    def createUser(self, identifier = "", is_disabled = "", metadata = ""):
        inner = {}
        if identifier != "":
            inner["identifier"] = identifier
        is_disabled = is_disabled.lower()
        if is_disabled == "" or is_disabled == "false":
            inner["is_disabled"] = "false"
        else:
            inner["is_disabled"] = "true"
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["user"] = inner

        response = self.makeRequest("POST", "/users", outer)
        return User(json.loads(response)["user"])

    # Required Parameters: userGUID
    # Optional Parameters: None
    def readUser(self, userGUID):
        response = self.makeRequest("GET", "/users/{0}".format(userGUID), "")
        return User(json.loads(response)["user"])

    # Required Parameters: userGuid
    # Optional Parameters: identifier, is_disabled, metadata
    def updateUser(self, userGUID, identifier = "", is_disabled = "", metadata = ""):
        inner = {}
        if identifier != "":
            inner["identifier"] = identifier
        if is_disabled != "":
            inner["is_disabled"] = is_disabled
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["user"] = inner

        response = self.makeRequest("PUT", "/users/{0}".format(userGUID), outer)
        return User(json.loads(response)["user"])

    # Required Parameters: None
    # Optional Parameters: page, records_per_page
    def listUsers(self, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users{0}".format(params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["users"]
        users = []
        for user in JSONArray:
            users.append(User(user))
        return users

    # Required Parameters: userGUID
    # Optional Parameters: None
    def deleteUser(self, userGUID):
        return self.makeRequest("DELETE", "/users/{0}".format(userGUID), "")


    # INSTITUTION

    # Required Parameters: None
    # Optional Parameters: name, page, records_per_page
    def listInstitutions(self, name = "", page = "", records_per_page = ""):
        params = self.optionalParameters(name, "", "", page, records_per_page)

        response =  self.makeRequest("GET", "/institutions{0}".format(params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["institutions"]
        institutions = []
        for institution in JSONArray:
            institutions.append(Institution(institution))
        return institutions

    # Required Parameters: institutionCode
    # Optional Parameters: None
    def readInstitution(self, institutionCode):
        response = self.makeRequest("GET", "/institutions/{0}".format(institutionCode), "")
        return Institution(json.loads(response)["institution"])

    # Required Parameters: institutionCode
    # Optional Parameters: page, records_per_page
    def readInstitutionCredentials(self, institutionCode, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response =  self.makeRequest("GET", "/institutions/{0}/credentials{1}".format(institutionCode, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["credentials"]
        credentials = []
        for credential in JSONArray:
            credentials.append(Credential(credential))
        return credentials


    # MEMBER

    # Required Parameters: userGUID, credentials, institutionCode
    # Optional Parameters: identifier, metadata
    def createMember(self, userGUID, credentials, institutionCode, identifier = "", metadata = ""):
        inner = {}
        inner["institution_code"] = institutionCode
        inner["credentials"] = credentials
        if identifier != "":
            inner["identifier"] = identifier
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["member"] = inner

        response = self.makeRequest("POST", "/users/{0}/members".format(userGUID), outer)
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def readMember(self, userGUID, memberGUID):
        response = self.makeRequest("GET", "/users/{0}/members/{1}".format(userGUID, memberGUID), "")
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: credentials, identifier, metadata
    def updateMember(self, userGUID, memberGUID, credentials = "", identifier = "", metadata = ""):
        inner = {}
        if credentials != "":
            inner["credentials"] = credentials
        if identifier != "":
            inner["identifier"] = identifier
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["member"] = inner

        response = self.makeRequest("PUT", "/users/{0}/members/{1}".format(userGUID, memberGUID), outer)
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def deleteMember(self, userGUID, memberGUID):
        return self.makeRequest("DELETE", "/users/{0}/members/{1}".format(userGUID, memberGUID), "")

    # Required Parameters: userGUID
    # Optional Parameters: page, records_per_page
    def listMembers(self, userGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members{1}".format(userGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["members"]
        members = []
        for member in JSONArray:
            members.append(Member(member))
        return members

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def aggregateMember(self, userGUID, memberGUID):
        response = self.makeRequest("POST", "/users/{0}/members/{1}/aggregate".format(userGUID, memberGUID), "")
        return Member(json.loads(response)["member"])

    # Required Parameters:  userGUID, memberGUID
    # Optional Parameters: None
    def readMemberAggregationStatus(self, userGUID, memberGUID):
        response = self.makeRequest("GET", "/users/{0}/members/{1}/status".format(userGUID, memberGUID), "")
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: page, records_per_page
    def listMemberMFAChallenges(self, userGUID, memberGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members/{1}/challenges{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["challenges"]
        challenges = []
        for challenge in JSONArray:
            challenges.append(Challenge(challenge))
        return challenges

    # Required Parameters: userGUID, memberGUID, answersMFA
    # Optional Parameters: None
    def resumeMemberAggregation(self, userGUID, memberGUID, answers):
        inner = {}
        inner["challenges"] = answers
        outer = {}
        outer["member"] = inner

        response = self.makeRequest("PUT", "/users/{0}/members/{1}/resume".format(userGUID, memberGUID), outer)
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: page, records_per_page
    def listMemberCredentials(self, userGUID, memberGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response =  self.makeRequest("GET", "/users/{0}/members/{1}/credentials{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["credentials"]
        credentials = []
        for credential in JSONArray:
            credentials.append(Credential(credential))
        return credentials

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: page, records_per_page
    def listMemberAccounts(self, userGUID, memberGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members/{1}/accounts{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["accounts"]
        accounts = []
        for account in JSONArray:
            accounts.append(Account(account))
        return accounts

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: from_date, to_date, page, records_per_page
    def listMemberTransactions(self, userGUID, memberGUID, from_date = "", to_date = "", page = "", records_per_page = ""):
        params = self.optionalParameters("", from_date, to_date, page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members/{1}/transactions{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["transactions"]
        transactions = []
        for transaction in JSONArray:
            transactions.append(Transaction(transaction))
        return transactions

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def verifyMember(self, userGUID, memberGUID):
        response = self.makeRequest("POST", "/users/{0}/members/{1}/verify".format(userGUID, memberGUID), "")
        return Member(json.loads(response)["member"])

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def identifyMember(self, userGUID, memberGUID):
        response = self.makeRequest("POST", "/users/{0}/members/{1}/identify".format(userGUID, memberGUID), "")
        return Member(json.loads(response)["member"])


    # ACCOUNT

    # Required Parameters: userGUID, accountGUID
    # Optional Parameters: None
    def readAccount(self, userGUID, accountGUID):
        response = self.makeRequest("GET", "/users/{0}/accounts/{1}".format(userGUID, accountGUID), "")
        return Account(json.loads(response)["account"])

    # Required Parameters: userGUID
    # Optional Parameters: page, records_per_page
    def listAccounts(self, userGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/accounts{1}".format(userGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["accounts"]
        accounts = []
        for account in JSONArray:
            accounts.append(Account(account))
        return accounts

    # Required Parameters: userGUID, accountGUID
    # Optional Parameters: from_date, to_date, page, records_per_page
    def listAccountTransactions(self, userGUID, accountGUID, from_date = "", to_date = "", page = "", records_per_page = ""):
        params = self.optionalParameters("", from_date, to_date, page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/accounts/{1}/transactions{2}".format(userGUID, accountGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["transactions"]
        transactions = []
        for transaction in JSONArray:
            transactions.append(Transaction(transaction))
        return transactions


    # TRANSACTION

    # Required Parameters: userGUID, transactionGUID
    # Optional Parameters: None
    def readTransaction(self, userGUID, transactionGUID):
        response = self.makeRequest("GET", "/users/{0}/transactions/{1}".format(userGUID, transactionGUID), "")
        return Transaction(json.loads(response)["transaction"])

    # Required Parameters: userGUID
    # Optional Parameters: from_date, to_date, page, records_per_page
    def listTransactions(self, userGUID, from_date = "", to_date = "", page = "", records_per_page = ""):
        params = self.optionalParameters("", from_date, to_date, page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/transactions{1}".format(userGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["transactions"]
        transactions = []
        for transaction in JSONArray:
            transactions.append(Transaction(transaction))
        return transactions


    # ACCOUNT NUMBER

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: page, records_per_page
    def listAccountNumbers(self, userGUID, memberGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members/{1}/account_numbers{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["account_numbers"]
        account_numbers = []
        for account_number in JSONArray:
            account_numbers.append(AccountNumber(account_number))
        return account_numbers


    # ACCOUNT OWNER

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: page, records_per_page
    def listAccountOwners(self, userGUID, memberGUID, page = "", records_per_page = ""):
        params = self.optionalParameters("", "", "", page, records_per_page)

        response = self.makeRequest("GET", "/users/{0}/members/{1}/account_owners{2}".format(userGUID, memberGUID, params), "")
        parsedJSON = json.loads(response)
        JSONArray = parsedJSON["account_owners"]
        account_owners = []
        for account_owner in JSONArray:
            account_owners.append(AccountOwner(account_owner))
        return account_owners


    # CONNECT WIDGET

    # Required Parameters: userGUID
    # Optional Parameters: None
    def createWidget(self, userGUID):
        response = self.makeRequest("POST", "/users/{0}/connect_widget_url".format(userGUID), "")
        return Connect(json.loads(response)["user"])


    # CLIENT

    # Required Parameters: mode, endpoint, body
    # Optional Parameters: None
    def makeRequest(self, mode, endpoint, body):
        body = json.dumps(body)
        conn = HTTPSConnection(self.environment)
        headers = { "Accept" : "application/vnd.mx.atrium.v1+json", "Content-Type" : "application/json", "MX-API-Key" : self.mxAPIKEY, "MX-Client-ID" : self.mxCLIENTID }
        conn.request(mode, endpoint, body, headers)
        response = conn.getresponse()
        self.httpError(response.status)
        return response.read()

    # Print and exit on http error
    def httpError(self, code):
        if code == 400:
            print(str(code) + " error: Required parameter is missing.")
        elif code == 401:
            print(str(code) + " error: Invalid MX-API-Key, MX-Client-ID, or being used in wrong environment.")
        elif code == 403:
            print(str(code) + " error: Requests must be HTTPS.")
        elif code == 404:
            print(str(code) + " error: GUID / URL path not recognized.")
        elif code == 405:
            print(str(code) + " error: Endpoint constraint not met.")
        elif code == 406:
            print(str(code) + " error: Specifiy valid API version.")
        elif code == 409:
            print(str(code) + " error: Object already exists.")
        elif code == 422:
            print(str(code) + " error: Data provided cannot be processed.")
        elif code == 500 or code == 502 or code == 504:
            print(str(code) + " error: An unexpected error occurred on MX's systems.")
        elif code == 503:
            print(str(code) + " error: Please try again later. The MX Platform is currently being updated.")

        # Quit on 4XX or 5XX errors
        if code // 100 == 4 or code // 100 == 5:
            sys.exit(0)

    def optionalParameters(self, name, from_date, to_date, page, records_per_page):
        params = "?"
        if name != "":
            params += "name=" + name + "&"
        if from_date != "":
            params += "from_date=" + from_date + "&"
        if to_date != "":
            params += "to_date=" + to_date + "&"
        if page != "":
            params += "page=" + page + "&"
        if records_per_page != "":
            params += "records_per_page=" + records_per_page + "&"
        params = params[:-1]

        return params
