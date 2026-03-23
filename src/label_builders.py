"""Helpers for building Type2/Type23/Type234 labels."""

import pandas as pd

from config import Label_Cols

TYPE23_SEPARATOR = "__"
TYPE234_SEPARATOR = "__"


def _require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    pass
