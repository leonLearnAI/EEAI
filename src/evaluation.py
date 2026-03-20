from sklearn.metrics import accuracy_score, f1_score

def compute_metrics(y_true, y_pred) -> dict:
    # Returns accuracy and macro F1 score for a given label
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_macro": f1_score(y_true, y_pred, average="macro", zero_division=0),
    }