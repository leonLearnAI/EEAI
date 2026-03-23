"""Choice 1 architecture: chained multi-output experiments."""

from collections import OrderedDict
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


def _result_row(task_name: str, metrics: dict) -> dict:
	return {
		"task": task_name,
		"accuracy": metrics["accuracy"],
		"f1_macro": metrics["f1_macro"],
	}


def _summary_dict(type2_result: dict, type23_result: dict, type234_result: dict) -> dict:
	return OrderedDict(
		[
			("type2", type2_result),
			("type23", type23_result),
			("type234", type234_result),
		]
	)


def run_type2_experiment(bundle: Any, model_name: str = "rf") -> dict:
	model = _get_model(model_name)
	y_true = bundle.test_y["type2"]
	model.train(bundle.train_x, bundle.train_y["type2"])
	y_pred = model.predict(bundle.test_x)
	metrics = compute_metrics(y_true, y_pred)
	return _result_row("type2", metrics)


def run_type23_experiment(bundle: Any, model_name: str = "rf") -> dict:
	model = _get_model(model_name)
	y_true = bundle.test_y["type23"]
	model.train(bundle.train_x, bundle.train_y["type23"])
	y_pred = model.predict(bundle.test_x)
	metrics = compute_metrics(y_true, y_pred)
	return _result_row("type23", metrics)


def run_type234_experiment(bundle: Any, model_name: str = "rf") -> dict:
	model = _get_model(model_name)
	y_true = bundle.test_y["type234"]
	model.train(bundle.train_x, bundle.train_y["type234"])
	y_pred = model.predict(bundle.test_x)
	metrics = compute_metrics(y_true, y_pred)
	return _result_row("type234", metrics)


def run_choice1(bundle: Any, model_name: str = "rf") -> dict:
	type2_result = run_type2_experiment(bundle, model_name=model_name)
	type23_result = run_type23_experiment(bundle, model_name=model_name)
	type234_result = run_type234_experiment(bundle, model_name=model_name)
	return _summary_dict(type2_result, type23_result, type234_result)


__all__ = [
	"run_type2_experiment",
	"run_type23_experiment",
	"run_type234_experiment",
	"run_choice1",
]
