from .Sex import Sex
from .IncomeLevel import IncomeLevel


class PersonalSelector:

    def __init__(self, age: int, sex: Sex, countryOfOrigin: str,
                 incomeLevel: IncomeLevel):
        self.age = age
        self.sex = sex
        self.countryOfOrigin = countryOfOrigin
        self.incomeLevel = incomeLevel

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getCountryOfOrigin(self):
        return self.countryOfOrigin

    def getIncomeLevel(self):
        return self.incomeLevel
