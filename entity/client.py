# entity/client.py
class Client:
    def __init__(self):
        pass

    def __init__(self, clientId, clientName, contactInfo, policy):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policy = policy

    @property
    def clientId(self):
        return self.__clientId
    
    @clientId.setter
    def clientId(self, clientId):
        self.__clientId = clientId
    
    @property
    def clientName(self):
        return self.__clientName
    
    @clientName.setter
    def clientName(self, clientName):
        self.__clientName = clientName
    
    @property
    def contactInfo(self):
        return self.__contactInfo
    
    @contactInfo.setter
    def contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo
    
    @property
    def policy(self):
        return self.__policy
    
    @policy.setter
    def policy(self, policy):
        self.__policy = policy

    def __str__(self):
        return f"Client(ID: {self.__clientId}, Name: {self.__clientName})"
