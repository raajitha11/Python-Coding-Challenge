
from dao.policy_dao import PolicyService
from entity.policy import Policy
from util.db_connection import DBConnection
import mysql.connector

class InsuranceServiceImpl(PolicyService):
    def createPolicy(self, policy: Policy) -> bool:
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO policies (policy_name, coverage, premium) VALUES (%s, %s, %s)",
                           (policy.policyName, policy.coverage, policy.premium))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Error creating policy:", e)
            return False
        finally:
            if connection.is_connected():
                connection.close()

    def getPolicy(self, policyId) -> Policy:
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM policies WHERE policy_id = %s", (policyId,))
            policy_record = cursor.fetchone()
            cursor.close()
            if policy_record:
                return Policy(policy_record[0], policy_record[1], policy_record[2], policy_record[3])
            else:
                return None
        except mysql.connector.Error as e:
            print("Error getting policy:", e)
            return None
        finally:
            if connection.is_connected():
                connection.close()

    def getAllPolicies(self) -> list:
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM policies")
            policy_records = cursor.fetchall()
            cursor.close()
            policies = []
            for policy_record in policy_records:
                policy = Policy(policy_record[0], policy_record[1], policy_record[2], policy_record[3])
                policies.append(policy)
            return policies
        except mysql.connector.Error as e:
            print("Error getting all policies:", e)
            return []
        finally:
            if connection.is_connected():
                connection.close()

    def updatePolicy(self, policy: Policy) -> bool:
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("UPDATE policies SET policy_name = %s, coverage = %s, premium = %s WHERE policy_id = %s",
                           (policy.policyName, policy.coverage, policy.premium, policy.policyId))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Error updating policy:", e)
            return False
        finally:
            if connection.is_connected():
                connection.close()

    def deletePolicy(self, policyId) -> bool:
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM policies WHERE policy_id = %s", (policyId,))
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Error deleting policy:", e)
            return False
        finally:
            if connection.is_connected():
                connection.close()
