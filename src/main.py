import pandas as pd
from style import custom_border_message
from extract import extract_csv
from transform import transform_data
from load import load_clean_data

file_path = "../data/raw_data.csv"

if __name__ == "__main__":

    # Extract the data from the CSV
    df_raw = extract_csv(file_path)
    custom_border_message(df_raw.to_string())
    
    # Transform the data
    if df_raw is not None:
        df_clean = transform_data(df_raw)
        if df_clean is not None:
            custom_border_message("[INFO] Transformation Complete.")

            # Load the data into local cleaned_data.csv
            load_success = load_clean_data(df_clean)
            if load_success:
                custom_border_message("[INFO] Data successfully saved to clean_data.csv")
                # Print clean data in Terminal
                custom_border_message(df_clean.to_string())
            else: 
                custom_border_message("[ERROR] Failed to save cleaned data.")
        else:
            custom_border_message("[ERROR] Transformation failed. Skipping load step.")
        
    else: 
        custom_border_message("[ERROR] Extraction Failed. Transformation Skipped")
