# entity/policy.py
class Policy:
    def __init__(self):
        pass
    
    def __init__(self, policyId=None, policyName="", coverage="", premium=0.0):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__coverage = coverage
        self.__premium = premium

    @property
    def policyId(self):
        return self.__policyId
    
    @policyId.setter
    def policyId(self, policyId):
        self.__policyId = policyId
    
    @property
    def policyName(self):
        return self.__policyName
    
    @policyName.setter
    def policyName(self, policyName):
        self.__policyName = policyName
    
    @property
    def coverage(self):
        return self.__coverage
    
    @coverage.setter
    def coverage(self, coverage):
        self.__coverage = coverage
    
    @property
    def premium(self):
        return self.__premium
    
    @premium.setter
    def premium(self, premium):
        self.__premium = premium

    def __str__(self):
        return f"Policy(ID: {self.__policyId}, Name: {self.__policyName}, Coverage: {self.__coverage}, Premium: {self.__premium})"
