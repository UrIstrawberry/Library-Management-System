class Member:

    def __init__(self, member_id, name, email):

        self.__member_id = member_id
        self.__name = name
        self.__email = email

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email