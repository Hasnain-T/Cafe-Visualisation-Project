import pandas as pd
from style import custom_border_message


# Extract the data from the CSV
df = pd.read_csv("../data/raw_data.csv")

# Transform the data


# Load the data into local cleaned_data.csv


custom_border_message(df.to_string())