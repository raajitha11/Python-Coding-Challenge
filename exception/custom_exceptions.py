# myexceptions/policy_exceptions.py
class PolicyNotFoundException(Exception):
    def __init__(self, message="Policy not found."):
        self.message = message
        super().__init__(self.message)
