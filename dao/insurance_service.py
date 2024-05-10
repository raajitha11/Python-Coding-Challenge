# dao/insurance_service_impl.py
from dao.policy_dao import PolicyService
from entity.policy import Policy

class InsuranceServiceImpl(PolicyService):
    def __init__(self):
        # Simulating database with a dictionary
        self.policy_db = {}
        self.next_policy_id = 1
    
    def createPolicy(self, policy: Policy) -> bool:
        # Assigning unique ID to the policy
        policy.policyId = self.next_policy_id
        # Adding policy to the database
        self.policy_db[policy.policyId] = policy
        # Incrementing ID for next policy
        self.next_policy_id += 1
        return True  # Successfully created policy
    
    def getPolicy(self, policyId) -> Policy:
        # Check if policy exists in the database
        if policyId in self.policy_db:
            return self.policy_db[policyId]
        else:
            return None  # Policy not found
    
    def getAllPolicies(self) -> list:
        return list(self.policy_db.values())
    
    def updatePolicy(self, policy: Policy) -> bool:
        # Check if policy exists in the database
        if policy.policyId in self.policy_db:
            # Update policy details
            self.policy_db[policy.policyId] = policy
            return True  # Successfully updated policy
        else:
            return False  # Policy not found
    
    def deletePolicy(self, policyId) -> bool:
        # Check if policy exists in the database
        if policyId in self.policy_db:
            # Delete policy from the database
            del self.policy_db[policyId]
            return True  # Successfully deleted policy
        else:
            return False  # Policy not found
