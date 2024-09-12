from .DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
import pandas as pd
import numpy as np


# Tax analysis class that creates the data set
class TaxAnalysis(DataSetBase):

    def __init__(self, profile: Profile):
        super().__init__(
            r'C:\data analysis best country in europe\tax\tax.tsv', profile)
        age = profile.personalSelector.age
        if (age < 35):
            self.agetreshold = "Y_LT35"
        elif (age >= 35 and age < 45):
            self.agetreshold = "Y35-44"
        elif (age >= 45 and age < 55):
            self.agetreshold = "Y45-54"
        elif (age >= 55 and age < 65):
            self.agetreshold = "Y55-64"
        elif (age >= 65 and age < 75):
            self.agetreshold = "Y65-74"
        elif (age >= 75):
            self.agetreshold = "Y_GE75"
        self.CreateDataSet()

    def CreateDataSet(self):
        dataSetTsvLeft = self.dataSetTsv.iloc[:, 0].str.split(',', expand=True)
        dataSetTsvLeft.columns = self.dataSetTsv.columns[0].split(',')

        self.dataSetTsv.drop(self.dataSetTsv.columns[[0]],
                             axis=1,
                             inplace=True)

        dfMerged = pd.concat([dataSetTsvLeft, self.dataSetTsv], axis=1)

        dfMerged.columns = dfMerged.columns.str.replace(' ', '')

        dfMerged = dfMerged[dfMerged['quantile'] ==
                            self.profile.personalSelector.incomeLevel.value]

        dfMerged = dfMerged[dfMerged['age'] == self.agetreshold]

        dfMerged.rename(columns={dfMerged.columns[4]: 'geo'}, inplace=True)

        charactersToRemove = ['s', ' ']

        for character in charactersToRemove:
            for i in range(2003, 2021):
                dfMerged[str(i)] = dfMerged[str(i)].str.replace(character, '')

        dfMerged.replace(':', np.nan, inplace=True)

        listYears = []

        for i in range(2003, 2021):
            dfMerged[str(i)] = dfMerged[str(i)].astype(float)
            listYears.append(str(i))

        dfSubset = dfMerged[listYears]

        dfSubset = dfSubset.T.fillna(dfSubset.mean(axis=1)).T.dropna()

        dfMerged[listYears] = dfSubset[listYears]

        dfMerged = dfMerged[dfMerged['geo'].isin(abreviationToCountry.keys())]

        dfMerged.replace({"geo": abreviationToCountry}, inplace=True)

        dfMerged = dfMerged[['geo', '2020']]

        dfMerged.rename(columns={'2020': 'taxs'}, inplace=True)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
