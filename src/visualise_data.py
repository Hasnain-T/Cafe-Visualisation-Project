# %% Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from style import custom_border_message

#  %% Load the cleaned data
file_path = ("../data/cleaned_data.csv")
df = pd.read_csv(file_path)

custom_border_message("[Info] Loaded clean data for visualisation.")

# %% Optional: set seaborn style
sns.set_theme(style="whitegrid")

# %% Total Sales by Drink
plt.figure(figsize=(10,6))
drink_revenue = df.groupby("Drink")["Price_num"].sum().sort_values(ascending=False)
sns.barplot(x=drink_revenue.index, y=drink_revenue.values, palette="viridis")
plt.title("Total Revenue per Drink")
plt.xlabel("Drink")
plt.ylabel("£ Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
# Payment Type Distribution
plt.figure(figsize=(8,5))
payment_method = df["Payment Type"].value_counts()
sns.barplot(x=payment_method.index, y=payment_method.values, palette="coolwarm")
plt.title("Payment Type Distribution")
plt.ylabel("Number of Transactions")
plt.xlabel("Payment Type")
plt.tight_layout()
plt.show()
# %%
# Total Sales per Branch
plt.figure(figsize=(10,6))
branch_sales = df.groupby("Branch")['Price_num'].sum().sort_values(ascending=False)
sns.barplot(x=branch_sales.index, y=branch_sales.values, palette="magma")
plt.title("Total Sales per Branch")
plt.ylabel("Revenue (£)")
plt.xlabel("Branch")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# %%
# Sales Over Time
plt.figure(figsize=(12,6))
df["Date"] = pd.to_datetime(df['Date'])
time_sales = df.groupby("Date")["Price_num"].sum()
time_sales.plot(marker='o')
plt.title("Sales Over Time")
plt.ylabel("Revenue (£)")
plt.xlabel("Date")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# %%
custom_border_message("[INFO] All visualisations generated successfully!")

