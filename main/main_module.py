import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao.insurance_service_imp import InsuranceServiceImpl
from entity.policy import Policy
from exception.custom_exceptions import PolicyNotFoundException

class MainModule:
    def __init__(self):
        self.insurance_service = InsuranceServiceImpl()

    def display_menu(self):
        print("Insurance Management System")
        print("1. Create Policy")
        print("2. Get Policy")
        print("3. Get All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_policy()
            elif choice == "2":
                self.get_policy()
            elif choice == "3":
                self.get_all_policies()
            elif choice == "4":
                self.update_policy()
            elif choice == "5":
                self.delete_policy()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_policy(self):
        # policy_id = int(input("Enter policy ID: "))
        policy_name = input("Enter policy name: ")
        coverage = input("Enter coverage: ")
        premium = float(input("Enter premium: "))
        policy = Policy(policyName=policy_name, coverage=coverage, premium=premium)
        success = self.insurance_service.createPolicy(policy)
        if success:
            print("Policy created successfully.")
        else:
            print("Failed to create policy.")

    def get_policy(self):
        try:
            policy_id = int(input("Enter policy ID: "))
            policy = self.insurance_service.getPolicy(policy_id)
            if policy is None:
                raise PolicyNotFoundException()
            else:
                print("Policy details:")
                print(policy)
        except ValueError:
            print("Invalid input. Policy ID must be an integer.")
        except PolicyNotFoundException as e:
            print(e.message)

    def get_all_policies(self):
        policies = self.insurance_service.getAllPolicies()
        if not policies:
            print("No policies found.")
        else:
            print("All Policies:")
            for policy in policies:
                print(policy)

    def update_policy(self):
        policy_id = int(input("Enter policy ID to update: "))
        policy_name = input("Enter updated policy name: ")
        coverage = input("Enter updated coverage: ")
        premium = float(input("Enter updated premium: "))
        policy = Policy(policy_id, policy_name, coverage, premium)
        success = self.insurance_service.updatePolicy(policy)
        if success:
            print("Policy updated successfully.")
        else:
            print("Failed to update policy.")

    def delete_policy(self):
        policy_id = int(input("Enter policy ID to delete: "))
        success = self.insurance_service.deletePolicy(policy_id)
        if success:
            print("Policy deleted successfully.")
        else:
            print("Failed to delete policy.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
