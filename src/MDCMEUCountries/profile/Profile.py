from .criterias.Weight import Weight
from .criterias.Sex import Sex
from .criterias.IncomeLevel import IncomeLevel


class Profile:

    def __init__(self, unsafetyWeight: Weight, migrantsWeight: Weight,
                 age: int, sex: Sex, countryOfOrigin: str,
                 healthWeight: Weight, costOfLivingWeight: Weight,
                 incomeLevel: IncomeLevel, taxWeight: Weight,
                 earningWeight: Weight):
        # Personal criterias
        self.age = age
        self.countryOfOrigin = countryOfOrigin
        self.sex = sex
        self.incomeLevel = incomeLevel

        # Criterias/Weights
        self.migrantsWeight = migrantsWeight
        self.unsafetyWeight = unsafetyWeight
        self.healthWeight = healthWeight
        self.costOfLivingWeight = costOfLivingWeight
        self.taxWeight = taxWeight
        self.earningWeight = earningWeight
