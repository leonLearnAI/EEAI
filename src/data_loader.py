import pandas as pd
from config import Data_Path, Text_Cols, Label_Cols


def load_Data(path=Data_Path) -> pd.DataFrame:
    """
    Load CSV and validate required columns.
    Only responsibilities:
    1) read csv
    2) check required columns exist
    3) fill missing text with ""
    """

    df = pd.read_csv(path)

    request_cols = Text_Cols + Label_Cols
    missing = [c for c in request_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}\n found columns: {df.columns}")
    # Ensure text columns are string and fill missing with ""
    for c in Text_Cols:
        df[c] = df[c].fillna("").astype(str)
    # Ensure label columns are strings
    for c in Label_Cols:
        df[c] = df[c].fillna("").astype(str)

    return df
