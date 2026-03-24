"""Choice 2 architecture: hierarchical modelling scaffold."""

from collections import defaultdict
from pathlib import Path
from typing import Any

from src.evaluation import compute_metrics
from src.models.logistic_regression import LogisticRegression
from src.models.random_forest import RandomForest

MIN_BRANCH_SAMPLES = 2


def _new_branch_metric(label: str, train_samples: int, status: str, warning: str = "") -> dict:
	return {
		"label": label,
		"train_samples": train_samples,
		"status": status,
		"warning": warning,
	}


def _new_path_metric(path_key: str, train_samples: int, status: str, warning: str = "") -> dict:
	return {
		"path": path_key,
		"train_samples": train_samples,
		"status": status,
		"warning": warning,
	}


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
	branch_summary: dict[str, dict] = {}
	warnings: list[str] = []

	for label in sorted(branches.keys()):
		indices = branches[label]
		sample_count = len(indices)
		if sample_count == 0:
			msg = f"type3 branch skipped for '{label}' because it is empty"
			warnings.append(msg)
			branch_summary[label] = _new_branch_metric(
				label,
				sample_count,
				"skipped",
				warning=msg,
			)
			continue
		if sample_count < MIN_BRANCH_SAMPLES:
			msg = f"type3 branch skipped for '{label}' due to low samples ({sample_count})"
			warnings.append(msg)
			branch_summary[label] = _new_branch_metric(
				label,
				sample_count,
				"skipped_low_sample",
				warning=msg,
			)
			continue
		branch_summary[label] = _new_branch_metric(label, sample_count, "placeholder")

	return {"branches": branch_summary, "warnings": warnings}


def split_by_type2_type3(y2, y3) -> dict[tuple[str, str], list[int]]:
	groups: dict[tuple[str, str], list[int]] = defaultdict(list)
	for idx in y2.index:
		groups[(str(y2.loc[idx]), str(y3.loc[idx]))].append(idx)
	return dict(groups)


def run_type4_paths(bundle: Any, model_name: str = "rf") -> dict:
	paths = split_by_type2_type3(bundle.train_y["type2"], bundle.train_y["type3"])
	path_summary: dict[str, dict] = {}
	warnings: list[str] = []

	for key in sorted(paths.keys()):
		indices = paths[key]
		path_key = f"{key[0]}->{key[1]}"
		sample_count = len(indices)
		if sample_count == 0:
			msg = f"type4 path skipped for '{path_key}' because it is empty"
			warnings.append(msg)
			path_summary[path_key] = _new_path_metric(
				path_key,
				sample_count,
				"skipped",
				warning=msg,
			)
			continue
		if sample_count < MIN_BRANCH_SAMPLES:
			msg = f"type4 path skipped for '{path_key}' due to low samples ({sample_count})"
			warnings.append(msg)
			path_summary[path_key] = _new_path_metric(
				path_key,
				sample_count,
				"skipped_low_sample",
				warning=msg,
			)
			continue
		path_summary[path_key] = _new_path_metric(path_key, sample_count, "placeholder")

	return {"paths": path_summary, "warnings": warnings}


def aggregate_choice2(bundle: Any, model_name: str = "rf") -> dict:
	type2_stage = run_type2_stage(bundle, model_name=model_name)
	type3_stage = run_type3_branches(bundle, model_name=model_name)
	type4_stage = run_type4_paths(bundle, model_name=model_name)
	all_warnings = type3_stage["warnings"] + type4_stage["warnings"]
	return {
		"type2_stage": type2_stage,
		"type3_branches": type3_stage["branches"],
		"type4_paths": type4_stage["paths"],
		"warnings": all_warnings,
	}


def print_choice2_summary(summary: dict) -> None:
	print("Choice2 Results (Hierarchical Modelling)")
	print("type2:", summary["type2_stage"]["accuracy"], summary["type2_stage"]["f1_macro"])
	print("type3 branches:", len(summary["type3_branches"]))
	print("type4 paths:", len(summary["type4_paths"]))
	print("warnings:", len(summary["warnings"]))


__all__ = [
	"run_type2_stage",
	"split_by_type2",
	"run_type3_branches",
	"split_by_type2_type3",
	"run_type4_paths",
	"aggregate_choice2",
	"print_choice2_summary",
]


if __name__ == "__main__":
	from src.data_loader import load_Data
	from src.dataset_builder import build_databundle
	from src.preprocessing import add_text_column

	df = add_text_column(load_Data(path=Path("data/AppGallery.csv")))
	bundle = build_databundle(df)
	result = aggregate_choice2(bundle, model_name="rf")
	print_choice2_summary(result)
