from dataSetsLib.DataSetBase import DataSetBase
from profile.Profile import Profile
from .constants.CountriesDic import abreviationToCountry
from dataSetsLib.DemographyAnalysis import DemographyAnalysis
import pandas as pd


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

        print(self.dataSetTsv)

        self.dataSetTsv.drop(self.dataSetTsv.columns[[0]],
                             axis=1,
                             inplace=True)

        dfMerged = pd.concat([dataSetTsvLeft, self.dataSetTsv], axis=1)

        self.dfMerged = dfMerged

    def getDataSet(self):
        return self.dfMerged
