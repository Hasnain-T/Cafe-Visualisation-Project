import pandas as pd
import os
from style import custom_border_message

file_path = "../data/raw_data.csv"

def transform_data(df):
    """
    Cleans extracted data by:
    - Assigning column names,
    - removing PIIs,
    - Handling missing & duplicate values, 
    - Standardising text fields
    """
    try:
        # Assign Column Names
        df.columns = [
        "Customer Name",
        "Drink",
        "Price",
        "Branch",
        "Payment Type",
        "Card Number",
        "Date"
]   
        custom_border_message("[INFO] Column names were assigned successfully.")
        
        # Remove PIIs
        df = df.drop(columns=["Customer Name", "Card Number"])
        custom_border_message("[INFO] Removed PII columns successfully.")

        # Remove duplicates
        # df = df.drop_duplicates()
        # custom_border_message("[INFO] Removed duplicate records.")

        # Standardise Column names
        for col in ["Drink", "Branch", "Payment Type"]:
            df[col] = df[col].str.title()
            custom_border_message("[INFO] Standardised text formatting.")
        
        # Prepare Numeric Price for DB
        # Create new column "price_num" by stripping '£' and converting to float
        df['Price_num'] = df['Price'].replace('£', '', regex=True).astype(float)
        custom_border_message("[INFO] Numeric price column 'Price_num' created for DB inserts.")

        # Convert Date column to datetime
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        custom_border_message("[INFO] Conerted 'Date' column to datetime format.")

        # At this point:
        # - df['Price'] still has £ for display/CSV
        # - df['Price_num'] is clean numeric for DB
        # - df['Date'] is proper datetime for DB
        
        return df

    except Exception as e:
        custom_border_message(f"[ERROR] Transformation failed: {e}")
        return None
    