from dataSetsLib.DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
from dataSetsLib.DemographyAnalysis import DemographyAnalysis
import pandas as pd
import numpy as np


# Earnings analysis class that creates the data set and filters it by the migrants Weight
class EarningsAnalysis(DataSetBase):

    def __init__(self, profile: Profile):
        super().__init__(
            r"C:\data analysis best country in europe\earnings\earn_nt_net_tabular.tsv",
            profile)
        self.demographyAnalysis = DemographyAnalysis(profile)
        self.CreateDataSet()

    # Create the data set by merging the demography data set with the migrants data set
    def CreateDataSet(self):
        dataSetTsvLeft = self.dataSetTsv.iloc[:, 0].str.split(',', expand=True)
        dataSetTsvLeft.columns = self.dataSetTsv.columns[0].split(',')

        self.dataSetTsv.drop(self.dataSetTsv.columns[[0]],
                             axis=1,
                             inplace=True)

        dfMerged = pd.concat([dataSetTsvLeft, self.dataSetTsv], axis=1)

        dfMerged.rename(columns={'geo\TIME_PERIOD': 'geo'}, inplace=True)

        dfMerged.columns = dfMerged.columns.str.replace(' ', '')

        dfMerged = dfMerged[dfMerged['estruct'] == 'NET']
        dfMerged = dfMerged[dfMerged['currency'] == 'EUR']

        listColumns = ['geo']
        listYears = []

        for i in range(2000, 2024):
            listYears.append(str(i))
            listColumns.append(str(i))
            dfMerged[str(i)] = dfMerged[str(i)].astype(str)
            dfMerged[str(i)] = dfMerged[str(i)].str.replace(' ', '')

        dfMerged.replace(':', np.nan, inplace=True)

        dfMerged[listYears] = dfMerged[listYears].astype(float)

        dfSubset = dfMerged[listYears]

        dfSubset = dfSubset.T.fillna(dfSubset.mean(axis=1)).T.dropna()

        dfMerged[listYears] = dfSubset[listYears]

        dfMerged = dfMerged[listColumns]

        dfMerged = dfMerged[dfMerged['geo'].isin(abreviationToCountry.keys())]

        dfMerged.rename(columns={'2023': 'earnings'}, inplace=True)

        dfMerged = dfMerged[['geo', 'earnings']]

        dfMerged = dfMerged[['geo', 'earnings']].groupby(['geo']).sum()

        dfMerged.reset_index(inplace=True)

        dfMerged.replace({"geo": abreviationToCountry}, inplace=True)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
