from abc import ABC, abstractmethod

# As CA requirement, Using abstraction for all ML models so all models share the same interface.

class BaseModel(ABC):

    @abstractmethod
    def train(self, X, y):
        # Fit the model on training data
        pass

    @abstractmethod
    def predict(self, X):
        # Return predictions for input X
        pass

    @abstractmethod
    def print_results(self, y_true, y_pred, label_name: str = ""):
        # Print accuracy and F1 score for given label
        pass