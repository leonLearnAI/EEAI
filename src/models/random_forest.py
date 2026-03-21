from sklearn.ensemble import RandomForestClassifier

from src.models.base_model import BaseModel
from src.evaluation import compute_metrics


class RandomForest(BaseModel):

    def __init__(self, n_estimators=100, random_state=10):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators, random_state=random_state
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def print_results(self, y_true, y_pred, label_name: str = ""):
        metrics = compute_metrics(y_true, y_pred)
        header = f"[RandomForest] {label_name}".strip()
        print(f"\n{header}")
        print(f"  Accuracy : {metrics['accuracy']:.4f}")
        print(f"  F1 Macro : {metrics['f1_macro']:.4f}")

    def evaluate(self, X_test, y_test) -> dict:
        # Predict on test data and return evaluation metrics
        y_pred = self.predict(X_test)
        return compute_metrics(y_test, y_pred)
