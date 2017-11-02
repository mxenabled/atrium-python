from httplib import HTTPSConnection
import json
import sys

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
    # Optional Parameters: identifier, isDisabled, metadata
    def createUser(self, identifier, isDisabled, metadata):
        inner = {}
        if identifier != "":
            inner["identifier"] = identifier
        isDisabled = isDisabled.lower()
        if isDisabled == "" or isDisabled == "false":
            inner["is_disabled"] = "false"
        else:
            inner["is_disabled"] = "true"
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["user"] = inner
        body = json.dumps(outer)

        return self.makeRequest("POST", "/users", body)

    # Required Parameters: userGUID
    # Optional Parameters: None
    def readUser(self, userGUID):
        return self.makeRequest("GET", "/users/{0}".format(userGUID), "")


    # Required Parameters: None
    # Optional Parameters: userGUID, identifier, isDisabled, metadata
    def updateUser(self, userGUID, identifier, isDisabled, metadata):
        inner = {}
        if identifier != "":
            inner["identifier"] = identifier
        if isDisabled != "":
            inner["is_disabled"] = isDisabled
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["user"] = inner
        body = json.dumps(outer)

        return self.makeRequest("PUT", "/users/{0}".format(userGUID), body)

    # Required Parameters: None
    # Optional Parameters: pageNumber, recordsPerPage
    def listUsers(self, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users{0}".format(params), "")

    # Required Parameters: userGUID
    # Optional Parameters: None
    def deleteUser(self, userGUID):
        return self.makeRequest("DELETE", "/users/{0}".format(userGUID), "")


    # INSTITUTION


    # Required Parameters: None
    # Optional Parameters: name, pageNumber, recordsPerPage
    def listInstitutions(self, name, pageNumber, recordsPerPage):
        params = self.optionalParameters(name, "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/institutions{0}".format(params), "")

    # Required Parameters: institutionCode
    # Optional Parameters: None
    def readInstitution(self, institutionCode):
        return self.makeRequest("GET", "/institutions/{0}".format(institutionCode), "")

    # Required Parameters: institutionCode
    # Optional Parameters: pageNumber, recordsPerPage
    def readInstitutionCredentials(self, institutionCode, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/institutions/{0}/credentials{1}".format(institutionCode, params), "")


    # MEMBER


    # Required Parameters: userGUID, credentials, institutionCode
    # Optional Parameters: identifier, metadata
    def createMember(self, userGUID, credentials, institutionCode, identifier, metadata):
        inner = {}
        inner["institution_code"] = institutionCode
        inner["credentials"] = credentials
        if identifier != "":
            inner["identifier"] = identifier
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["member"] = inner
        body = json.dumps(outer)

        return self.makeRequest("POST", "/users/{0}/members".format(userGUID), body)

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def readMember(self, userGUID, memberGUID):
        return self.makeRequest("GET", "/users/{0}/members/{1}".format(userGUID, memberGUID), "")

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: credentials, identifier, metadata
    def updateMember(self, userGUID, memberGUID, credentials, identifier, metadata):
        inner = {}
        if credentials != "":
            inner["credentials"] = credentials
        if identifier != "":
            inner["identifier"] = identifier
        if metadata != "":
            inner["metadata"] = metadata
        outer = {}
        outer["member"] = inner
        body = json.dumps(outer)

        return self.makeRequest("PUT", "/users/{0}/members/{1}".format(userGUID, memberGUID), body)

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def deleteMember(self, userGUID, memberGUID):
        return self.makeRequest("DELETE", "/users/{0}/members/{1}".format(userGUID, memberGUID), "")

    # Required Parameters: userGUID
    # Optional Parameters: pageNumber, recordsPerPage
    def listMembers(self, userGUID, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/members{1}".format(userGUID, params), "")

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: None
    def aggregateMember(self, userGUID, memberGUID):
        return self.makeRequest("POST", "/users/{0}/members/{1}/aggregate".format(userGUID, memberGUID), "")

    # Required Parameters:  userGUID, memberGUID
    # Optional Parameters: None
    def readMemberAggregationStatus(self, userGUID, memberGUID):
        return self.makeRequest("GET", "/users/{0}/members/{1}/status".format(userGUID, memberGUID), "")

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: pageNumber, recordsPerPage
    def listMemberMFAChallenges(self, userGUID, memberGUID, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/members/{1}/challenges{2}".format(userGUID, memberGUID, params), "")

    # Required Parameters: userGUID, memberGUID, answersMFA
    # Optional Parameters: None
    def resumeMemberAggregation(self, userGUID, memberGUID, answers):
        inner = {}
        inner["challenges"] = answers
        outer = {}
        outer["member"] = inner
        body = json.dumps(outer)

        return self.makeRequest("PUT", "/users/{0}/members/{1}/resume".format(userGUID, memberGUID), body)

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: pageNumber, recordsPerPage
    def listMemberCredentials(self, userGUID, memberGUID, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/members/{1}/credentials{2}".format(userGUID, memberGUID, params), "")

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: pageNumber, recordsPerPage
    def listMemberAccounts(self, userGUID, memberGUID, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/members/{1}/accounts{2}".format(userGUID, memberGUID, params), "")

    # Required Parameters: userGUID, memberGUID
    # Optional Parameters: fromDate, toDate, pageNumber, recordsPerPage
    def listMemberTransactions(self, userGUID, memberGUID, fromDate, toDate, pageNumber, recordsPerPage):
        params = self.optionalParameters("", fromDate, toDate, pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/members/{1}/transactions{2}".format(userGUID, memberGUID, params), "")

    # ACCOUNT


    # Required Parameters: userGUID, accountGUID
    # Optional Parameters: None
    def readAccount(self, userGUID, accountGUID):
        return self.makeRequest("GET", "/users/{0}/accounts/{1}".format(userGUID, accountGUID), "")

    # Required Parameters: userGUID
    # Optional Parameters: pageNumber, recordsPerPage
    def listAccounts(self, userGUID, pageNumber, recordsPerPage):
        params = self.optionalParameters("", "", "", pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/accounts{1}".format(userGUID, params), "")

    # Required Parameters: userGUID, accountGUID
    # Optional Parameters: fromDate, toDate, pageNumber, recordsPerPage
    def listAccountTransactions(self, userGUID, accountGUID, fromDate, toDate, pageNumber, recordsPerPage):
        params = self.optionalParameters("", fromDate, toDate, pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/accounts/{1}/transactions{2}".format(userGUID, memberGUID, params), "")



    # TRANSACTION

    # Required Parameters: userGUID, transactionGUID
    # Optional Parameters: None
    def readTransaction(self, userGUID, transactionGUID):
        return self.makeRequest("GET", "/users/{0}/transactions/{1}".format(userGUID, transactionGUID), "")

    # Required Parameters: userGUID
    # Optional Parameters: fromDate, toDate, pageNumber, recordsPerPage
    def listTransactions(self, userGUID, fromDate, toDate, pageNumber, recordsPerPage):
        params = self.optionalParameters("", fromDate, toDate, pageNumber, recordsPerPage)

        return self.makeRequest("GET", "/users/{0}/transactions{1}".format(userGUID, params), "")


    # CONNECT WIDGET

    # Required Parameters: userGUID
    # Optional Parameters: None
    def createWidget(self, userGUID):
        return self.makeRequest("POST", "/users/{0}/connect_widget_url".format(userGUID), "")


    # CLIENT

    # Required Parameters: mode, endpoint, body
    # Optional Parameters: None
    def makeRequest(self, mode, endpoint, body):
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

    def optionalParameters(self, name, fromDate, toDate, pageNumber, recordsPerPage):
        params = "?"
        if name != "":
            params += "name=" + name + "&"
        if fromDate != "":
            params += "from_date=" + fromDate + "&"
        if toDate != "":
            params += "to_date=" + toDate + "&"
        if pageNumber != "":
            params += "page=" + pageNumber + "&"
        if recordsPerPage != "":
            params += "records_per_page=" + recordsPerPage + "&"
        params = params[:-1]

        return params
