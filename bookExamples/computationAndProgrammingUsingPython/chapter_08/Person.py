import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthDate):
        self.birthday = birthDate

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name