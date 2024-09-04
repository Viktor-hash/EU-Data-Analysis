from profile import Profile
import numpy as np
from profile.criterias import Sex, Weight, IncomeLevel
from dataSetsLib import CostOfLivingAnalysis
from dataSetsLib import MigrantsAnalysis
from dataSetsLib import TaxAnalysis
from dataSetsLib import EarningsAnalysis
import pandas as pd
from sklearn.preprocessing import normalize

michaelProfile = Profile(age=41,
                         sex=Sex.MALE,
                         countryOfOrigin='Hong Kong',
                         incomeLevel=IncomeLevel.HIGH,
                         costOfLivingWeight=Weight.MEDIUM_LESS,
                         taxWeight=Weight.HIGH_LESS,
                         earningWeight=Weight.HIGH_MORE,
                         migrantsWeight=Weight.HIGH_LESS,
                         healthWeight=Weight.MEDIUM_MORE,
                         unsafetyWeight=Weight.MEDIUM_LESS)

# Economic analysis
costOfLiving = CostOfLivingAnalysis(michaelProfile).getDataSet()
taxLevel = TaxAnalysis(michaelProfile).getDataSet()
earningLevel = EarningsAnalysis(michaelProfile).getDataSet()

print(earningLevel)

# Safety and Security

# Culture and lifestyle
migrants = MigrantsAnalysis(michaelProfile).getDataSet()

# Education and Healthcare

# Environment and Climate

# Visa and Immigration Requirements

# Infrastructure and Transportation

# Personal Freedoms

matrix = pd.merge(costOfLiving, migrants, on=['geo'], how='inner')

matrix = pd.merge(matrix, taxLevel, on=['geo'], how='inner')

# select the columns to normalize
columns_to_normalize = ['costOfLiving', 'numberOfMigrants', 'taxLevel']

# normalize the selected columns
df_normalized = matrix.copy()
df_normalized[columns_to_normalize] = normalize(
    matrix[columns_to_normalize].values, axis=0)

df_normalized['costOfLiving'] = df_normalized['costOfLiving'].mul(
    michaelProfile.migrantsWeight.value)

df_normalized['numberOfMigrants'] = df_normalized['numberOfMigrants'].mul(
    michaelProfile.migrantsWeight.value)

df_normalized['taxLevel'] = df_normalized['taxLevel'].mul(
    michaelProfile.taxWeight.value)

weighted_matrix = df_normalized[[
    'costOfLiving', 'numberOfMigrants', 'taxLevel'
]]

# calculate the ideal solution (IS) and negative ideal solution (NIS)
IS = weighted_matrix.max()
NIS = weighted_matrix.min()

# calculate the distance from the ideal solution (DIS) and distance from the negative ideal solution (DNIS)
DIS = np.sqrt(np.sum((weighted_matrix - IS)**2, axis=1))
DNI = np.sqrt(np.sum((weighted_matrix - NIS)**2, axis=1))

# calculate the relative closeness (RC)
RC = pd.DataFrame(DNI / (DIS + DNI), columns=['Relative Closeness'])

result = pd.concat([df_normalized['geo'], RC], axis=1)

ranked_alternatives = result.sort_values(by='Relative Closeness',
                                         ascending=False)

#print(ranked_alternatives)
