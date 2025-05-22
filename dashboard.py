import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("sales.csv", parse_dates=["date"])
    return df

df = load_data()

# Filter by region
st.sidebar.header("Filter Options")
region = st.sidebar.selectbox("Select Region", options=["All"] + sorted(df["region"].unique().tolist()))
if region != "All":
    df = df[df["region"] == region]

# Filter by product
product = st.sidebar.selectbox("Select Product", options=["All"] + sorted(df["product"].unique().tolist()))
if product != "All":
    df = df[df["product"] == product]

# Display summary metrics
st.subheader("Summary Metrics")
st.metric("Total Units Sold", int(df["units_sold"].sum()))
st.metric("Total Revenue", f"${df['revenue'].sum():,.2f}")

# Line chart of revenue over time
st.subheader("Revenue Over Time")
revenue_over_time = df.groupby("date")["revenue"].sum().reset_index()
st.line_chart(revenue_over_time.rename(columns={"date": "index"}).set_index("index"))

# Display filtered table
st.subheader("Filtered Sales Data")
st.dataframe(df)

# Bar chart of revenue by product
st.subheader("Revenue by Product")

# Group by product
revenue_by_product = df.groupby("product")["revenue"].sum().reset_index()

# Simple bar chart
st.bar_chart(revenue_by_product.set_index("product"))



