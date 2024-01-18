class User():
    count_id = 0
    def __init__(self, name, email, message):
        self.__user_id = User.count_id
        self.__name = name
        self.__email = email
        self.__message = message
    def get_user_id(self):
        return self.__user_id
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_message(self):
        return self.__message
    def set_user_id(self,user_id):
        self.__user_id = user_id
    def set_name(self,name):
        self.__name = name
    def set_email(self,email):
        self.__email = email
    def set_message(self,message):
        self.__message = message