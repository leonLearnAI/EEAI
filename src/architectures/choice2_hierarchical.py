"""Choice 2 architecture: hierarchical modelling scaffold."""

from collections import defaultdict
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


def run_type2_stage(bundle: Any, model_name: str = "rf") -> dict:
	model = _get_model(model_name)
	y_true = bundle.test_y["type2"]
	model.train(bundle.train_x, bundle.train_y["type2"])
	y_pred = model.predict(bundle.test_x)
	metrics = compute_metrics(y_true, y_pred)
	return {
		"task": "type2",
		"accuracy": metrics["accuracy"],
		"f1_macro": metrics["f1_macro"],
	}


def split_by_type2(y2) -> dict[str, list[int]]:
	groups: dict[str, list[int]] = defaultdict(list)
	for idx, label in y2.items():
		groups[str(label)].append(idx)
	return dict(groups)


def run_type3_branches(bundle: Any, model_name: str = "rf") -> dict:
	branches = split_by_type2(bundle.train_y["type2"])
	branch_summary = {}
	for label, indices in branches.items():
		branch_summary[label] = {
			"train_samples": len(indices),
			"status": "placeholder",
		}
	return branch_summary


def split_by_type2_type3(y2, y3) -> dict[tuple[str, str], list[int]]:
	groups: dict[tuple[str, str], list[int]] = defaultdict(list)
	for idx in y2.index:
		groups[(str(y2.loc[idx]), str(y3.loc[idx]))].append(idx)
	return dict(groups)


def run_type4_paths(bundle: Any, model_name: str = "rf") -> dict:
	paths = split_by_type2_type3(bundle.train_y["type2"], bundle.train_y["type3"])
	path_summary = {}
	for key, indices in paths.items():
		path_summary[f"{key[0]}->{key[1]}"] = {
			"train_samples": len(indices),
			"status": "placeholder",
		}
	return path_summary
