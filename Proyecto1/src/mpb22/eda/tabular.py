import pandas as pd
import numpy as np
from src.mpb22.eda.base import DatasetSummary
class TabularDatasetSummary(DatasetSummary):
    def __init__(self, filepath, features=None, labels=None):
        self.filepath=filepath
        self.features=features
        self.labels=labels
    def list_features(self):
        try:
            if self.features !=None and self.labels !=None:
                self.features=set(self.features)^set(self.labels)
                df = pd.read_csv(self.filepath,names=self.features)
            else:
                df = pd.read_csv(self.filepath,names=self.features)
            return self.features
        except ValueError:
            print("Fail: ",ValueError)
    def list_labels(self):
        try:
            return self.labels
        except ValueError:
            print("Fail: ",ValueError)
    def count_categorical(self):
        try:
            df = pd.read_csv(self.filepath)
            categorical = df.select_dtypes(exclude=['number']).copy()
            size = len(categorical.columns.values)
            return size
        except ValueError:
            print("Fail: ",ValueError)
    def count_numerical(self):
        try:
            df = pd.read_csv(self.filepath)
            number = df.select_dtypes(include=['number']).copy()
            size = len(number.columns.values)
            return size
        except ValueError:
            print("Fail: ",ValueError)
    def statistics(self):
        try:
            df = pd.read_csv(self.filepath)
            number = df.select_dtypes(include=['number']).copy()
            element=number.columns.values
            dict_feature={}
            for i in df.columns:
                if i in element:
                    dict_statistics={
                        "type": "numerical",
                        "mean": df[i].mean(),
                        "mode": list(df[i].mode()),
                        "median": df[i].median(),
                        "std": df[i].std(),
                        "n_null":df[i].isnull().sum(),
                        "n_total": df[i].count()
                    }
                else:
                    dict_statistics={
                        "type": "categorical",
                        "mean": None,
                        "mode": list(df[i].mode()),
                        "median": None,
                        "std": None,
                        "n_null": df[i].isnull().sum(),
                        "n_total": df[i].count()
                    }
                dict_feature[i] = dict_statistics
            return dict_feature
        except ValueError:
            print("Fail: ",ValueError)
    def histogram(self,feature,bins=10):
        try:
            df = pd.read_csv(self.filepath)
            if df[feature].dtype == 'object':
                return df[feature].value_counts().index, df[feature].value_counts().values
            else:
                x, y = np.histogram(df[feature], bins=bins)
                y = y[:-1]
                return y, x
            print(hist)
        except ValueError:
            print("Fail: ",ValueError)