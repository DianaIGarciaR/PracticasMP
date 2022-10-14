from abc import ABC, abstractmethod
class DatasetSummary(ABC):
    @abstractmethod
    def list_features(self):
        pass
    @abstractmethod
    def list_labels(self):
        pass
    @abstractmethod
    def count_categorical(self):
        pass
    @abstractmethod
    def count_numerical(slef):
        pass
    @abstractmethod
    def statistics(self):
        pass
    @abstractmethod
    def histogram(self, feature, bins=10):
        pass