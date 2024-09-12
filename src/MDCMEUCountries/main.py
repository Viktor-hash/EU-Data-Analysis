from profile import Profile
import numpy as np
from profile.criterias import Sex, Weight, IncomeLevel
from dataSetsLib import CostOfLivingAnalysis
from dataSetsLib import MigrantsAnalysis
from dataSetsLib import TaxAnalysis
from dataSetsLib import EarningsAnalysis
import pandas as pd
from sklearn.preprocessing import normalize
from profile.criterias import Sex, Weight, IncomeLevel, Preference
from profile.criterias import PersonalSelector, CriteriaSelector
from calculations import RankingCalculations

michaelPersonalSelector = PersonalSelector(
    age=24,
    sex=Sex.MALE,
    countryOfOrigin='India',
    incomeLevel=IncomeLevel.MID,
)

michaelCostOfLiving = CriteriaSelector(
    preference=Preference.HIGH,
    weight=Weight.HIGH,
)

michaelTaxs = CriteriaSelector(
    preference=Preference.HIGH,
    weight=Weight.HIGH,
)

michaelMigrants = CriteriaSelector(
    preference=Preference.MID,
    weight=Weight.MID,
)

michaelEarnings = CriteriaSelector(
    preference=Preference.LOW,
    weight=Weight.MID,
)

michaelProfile = Profile(personalSelector=michaelPersonalSelector,
                         costOfLiving=michaelCostOfLiving,
                         taxs=michaelTaxs,
                         migrants=michaelMigrants,
                         earnings=michaelEarnings)

ranking = RankingCalculations(
    michaelProfile,
    ['costOfLiving', 'taxs', 'migrants', 'earnings']).getRanking()

print(ranking)
