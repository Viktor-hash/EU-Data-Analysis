import pandas as pd
from enum import Enum

abreviationToCountry = {
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CZ": "Czechia",
    "DK": "Denmark",
    "DE": "Germany",
    "EE": "Estonia",
    "IE": "Ireland",
    "EL": "Greece",
    "ES": "Spain",
    "FR": "France",
    "HR": "Croatia",
    "IT": "Italy",
    "CY": "Cyprus",
    "LV": "Latvia",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "HU": "Hungary",
    "MT": "Malta",
    "NL": "Netherlands",
    "AT": "Austria",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SI": "Slovenia",
    "SK": "Slovakia",
    "FI": "Finland",
    "SE": "Sweden",
    "IS": "Iceland",
    "NO": "Norway",
    "CH": "Switzerland",
    "UK": "United Kingdom",
    "BA": "Bosnia and Herzegovina",
    "ME": "Montenegro",
    "MD": "Moldova",
    "MK": "North Macedonia",
    "GE": "Georgia",
    "AL": "Albania",
    "RS": "Serbia",
    "TR": "Turkiye",
    "HK": "Hong Kong"
}


class Tolerance(Enum):
    MAX = 1.0
    HIGH = 0.75
    MEDIUM = 0.50
    LOW = 0.25


class Sex(Enum):
    MALE = 0
    FEMALE = 1


class Profile:

    def __init__(self, unsafetyTolerance: Tolerance,
                 migrantsTolerance: Tolerance, age: int, sex: Sex,
                 countryOfOrigin: str, healthCareNeed: Tolerance):
        self.age = age
        self.migrantsTolerance = migrantsTolerance
        self.sex = sex
        self.countryOfOrigin = countryOfOrigin
        self.unsafetyTolerance = unsafetyTolerance
        self.dicOfMatchingCountries = {}
        self.healthCareNeed = healthCareNeed

    def addMatchingCountry(self, analysis: str, countries: list):
        self.dicOfMatchingCountries[analysis] = countries

    def getMatchingCountries(self):
        return self.dicOfMatchingCountries


# Data set analysis class base class
class DataSetAnalysis:

    def __init__(self, filePath: str, profile: Profile):
        self.filePath = filePath
        self.dataSetTsv = pd.read_csv(filePath, sep='\t')
        self.profile = profile


class HealthAnalysis(DataSetAnalysis):

    def __init__(self, profile: Profile):
        super().__init__(
            'C:\data analysis best country in europe\demo_pjan_tabular.tsv\demo_pjan_tabular.tsv',
            profile)


# Age analysis class that creates the data set
class AgeAnalysis(DataSetAnalysis):

    def __init__(self, profile: Profile):
        super().__init__(
            'C:\data analysis best country in europe\demo_pjan_tabular.tsv\demo_pjan_tabular.tsv',
            profile)
        self.CreateDataSet()


# Demography analysis class that creates the data set
class DemographyAnalysis(DataSetAnalysis):

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


# Migrants analysis class that creates the data set and filters it by the migrants tolerance
class MigrantsAnalysis(DataSetAnalysis):

    def __init__(self, profile: Profile):
        super().__init__(
            'C:\data analysis best country in europe\estat_lfsa_pfganwsm.tsv\estat_lfsa_pfganwsm.tsv',
            profile)
        self.demographyAnalysis = DemographyAnalysis(profile)
        self.CreateDataSet()

    # Create the data set by merging the demography data set with the migrants data set
    # The data set is then filtered by the migrants tolerance on the percentage of migrants
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

        self.dfMerged = dfMerged

    def addMatchingCountriesToProfile(self):
        filteredDfMerged = self.dfMerged[
            self.dfMerged['percentage'] <= self.dfMerged['percentage'].
            quantile(self.profile.migrantsTolerance.value)]
        listMatchingCountries = filteredDfMerged['geo'].unique()
        self.profile.addMatchingCountry('migrants', listMatchingCountries)


jeanneProfile = Profile(
    Tolerance.LOW,
    Tolerance.LOW,
    24,
    Sex.FEMALE,
    'Hong Kong',
)

MigrantsAnalysis(jeanneProfile).addMatchingCountriesToProfile()

DemographyAnalysis(jeanneProfile)

matchingCountries = jeanneProfile.getMatchingCountries()

for analysis in matchingCountries:
    print(analysis)
    print(matchingCountries[analysis])
