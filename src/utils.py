"""Utility helpers for result formatting and export."""

import csv
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
	out_path = Path(out_path)
	out_path.parent.mkdir(parents=True, exist_ok=True)
	if not rows:
		out_path.write_text("", encoding="utf-8")
		return

	fieldnames = list(rows[0].keys())
	with out_path.open("w", newline="", encoding="utf-8") as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(rows)
