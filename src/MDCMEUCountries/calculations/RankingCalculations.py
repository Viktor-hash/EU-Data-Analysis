from profile.Profile import Profile
import pandas as pd
from dataSetsLib import CostOfLivingAnalysis
from dataSetsLib import MigrantsAnalysis
from dataSetsLib import TaxAnalysis
from dataSetsLib import EarningsAnalysis
from profile.criterias import Preference
from sklearn.preprocessing import normalize


# Data set analysis class base class
class RankingCalculations:

    def __init__(
        self,
        profile: Profile,
        dataSetsToAnalyze: list,
    ):
        self.profile = profile
        self.dataSetsDic = {}
        self.dataSetsToAnalyze = dataSetsToAnalyze
        self.dfMerged = None
        self.createDataSetDic()
        self.mergeDataSets()
        self.applyPreferences()
        self.normalize()
        self.applyWeights()
        self.createRanking()

    def createDataSetDic(self):
        for dataSet in self.dataSetsToAnalyze:
            # Economic analysis
            if (dataSet == 'costOfLiving'):
                self.dataSetsDic[dataSet] = CostOfLivingAnalysis(
                    self.profile).getDataSet()
            elif (dataSet == 'taxs'):
                self.dataSetsDic[dataSet] = TaxAnalysis(
                    self.profile).getDataSet()
            elif (dataSet == 'earnings'):
                self.dataSetsDic[dataSet] = EarningsAnalysis(
                    self.profile).getDataSet()
            # Safety and Security

            # Culture and lifestyle
            elif (dataSet == 'migrants'):
                self.dataSetsDic[dataSet] = MigrantsAnalysis(
                    self.profile).getDataSet()

            # Education and Healthcare

            # Environment and Climate

            # Visa and Immigration Requirements

            # Infrastructure and Transportation

            # Personal Freedoms

    def getDataSetDic(self):
        return self.dataSetsDic

    def mergeDataSets(self):
        dfMerged = self.dataSetsDic[self.dataSetsToAnalyze[0]]['geo']
        for dataSet in self.dataSetsToAnalyze:
            print(self.dataSetsDic[dataSet])
            dfMerged = pd.merge(dfMerged,
                                self.dataSetsDic[dataSet],
                                on=['geo'],
                                how='inner')

        self.dfMerged = dfMerged

    def applyPreferences(self):
        for dataSet in self.dataSetsToAnalyze:
            preference = self.profile.getPreferences(dataSet).getPreference()
            if (preference == Preference.MID):
                mean = self.dfMerged[dataSet].mean()
                self.dfMerged[dataSet] = 1 / abs(self.dfMerged[dataSet] - mean)
            if (preference == Preference.LOW):
                self.dfMerged[dataSet] = 1 / self.dfMerged[dataSet]

    def normalize(self):
        self.dfMerged[self.dataSetsToAnalyze] = normalize(
            self.dfMerged[self.dataSetsToAnalyze].values, axis=0)

    def applyWeights(self):
        for dataSet in self.dataSetsToAnalyze:
            weight = self.profile.getPreferences(dataSet).getWeight()
            self.dfMerged[dataSet] = self.dfMerged[dataSet].mul(weight.value)

    def createRanking(self):
        # Add columns together to create a new column 'Ranking'
        self.dfMerged['Ranking'] = self.dfMerged[self.dataSetsToAnalyze].sum(
            axis=1)

        # Sort the data by the 'Ranking' column in descending order
        self.dfMerged = self.dfMerged.sort_values(by='Ranking',
                                                  ascending=False)

    def getRanking(self):
        return self.dfMerged[['geo', 'Ranking']]
