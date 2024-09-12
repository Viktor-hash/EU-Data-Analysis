from profile.Profile import Profile
import pandas as pd


# Data set analysis class base class
class DataSetBase:

    def __init__(self, filePath: str, profile: Profile):
        self.filePath = filePath
        self.dataSetTsv = pd.read_csv(filePath, sep='\t')
        self.profile = profile
