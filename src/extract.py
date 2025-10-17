import pandas as pd
import os
from style import custom_border_message

file_path = "../data/raw_data.csv"

# Extract the data from the CSV
def extract_csv(file_path: str):
    """
    Extracts data from a CSV file and returns a pandas DataFrame.
    Logs success or failure messages.
    """
    try:
        df = pd.read_csv(file_path, header=None, sep=r"\s+", engine="python")

        # Debugging line — check number of detected columns
        print(f"[DEBUG] Columns detected: {df.shape[1]}")
        
        custom_border_message(f"[INFO] Successfully extracted from {file_path}")
        return df
    except Exception as e:
        custom_border_message(f"[ERROR] Failed to extract data: {e}")
        return None