from .DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
import pandas as pd
import numpy as np

from profile.criterias import Sex, Weight


# Demography analysis class that creates the data set
class CostOfLivingAnalysis(DataSetBase):

    def __init__(self, profile: Profile):
        super().__init__(
            "C:\data analysis best country in europe\costOfLiving\costOfLiving.tsv",
            profile)
        self.CreateDataSet()

    def CreateDataSet(self):
        dataSetTsvLeft = self.dataSetTsv.iloc[:, 0].str.split(',', expand=True)
        dataSetTsvLeft.columns = self.dataSetTsv.columns[0].split(',')

        self.dataSetTsv.drop(self.dataSetTsv.columns[[0]],
                             axis=1,
                             inplace=True)

        dfMerged = pd.concat([dataSetTsvLeft, self.dataSetTsv], axis=1)

        dfMerged.rename(columns={dfMerged.columns[3]: 'geo'}, inplace=True)

        dfMerged.drop(dfMerged.columns[[0, 1, 2]], axis=1, inplace=True)

        dfMerged = dfMerged[dfMerged['geo'].isin(abreviationToCountry.keys())]

        dfMerged.replace({"geo": abreviationToCountry}, inplace=True)

        dfMerged.columns = dfMerged.columns.str.replace(' ', '')

        dfMerged = dfMerged[['geo', '2023']]

        dfMerged = dfMerged[~dfMerged['2023'].str.contains(":")]

        dfMerged.rename(columns={'2023': 'costOfLiving'}, inplace=True)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
