# entity/user.py
class User:
    def __init__(self):
        pass

    def __init__(self, userId, username, password, role):
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    @property
    def userId(self):
        return self.__userId
    
    @userId.setter
    def userId(self, userId):
        self.__userId = userId
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role):
        self.__role = role

    def __str__(self):
        return f"User(ID: {self.__userId}, Username: {self.__username}, Role: {self.__role})"
