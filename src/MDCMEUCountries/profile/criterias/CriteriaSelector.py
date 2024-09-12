from .Preference import Preference
from .Weight import Weight


class CriteriaSelector:

    def __init__(self, preference: Preference, weight: Weight):
        self.preference = preference
        self.weight = weight

    def getPreference(self):
        return self.preference

    def getWeight(self):
        return self.weight
