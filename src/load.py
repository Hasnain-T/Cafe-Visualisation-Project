import pandas as pd
import os
from style import custom_border_message

file_path = "../data/raw_data.csv"

def load_clean_data(df, output_path="../data/cleaned_data.csv"):
    """
    Saves the Cleaned DataFrame to a CSV file.
    This acts as a Checkpoint before loading into database.
    """
    try: 
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the cleaned DataFrame
        df.to_csv(output_path, index=False)
        custom_border_message(f"[INFO] Clean data successfully saved to {output_path}")
        return True
    
    except Exception as e:
        custom_border_message(f"[ERROR] Failed to save clean data: {e}")
        return False