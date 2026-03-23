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
    return df[Label_Cols[0]].str.strip().copy()


def build_y23(df: pd.DataFrame) -> pd.Series:
    """Return combined labels for Type 2 and Type 3."""
    _require_columns(df, [Label_Cols[0], Label_Cols[1]])
    left = df[Label_Cols[0]].astype(str)
    right = df[Label_Cols[1]].astype(str)
    return (left + TYPE23_SEPARATOR + right).str.strip()


def build_y234(df: pd.DataFrame) -> pd.Series:
    """Return combined labels for Type 2, Type 3, and Type 4."""
    _require_columns(df, [Label_Cols[0], Label_Cols[1], Label_Cols[2]])
    l2 = df[Label_Cols[0]].astype(str)
    l3 = df[Label_Cols[1]].astype(str)
    l4 = df[Label_Cols[2]].astype(str)
    return (l2 + TYPE234_SEPARATOR + l3 + TYPE234_SEPARATOR + l4).str.strip()
