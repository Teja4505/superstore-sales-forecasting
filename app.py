
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
    return df

df = load_data()

# ---------------- TITLE ----------------
st.title("📊 Superstore Sales Forecasting Dashboard")
st.markdown("### Sales Performance & Business Insights")
st.divider()

# ---------------- KPI CARDS ----------------
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
max_sale = df["Sales"].max()
total_orders = df["Order ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 💰 Total Sales")
    st.markdown(f"## ${total_sales:,.0f}")

with col2:
    st.markdown("### 🛒 Total Orders")
    st.markdown(f"## {total_orders:,}")

with col3:
    st.markdown("### 📈 Average Sale")
    st.markdown(f"## ${avg_sales:,.2f}")

with col4:
    st.markdown("### 🚀 Maximum Sale")
    st.markdown(f"## ${max_sale:,.2f}")

st.divider()

# ---------------- MONTHLY SALES TREND ----------------
st.header("📈 Monthly Sales Trend")

monthly_sales = (
    df.set_index("Order Date")
      .resample("ME")["Sales"]
      .sum()
)

fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")
ax1.set_title("Monthly Sales Over Time")
ax1.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# ---------------- CATEGORY SALES ----------------
st.header("🛍️ Category-wise Sales")

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(10, 5))
category_sales.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Category")
ax2.set_ylabel("Sales")
ax2.set_title("Sales by Category")
ax2.tick_params(axis="x", rotation=0)
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

# ---------------- REGION SALES ----------------
st.header("🌍 Region-wise Sales")

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig3, ax3 = plt.subplots(figsize=(10, 5))
region_sales.plot(kind="bar", ax=ax3)
ax3.set_xlabel("Region")
ax3.set_ylabel("Sales")
ax3.set_title("Sales by Region")
ax3.tick_params(axis="x", rotation=0)
plt.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

# ---------------- TOP 10 PRODUCTS ----------------
st.header("🏆 Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .nlargest(10)
      .sort_values()
)

fig4, ax4 = plt.subplots(figsize=(12, 7))
top_products.plot(kind="barh", ax=ax4)
ax4.set_xlabel("Sales")
ax4.set_ylabel("Product")
ax4.set_title("Top 10 Products by Sales")
plt.tight_layout()
st.pyplot(fig4)
plt.close(fig4)

# ---------------- SEGMENT SALES ----------------
st.header("👥 Segment-wise Sales")

segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig5, ax5 = plt.subplots(figsize=(10, 5))
segment_sales.plot(kind="bar", ax=ax5)
ax5.set_xlabel("Segment")
ax5.set_ylabel("Sales")
ax5.set_title("Sales by Customer Segment")
ax5.tick_params(axis="x", rotation=0)
plt.tight_layout()
st.pyplot(fig5)
plt.close(fig5)

# ---------------- BUSINESS INSIGHTS ----------------
st.divider()
st.header("💡 Key Business Insights")

best_category = category_sales.idxmax()
best_region = region_sales.idxmax()
best_segment = segment_sales.idxmax()
best_month = monthly_sales.idxmax().strftime("%B %Y")

st.success(f"""
🏆 Best Performing Category: {best_category}

🌍 Highest Sales Region: {best_region}

👥 Top Customer Segment: {best_segment}

📅 Highest Sales Month: {best_month}

💰 Total Sales Generated: ${total_sales:,.2f}
""")

st.success("✅ Dashboard loaded successfully!")
