from profile import Profile
import numpy as np
from profile.criterias import Sex, Weight
from dataSetsLib import CostOfLivingAnalysis
from dataSetsLib import MigrantsAnalysis
import pandas as pd
from sklearn.preprocessing import normalize

jeanneProfile = Profile(migrantsWeight=Weight.LOW,
                        unsafetyWeight=Weight.LOW,
                        age=24,
                        sex=Sex.FEMALE,
                        countryOfOrigin='Hong Kong',
                        healthWeight=Weight.LOW,
                        costOfLivingWeight=Weight.MEDIUM)

costOfLiving = CostOfLivingAnalysis(jeanneProfile).getDataSet()
migrants = MigrantsAnalysis(jeanneProfile).getDataSet()

matrix = pd.merge(costOfLiving, migrants, on=['geo'], how='inner')

print(matrix)

# select the columns to normalize
columns_to_normalize = ['costOfLiving', 'numberOfMigrants']

# normalize the selected columns
df_normalized = matrix.copy()
df_normalized[columns_to_normalize] = normalize(
    matrix[columns_to_normalize].values, axis=0)

print(df_normalized)

df_normalized['costOfLiving'] = df_normalized['costOfLiving'].mul(4)

df_normalized['numberOfMigrants'] = df_normalized['numberOfMigrants'].mul(-4)

print(df_normalized)

weighted_matrix = df_normalized[['costOfLiving', 'numberOfMigrants']]

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

print(ranked_alternatives)
