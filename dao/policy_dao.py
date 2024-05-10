# dao/ipolicy_service.py
from abc import ABC, abstractmethod
from entity.policy import Policy

class PolicyService(ABC):
    @abstractmethod
    def createPolicy(self, policy: Policy) -> bool:
        pass
    
    @abstractmethod
    def getPolicy(self, policyId) -> Policy:
        pass
    
    @abstractmethod
    def getAllPolicies(self) -> list:
        pass
    
    @abstractmethod
    def updatePolicy(self, policy: Policy) -> bool:
        pass
    
    @abstractmethod
    def deletePolicy(self, policyId) -> bool:
        pass
