from dataSetsLib.DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
from dataSetsLib.DemographyAnalysis import DemographyAnalysis
import pandas as pd


# Migrants analysis class that creates the data set and filters it by the migrants Weight
class MigrantsAnalysis(DataSetBase):

    def __init__(self, profile: Profile):
        super().__init__(
            'C:\data analysis best country in europe\estat_lfsa_pfganwsm.tsv\estat_lfsa_pfganwsm.tsv',
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

        dfMerged.rename(columns={dfMerged.columns[7]: 'geo'}, inplace=True)
        dfMerged.rename(columns={'2023 ': '2023'}, inplace=True)
        dfMerged.rename(columns={'2021 ': '2021'}, inplace=True)

        dfMerged = dfMerged[~dfMerged['2021'].str.contains(":")
                            & ~dfMerged['2023'].str.contains(":")]

        charactersToRemove = ['b', 'd', 'u', ' ']

        for character in charactersToRemove:
            dfMerged['2021'] = dfMerged['2021'].str.replace(character, '')
            dfMerged['2023'] = dfMerged['2023'].str.replace(character, '')

        dfMerged.replace({"geo": abreviationToCountry}, inplace=True)

        dfMerged['2023'] = dfMerged['2023'].astype(float)

        citizensTokeep = ["TOTAL", "NEU27_2020_FOR", "EU27_2020_FOR"]

        dfMerged = dfMerged[dfMerged['wstatus'] == "EMP"]
        dfMerged = dfMerged[dfMerged['citizen'].isin(citizensTokeep)]
        dfMerged = dfMerged[dfMerged['geo'] != "EA20"]
        dfMerged = dfMerged[dfMerged['geo'] != "EU27_2020"]

        abreviationToCitizen = {
            "TOTAL": "All",
            "NEU27_2020_FOR": "Non EU",
            "EU27_2020_FOR": "EU"
        }

        dfMerged.replace({"citizen": abreviationToCitizen}, inplace=True)

        dfMerged = dfMerged[['citizen', 'geo',
                             '2023']].groupby(['geo', 'citizen']).sum()

        dfMerged.reset_index(inplace=True)

        dfMerged['2023'] = round(dfMerged['2023'] / 10000, 2)

        dfMerged = dfMerged.sort_values(by=['2023'], ascending=False)

        dfMerged = dfMerged[dfMerged['citizen'] == "All"]

        dfMerged = dfMerged[['geo', '2023']]

        dfMerged = pd.merge(dfMerged,
                            self.demographyAnalysis.getDataSet(),
                            on=['geo'],
                            how='inner')

        dfMerged['population'] = round(dfMerged['population'] / 10000, 2)

        dfMerged['percentage'] = (dfMerged['2023'] *
                                  100) / dfMerged['population']

        dfMerged = dfMerged[['geo', 'percentage']]

        dfMerged.rename(columns={'percentage': 'numberOfMigrants'},
                        inplace=True)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
