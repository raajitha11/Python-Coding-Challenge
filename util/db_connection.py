# util/db_connection.py
import mysql.connector
from util.property_util import PropertyUtil
import time

class DBConnection:
    __connection = None

    @staticmethod
    def getConnection():
        property_file = r"C:\Users\raaji\OneDrive\Documents\hexaware training\Insurance\util\db.properties"
        connection_string = PropertyUtil().getPropertyString(property_file)
        try:
            DBConnection.__connection = mysql.connector.connect(**connection_string)
            print("Connected to MySQL database successfully.")
            return DBConnection.__connection
        except mysql.connector.Error as err:
            print("Error connecting to MySQL:", err)
            return None
        

