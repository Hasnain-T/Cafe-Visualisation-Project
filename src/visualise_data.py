# Visualising the Data
# Run each cell in order 

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
# Average Drink Price Across Branches
# Group by Branch and Drink, take the average Price
avg_price = df.groupby(["Branch", "Drink"])["Price_num"].mean().unstack()

plt.figure(figsize=(12,7))
avg_price.plot(kind="bar", stacked=False, figsize=(12, 7))

plt.title("Average Drink Price Across Branches", fontsize=16)
plt.xlabel("Branch", fontsize=12)
plt.ylabel("Average Price (£)", fontsize=12)
plt.legend(title="Drink", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# %%
# Heatmap: Average Prices
avg_matrix = df.pivot_table(values="Price_num", index="Drink", columns="Branch", aggfunc="mean")
plt.figure(figsize=(10,6))
sns.heatmap(avg_matrix, annot=True, cmap="viridis", fmt=".2f")
plt.title("Averae Drink Price by Branch (Heatmap)")
plt.show()

# %%
payment_share = df["Payment Type"].value_counts()
plt.pie(payment_share, labels=payment_share.index, autopct="%1.1f%%", startangle=90)
plt.title("Payment Method as %")
plt.show()

# %%
# Branch vs Payment Type (Clustered Bar Chart)
branch_payment = df.groupby(["Branch", "Payment Type"])["Price_num"].sum().unstack()
branch_payment.plot(kind="bar", figsize=(10,6))
plt.title("Branch vs Payment Type = Total Sales")
plt.ylabel("Revenue (£)")
plt.show()

# %%
custom_border_message("[INFO] All visualisations generated successfully!")

