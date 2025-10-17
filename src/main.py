import pandas as pd
from style import custom_border_message
from extract import extract_csv
from transform import transform_data

file_path = "../data/raw_data.csv"

if __name__ == "__main__":

    # Extract the data from the CSV
    df_raw = extract_csv(file_path)
    custom_border_message(df_raw.to_string())
    
    # Transform the data
    if df_raw is not None:
        df_clean = transform_data(df_raw)
        custom_border_message("[INFO] Transformation Complete.")
        # print(df_clean.head())
    else: 
        custom_border_message("[ERROR] Extraction Failed. Transformation Skipped")



# Load the data into local cleaned_data.csv
