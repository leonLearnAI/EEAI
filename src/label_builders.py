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
    """Return labels for Type 2 classification."""
    _require_columns(df, [Label_Cols[0]])
    return df[Label_Cols[0]].copy()


def build_y23(df: pd.DataFrame) -> pd.Series:
    """Return combined labels for Type 2 and Type 3."""
    _require_columns(df, [Label_Cols[0], Label_Cols[1]])
    return df[Label_Cols[0]] + TYPE23_SEPARATOR + df[Label_Cols[1]]


def build_y234(df: pd.DataFrame) -> pd.Series:
    pass
