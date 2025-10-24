# src/cafe_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------
# Load cleaned data
# --------------------------
file_path = "../data/cleaned_data.csv"
df = pd.read_csv(file_path)

# Strip any whitespace from column names
df.columns = [col.strip() for col in df.columns]

st.set_page_config(page_title="Cafe Sales Dashboard", layout="wide")
st.title("☕ Cafe Sales Dashboard")
st.markdown("---")

# --------------------------
# KPI Cards
# --------------------------
total_revenue = df["Price_num"].sum()
total_orders = len(df)
avg_price = df["Price_num"].mean()
num_branches = df["Branch"].nunique()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric(label="💰 Total Revenue (£)", value=f"{total_revenue:,.2f}")
kpi2.metric(label="🛒 Total Orders", value=total_orders)
kpi3.metric(label="☕ Average Drink Price (£)", value=f"{avg_price:,.2f}")
kpi4.metric(label="🏬 Number of Branches", value=num_branches)

st.markdown("---")

# --------------------------
# Preprocess Data for Charts
# --------------------------

# 1. Total Sales by Drink
drink_revenue = df.groupby("Drink")["Price_num"].sum().sort_values(ascending=False).reset_index()

# 2. Payment Type Distribution
payment_dist = df["Payment Type"].value_counts().reset_index()
payment_dist.columns = ["Payment Type", "Count"]

# 3. Total Sales per Branch
branch_sales = df.groupby("Branch")["Price_num"].sum().sort_values(ascending=False).reset_index()

# 4. Sales Over Time
df["Date"] = pd.to_datetime(df["Date"])
time_sales = df.groupby("Date")["Price_num"].sum().reset_index()

# 5. Average Drink Price Across Branches (Stacked Bar)
avg_price = df.groupby(["Branch", "Drink"])["Price_num"].mean().unstack().reset_index()

# 6. Heatmap: Average Prices
avg_matrix = df.pivot_table(values="Price_num", index="Drink", columns="Branch", aggfunc="mean")

# 7. Payment Method Pie
payment_share = df["Payment Type"].value_counts().reset_index()
payment_share.columns = ["Payment Type", "Count"]

# 8. Branch vs Payment Type
branch_payment = df.groupby(["Branch", "Payment Type"])["Price_num"].sum().unstack().fillna(0).reset_index()

# --------------------------
# Layout: 3x3 grid using columns
# --------------------------

# Row 1
cols = st.columns(3)
with cols[0]:
    fig1 = px.bar(drink_revenue, x="Drink", y="Price_num", color="Drink", title="💰 Total Revenue per Drink")
    st.plotly_chart(fig1, use_container_width=True)

with cols[1]:
    fig3 = px.bar(branch_sales, x="Branch", y="Price_num", color="Branch", title="🏬 Total Sales per Branch")
    st.plotly_chart(fig3, use_container_width=True)

with cols[2]:
    fig4 = px.line(time_sales, x="Date", y="Price_num", title="📈 Sales Over Time", markers=True)
    st.plotly_chart(fig4, use_container_width=True)

# Row 2
cols2 = st.columns(3)
with cols2[0]:
    fig5 = go.Figure()
    for drink in avg_price.columns[1:]:
        fig5.add_trace(go.Bar(
            x=avg_price["Branch"],
            y=avg_price[drink],
            name=drink
        ))
    fig5.update_layout(title="☕ Average Drink Price Across Branches", barmode='group', xaxis_title="Branch", yaxis_title="Average Price (£)")
    st.plotly_chart(fig5, use_container_width=True)

with cols2[1]:
    fig6 = px.imshow(avg_matrix, text_auto=".2f", color_continuous_scale="Viridis", title="🌡️ Average Drink Price by Branch (Heatmap)")
    st.plotly_chart(fig6, use_container_width=True)

drink_branch_counts = df.groupby(["Branch", "Drink"]).size().unstack(fill_value=0).reset_index()

fig9 = go.Figure()
for drink in drink_branch_counts.columns[1:]:  # skip 'Branch' column
    fig9.add_trace(go.Bar(
        x=drink_branch_counts["Branch"],
        y=drink_branch_counts[drink],
        name=drink
    ))

fig9.update_layout(
    title="🥤 Drink Popularity by Branch",
    barmode="stack",
    xaxis_title="Branch",
    yaxis_title="Number of Sales"
)

cols2[2].plotly_chart(fig9, use_container_width=True)

# Row 3
cols3 = st.columns(3)
color_map = {"Cash": "teal", "Card": "gold"}

with cols3[0]:
    fig8 = go.Figure()
    for col in branch_payment.columns[1:]:
        fig8.add_trace(go.Bar(
            x=branch_payment["Branch"],
            y=branch_payment[col],
            name=col,
            marker_color=color_map.get(col, "grey")
        ))
    fig8.update_layout(title="🏬 Branch vs Payment Type (Total Sales)", barmode='group', xaxis_title="Branch", yaxis_title="Revenue (£)")
    st.plotly_chart(fig8, use_container_width=True)

with cols3[1]:
    fig2 = px.bar(
        payment_dist,
        x="Payment Type",
        y="Count",
        color="Payment Type",
        color_discrete_map=color_map,
        title="💳 Payment Type Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

with cols3[2]:
    fig7 = px.pie(
        payment_share,
        names="Payment Type",
        values="Count",
        color="Payment Type",
        color_discrete_map=color_map,
        title="💳 Payment Method Share"
    )
    st.plotly_chart(fig7, use_container_width=True)

st.markdown("---")
st.success("All visualisations loaded successfully! ✅")

# Run this is the terminal:
# streamlit run cafe_dashboard.py