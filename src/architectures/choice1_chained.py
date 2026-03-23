"""Choice 1 architecture: chained multi-output experiments."""

from typing import Any

from src.evaluation import compute_metrics
from src.models.logistic_regression import LogisticRegression
from src.models.random_forest import RandomForest


def _get_model(model_name: str):
	if model_name == "rf":
		return RandomForest()
	if model_name == "lr":
		return LogisticRegression()
	raise ValueError(f"Unsupported model: {model_name}")


def run_type2_experiment(bundle: Any, model_name: str = "rf") -> dict:
	pass


def run_type23_experiment(bundle: Any, model_name: str = "rf") -> dict:
	pass


def run_type234_experiment(bundle: Any, model_name: str = "rf") -> dict:
	pass
