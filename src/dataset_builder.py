# from src.data_loader import load_Data
# from src.preprocessing import add_text_column
# TESTING CODE
# df = load_Data()
# df = add_text_column(df)

# print(df[["Ticket Summary", "Interaction content", "text"]].head(5))
# print("Empty text count:", (df["text"].str.len() == 0).sum())

from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from config import Text_Cols, Label_Cols, Test_Size, Random_State, Max_Features


@dataclass
class DataBundle:
    """
    Encapsulation object required by the CA:
    keep the model input format stable, so models don't change when data changes.

    - train_x/test_x: numeric feature matrices
    - train_y/test_y: labels in a consistent dict format
    - vectorizer: fitted vectorizer (so the same transformation is used for test/new data)
    """

    train_x: object
    train_y: object
    test_x: object
    test_y: object
    vectorizer: TfidfVectorizer


def build_databundle(df: pd.DataFrame) -> DataBundle:
    """
    Build the standardized dataset object.
    """
    if "text" not in df.columns:
        raise ValueError(
            "DataFrame must have a 'text' column. Please run add_text_column first."
        )
    # X is the cleaned text column
    X = df["text"].astype(str)
    # y columns ,keep them as strings
    y2 = df[Label_Cols[0]].astype(str)
    y3 = df[Label_Cols[1]].astype(str)
    y4 = df[Label_Cols[2]].astype(str)
    # Split once, so all labels align with the same indices
    X_train, X_test, y2_train, y2_test, y3_train, y3_test, y4_train, y4_test = (
        train_test_split(X, y2, y3, y4, test_size=Test_Size, random_state=Random_State)
    )
    # Vectorize text using TF-IDF
    vectorizer = TfidfVectorizer(max_features=Max_Features)
    train_x = vectorizer.fit_transform(X_train)
    test_x = vectorizer.transform(X_test)
    # Pack labels into a stable dict format
    train_y = {"type2": y2_train, "type3": y3_train, "type4": y4_train}
    test_y = {"type2": y2_test, "type3": y3_test, "type4": y4_test}

    return DataBundle(train_x, train_y, test_x, test_y, vectorizer)


if __name__ == "__main__":
    from src.data_loader import load_Data
    from src.preprocessing import add_text_column

    df0 = load_Data()
    df1 = add_text_column(df0)
    bundle = build_databundle(df1)
    print("train_x shape:", bundle.train_x.shape)
    print("test_x shape:", bundle.test_x.shape)
    print("train_y keys:", bundle.train_y.keys())
    print("Sample type2 labels:", bundle.train_y["type2"].head(5).tolist())
