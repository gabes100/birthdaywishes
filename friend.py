class Friend():
    # Action List
    # 0 --------- Facebook message [False] send email to self [False]
    # 1 (default) Facebook message [True] send email to self [True]
    # 2 --------- Facebook message [True] send email to self [False]
    # 3 --------- Facebook message [False] send email to self [True]
    # 4 --------- Facebook message [True] send email to self [True] send reminder n number of days before [True]
    # 5 --------- Facebook message [False] send email to self [True] send reminder n number of days before [True]
    def __init__(self, birthday, first_name, last_name, action, nickname =""):
        self.first_name=first_name
        self.last_name=last_name
        self.nickname=nickname
        self.action=int(action)
        self.birthday=birthday
        self.message=""
        self.birthdayFormat() # make birthday
    def birthdayFormat(self):
        convert = self.birthday.split("/")
        if len(convert) == 3:
            self.bmonth=convert[0]
            self.bday=convert[1]
            self.byear=convert[2]
        else:
            self.bmonth=convert[0]
            self.bday=convert[1]
            self.byear=""
    def setMessage(self, value):
        self.message = value
    def getMessage(self):
        return self.message
    def getBirthday(self):
        return self.birthday
    def getBday(self):
        return self.bday
    def getBmonth(self):
        return self.bmonth
    def getByear(self):
        return self.byear
    def getAction(self):
        return self.action
    def getName(self):
        if self.nickname != "":
            return self.nickname
        else:
            return self.first_name
    def getFullName(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        s = "Name: " + self.first_name + " " +  self.last_name  +"\n"
        s+= "Nickname: " + self.nickname +"\n"
        s+= "Birthday: " + str(self.birthday) + "\n"
        s+= "Priority: " + str(self.action) + "\n"
        s+= "Message: "  + self.message + "\n"
        return s
