"""Utility helpers for result formatting and export."""

from pathlib import Path


def flatten_results(results: dict) -> list[dict]:
	rows = []
	for key, row in results.items():
		if isinstance(row, dict):
			rows.append(
				{
					"task_key": key,
					"task": row.get("task", key),
					"accuracy": row.get("accuracy"),
					"f1_macro": row.get("f1_macro"),
				}
			)
	return rows


def export_csv(rows: list[dict], out_path: str | Path) -> None:
	pass
