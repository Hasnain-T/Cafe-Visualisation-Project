import pandas as pd
from style import custom_border_message
from extract import extract_csv
from transform import transform_data
from load import load_clean_data
from load_to_db import load_to_db

file_path = "../data/raw_data.csv"

if __name__ == "__main__":

    # Extract the data from the CSV
    df_raw = extract_csv(file_path)
    if df_raw is not None:
        custom_border_message(df_raw.to_string())
    else:
        custom_border_message("[ERROR] Extraction Failed. Transformation skipped.")
        exit(1)
    
    # Transform the data
    
    df_clean = transform_data(df_raw)
    if df_clean is None:
        custom_border_message("[ERROR] Transformation failed. Skipping load step")
        exit(1)
        
    custom_border_message("[INFO] Transformation Complete.")

    # Load the data into local cleaned_data.csv
    load_success = load_clean_data(df_clean)
    if load_success:
        custom_border_message("[INFO] Data successfully saved to clean_data.csv")
    else:
        custom_border_message("[ERROR] Failed to save cleaned_data.csv")

    # Load to PostgreSQL DB    
    db_success = load_to_db(df_clean)
    if db_success:
        custom_border_message("[INFO] Data successfully loaded into PostgreSQL.")
    else:
        custom_border_message("[ERROR] Failed to load data into PostgreSQL")

    # Print clean data in Terminal
    clean_display_df = df_clean.drop(columns=['Price_num'], errors='ignore')
    custom_border_message("[INFO] Final Cleaned Data Preview:")
    custom_border_message(clean_display_df.to_string(index=False))

