from dataSetsLib.DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
import pandas as pd


# Demography analysis class that creates the data set
class DemographyAnalysis(DataSetBase):

    def __init__(self, profile: Profile):
        super().__init__(
            'C:\data analysis best country in europe\demo_pjan_tabular.tsv\demo_pjan_tabular.tsv',
            profile)
        self.CreateDataSet()

    def CreateDataSet(self):
        dataSetTsvLeft = self.dataSetTsv.iloc[:, 0].str.split(',', expand=True)
        dataSetTsvLeft.columns = self.dataSetTsv.columns[0].split(',')

        self.dataSetTsv.drop(self.dataSetTsv.columns[[0]],
                             axis=1,
                             inplace=True)

        dfMerged = pd.concat([dataSetTsvLeft, self.dataSetTsv], axis=1)

        dfMerged.rename(columns={dfMerged.columns[4]: 'geo'}, inplace=True)
        dfMerged = dfMerged[dfMerged['age'] == 'TOTAL']

        dfMerged.columns = dfMerged.columns.str.replace(' ', '')

        dfMerged = dfMerged[dfMerged['sex'] == 'T']

        dfMerged = dfMerged[['geo', '2023']]

        dfMerged = dfMerged[~dfMerged['2023'].str.contains(":")]

        charactersToRemove = ['b', 'd', 'u', ' ', 'e', 'p']

        for character in charactersToRemove:
            dfMerged['2023'] = dfMerged['2023'].str.replace(character, '')

        dfMerged = dfMerged.groupby(['geo']).sum()

        dfMerged.reset_index(inplace=True)

        dfMerged['2023'] = dfMerged['2023'].astype(float)

        dfMerged.rename(columns={'2023': 'population'}, inplace=True)

        dfMerged = dfMerged[dfMerged['geo'].isin(abreviationToCountry.keys())]

        dfMerged.replace({"geo": abreviationToCountry}, inplace=True)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
