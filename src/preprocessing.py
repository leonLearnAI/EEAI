# from src.data_loader import load_Data
# TESTING CODE
# df = load_Data()
# print("rows:", len(df))
# print("columns:", len(df.columns))
# print("head:", df.head(5))

import pandas as pd
from config import Data_Path, Text_Cols, Label_Cols


def add_text_column(df: pd.DataFrame, out_col: str = "text") -> pd.DataFrame:
    """
    Create df['text'] by concatenating TEXT_COLS and doing minimal cleaning.
    - lowercase
    - strip
    - compress multiple whitespace into one space
    """
    # 1) Start with the first text column
    text = df[Text_Cols[0]].astype(str)
    # 2) Append remaining text columns
    for c in Text_Cols[1:]:
        text += " " + df[c].astype(str)
    text = text.str.lower().str.strip()
    # 3）collapse multiple spaces
    text = text.str.replace(r"\s+", " ", regex=True)
    # 4) Do not modify original df in-place, safer for debugging and reuse
    df2 = df.copy()
    df2[out_col] = text
    return df2
