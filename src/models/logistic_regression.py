from sklearn.linear_model import LogisticRegression as SklearnLR

from src.models.base_model import BaseModel
from src.evaluation import compute_metrics


class LogisticRegression(BaseModel):

    def __init__(self, max_iter=1000, random_state=10):
        self.model = SklearnLR(max_iter=max_iter, random_state=random_state)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def print_results(self, y_true, y_pred, label_name: str = ""):
        metrics = compute_metrics(y_true, y_pred)
        header = f"[LogisticRegression] {label_name}".strip()
        print(f"\n{header}")
        print(f"  Accuracy : {metrics['accuracy']:.4f}")
        print(f"  F1 Macro : {metrics['f1_macro']:.4f}")

    def evaluate(self, X_test, y_test) -> dict:
        # Predict on test data and return evaluation metrics
        y_pred = self.predict(X_test)
        return compute_metrics(y_test, y_pred)
