"""Controller layer for orchestrating data and architecture runs."""

from pathlib import Path

from src.architectures.choice1_chained import run_choice1 as run_choice1_arch
from src.data_loader import load_Data
from src.dataset_builder import build_databundle
from src.preprocessing import add_text_column
from src.utils import export_csv, flatten_results


def build_pipeline_data(data_path: str | Path | None = None):
	df = load_Data(path=data_path) if data_path else load_Data()
	df = add_text_column(df)
	return build_databundle(df)


def run_choice1(
	model_name: str = "rf",
	data_path: str | Path | None = None,
	export_path: str | Path | None = None,
) -> dict:
	bundle = build_pipeline_data(data_path=data_path)
	result = run_choice1_arch(bundle, model_name=model_name)
	if export_path:
		rows = flatten_results(result)
		export_csv(rows, export_path)
	return result


def run_architecture(
	arch: str,
	model_name: str = "rf",
	data_path: str | Path | None = None,
	export_path: str | Path | None = None,
) -> dict:
	if arch == "choice1":
		return run_choice1(
			model_name=model_name,
			data_path=data_path,
			export_path=export_path,
		)
	if arch == "choice2":
		return {"message": "Choice2 is not implemented yet."}
	raise ValueError(f"Unsupported architecture: {arch}")


__all__ = ["build_pipeline_data", "run_choice1", "run_architecture"]
