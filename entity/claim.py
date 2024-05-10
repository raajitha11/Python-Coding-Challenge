# entity/claim.py
class Claim:
    def __init__(self):
        pass

    def __init__(self, claimId, claimNumber, dateFiled, claimAmount, status, policy, client):
        self.__claimId = claimId
        self.__claimNumber = claimNumber
        self.__dateFiled = dateFiled
        self.__claimAmount = claimAmount
        self.__status = status
        self.__policy = policy
        self.__client = client

    @property
    def claimId(self):
        return self.__claimId
    
    @claimId.setter
    def claimId(self, claimId):
        self.__claimId = claimId
    
    @property
    def claimNumber(self):
        return self.__claimNumber
    
    @claimNumber.setter
    def claimNumber(self, claimNumber):
        self.__claimNumber = claimNumber
    
    @property
    def dateFiled(self):
        return self.__dateFiled
    
    @dateFiled.setter
    def dateFiled(self, dateFiled):
        self.__dateFiled = dateFiled
    
    @property
    def claimAmount(self):
        return self.__claimAmount
    
    @claimAmount.setter
    def claimAmount(self, claimAmount):
        self.__claimAmount = claimAmount
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status
    
    @property
    def policy(self):
        return self.__policy
    
    @policy.setter
    def policy(self, policy):
        self.__policy = policy
    
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, client):
        self.__client = client

    def __str__(self):
        return f"Claim(ID: {self.__claimId}, Number: {self.__claimNumber}, Amount: {self.__claimAmount})"
