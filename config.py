# config.py
from pathlib import Path

# 1) Data directory, use ~ and expand to an absolute path
Data_Dir = Path("~/EEAI/data").expanduser()
# 2) Which CSV to use, switch this name to test another dataset
# CSV_file = "Purchasing.csv"
CSV_file = "AppGallery.csv"
Data_Path = Data_Dir / CSV_file
# 3) Text columns used to build the final model input
Text_Cols = ["Ticket Summary", "Interaction content"]
# 4) Target label columns
Label_Cols = ["Type 2", "Type 3", "Type 4"]
# 5) Train/test split settings
Test_Size = 0.2  # 20% test set
Random_State = 42  # fixed seed for reproducibility
# 6) Vectorizer settings (TF-IDF)
Max_Features = 20000

print("Using CSV:", Data_Path)
