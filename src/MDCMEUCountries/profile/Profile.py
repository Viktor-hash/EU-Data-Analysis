from .criterias.PersonalSelector import PersonalSelector
from .criterias.CriteriaSelector import CriteriaSelector


class Profile:

    def __init__(self, personalSelector: PersonalSelector,
                 costOfLiving: CriteriaSelector, taxs: CriteriaSelector,
                 migrants: CriteriaSelector, earnings: CriteriaSelector):
        # Personal criterias
        self.personalSelector = personalSelector

        # Preferences and Weights
        self.migrants = migrants
        self.costOfLiving = costOfLiving
        self.taxs = taxs
        self.earnings = earnings

    def getPreferences(self, dataSet: str):
        if (dataSet == 'costOfLiving'):
            return self.costOfLiving
        elif (dataSet == 'taxs'):
            return self.taxs
        elif (dataSet == 'migrants'):
            return self.migrants
        elif (dataSet == 'earnings'):
            return self.earnings
