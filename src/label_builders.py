"""Helpers for building Type2/Type23/Type234 labels."""

import pandas as pd

from config import Label_Cols

TYPE23_SEPARATOR = "__"
TYPE234_SEPARATOR = "__"


def _require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns for label building: {missing}")


def build_y2(df: pd.DataFrame) -> pd.Series:
    pass
