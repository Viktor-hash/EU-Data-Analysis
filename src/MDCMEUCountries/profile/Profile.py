from .criterias.Weight import Weight
from .criterias.Sex import Sex


class Profile:

    def __init__(self, unsafetyWeight: Weight, migrantsWeight: Weight,
                 age: int, sex: Sex, countryOfOrigin: str,
                 healthWeight: Weight, costOfLivingWeight: Weight):
        # Personal criterias
        self.age = age
        self.countryOfOrigin = countryOfOrigin
        self.sex = sex

        # Criterias/Weights
        self.migrantsWeight = migrantsWeight
        self.unsafetyWeight = unsafetyWeight
        self.healthWeight = healthWeight
        self.costOfLivingWeight = costOfLivingWeight
