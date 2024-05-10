# entity/payment.py
class Payment:
    def __init__(self):
        pass

    def __init__(self, paymentId, paymentDate, paymentAmount, client):
        self.__paymentId = paymentId
        self.__paymentDate = paymentDate
        self.__paymentAmount = paymentAmount
        self.__client = client

    @property
    def paymentId(self):
        return self.__paymentId
    
    @paymentId.setter
    def paymentId(self, paymentId):
        self.__paymentId = paymentId
    
    @property
    def paymentDate(self):
        return self.__paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate
    
    @property
    def paymentAmount(self):
        return self.__paymentAmount
    
    @paymentAmount.setter
    def paymentAmount(self, paymentAmount):
        self.__paymentAmount = paymentAmount
    
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, client):
        self.__client = client

    def __str__(self):
        return f"Payment(ID: {self.__paymentId}, Amount: {self.__paymentAmount})"
