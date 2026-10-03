# 🛍️ Customer Shopping Behavior Analysis

An end-to-end data analytics project that cleans retail customer data with **Python**, answers business questions with **SQL (PostgreSQL)**, and presents the results in an interactive **Power BI** dashboard.

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Tools & Technologies](#-tools--technologies)
- [Project Workflow](#-project-workflow)
- [Data Cleaning & EDA (Python)](#-data-cleaning--eda-python)
- [SQL Business Analysis](#-sql-business-analysis)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Insights](#-key-insights)
- [Business Recommendations](#-business-recommendations)
- [Repository Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 🎯 Problem Statement

Retail businesses collect large amounts of transaction data, but raw data does not directly give actionable insights. This project analyzes customer shopping behavior to understand **purchasing patterns, customer spending, product performance, discount usage, subscription behavior, shipping preferences, and customer segments**.

## 📂 Dataset

- **Records:** 3,900 customers
- **Attributes:** 18 original columns
- **File:** `customer_shopping_behavior.csv`

| Group | Columns |
|---|---|
| Demographics | Customer ID, Age, Gender, Location |
| Product | Item Purchased, Category, Size, Color, Season |
| Purchase | Purchase Amount (USD), Review Rating, Previous Purchases, Frequency of Purchases |
| Offers & Delivery | Discount Applied, Promo Code Used, Shipping Type |
| Customer | Subscription Status, Payment Method |

## 🧰 Tools & Technologies

| Tool | Purpose |
|---|---|
| Python (Pandas) | Data loading, cleaning, feature engineering, EDA |
| PostgreSQL / SQL | Business analysis queries, aggregations, window functions |
| Power BI | Interactive dashboard and visualization |

## 🔄 Project Workflow

```
Raw CSV  →  Python (clean + engineer features)  →  PostgreSQL (SQL analysis)  →  Power BI (dashboard)  →  Insights & recommendations
```

## 🐍 Data Cleaning & EDA (Python)

| Step | What was done |
|---|---|
| Structure check | `df.info()` confirmed 3,900 rows, 18 columns, and only `Review Rating` with nulls |
| Statistical summary | `df.describe(include='all')` to understand distributions |
| Missing values | 37 missing ratings (≈0.9%) filled with the **median rating of each product category** |
| Column standardization | Column names converted to lowercase `snake_case` |
| Age groups | Customers split into 4 quartile groups: young adult, adult, middle age, senior (`pd.qcut`) |
| Purchase frequency | Text frequencies (Weekly, Fortnightly, Annually, …) mapped to numeric **days** |
| Redundant column | `promo_code_used` dropped because it was identical to `discount_applied` |

```python
# Fill missing ratings with the category median
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)

# Age groups
labels = ['young adult', 'adult', 'middle age', 'senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
```

## 🗄️ SQL Business Analysis

The cleaned data was loaded into PostgreSQL and used to answer 10 business questions:

1. Revenue by gender
2. Discount users who still spent above the average
3. Top 5 products by average review rating
4. Average purchase: Standard vs Express shipping
5. Subscribers vs non-subscribers (customers, average spend, revenue)
6. Products with the highest discount usage
7. Customer segmentation: New, Returning, Loyal
8. Top 3 products in each category (window function)
9. Subscription status of repeat buyers
10. Revenue by age group

**SQL concepts used:** `GROUP BY`, aggregate functions, subqueries, CTEs, `CASE WHEN`, `ROW_NUMBER() OVER (PARTITION BY ...)`, filtering and sorting.

## 📊 Power BI Dashboard

The dashboard includes:

- **KPI cards:** Number of Customers (3.9K), Average Purchase Amount ($59.76), Average Review Rating (3.75)
- **Charts:** % of Subscribers, Revenue by Category, Sales by Category, Revenue by Age Group, Sales by Age Group
- **Slicers:** Subscription Status, Gender, Category, Shipping Type

## 💡 Key Insights

- Revenue totals about **$233K** across 3,900 customers.
- **Male customers generate ~68%** of revenue ($157,890 vs $75,191).
- **Clothing and Accessories** generate about 76% of revenue; Clothing is the top category ($104K).
- **43% of purchases use a discount**, and products like Hat, Sneakers, and Coat are discounted in about half of their purchases.
- **Only 27% of customers are subscribers**, and subscribers spend about the same as non-subscribers ($59.49 vs $59.87).
- **80% of customers are "Loyal"** (more than 10 previous purchases), yet only 28% of repeat buyers are subscribed.
- Express shipping customers spend slightly more than Standard ($60.48 vs $58.46).

## ✅ Business Recommendations

- Increase subscription adoption with targeted benefits and personalized offers.
- Target high-value customers with personalized discounts instead of broad discounting.
- Monitor products with high discount usage to reduce discount dependency.
- Focus inventory and marketing on high-revenue categories.
- Build loyalty programs for returning and loyal customers.
- Use customer segments and demographics for targeted campaigns.

## 📁 Repository Structure

Adjust this to match your repository.

```
├── data/
│   └── customer_shopping_behavior.csv
├── python/
│   └── app.py                  # cleaning + EDA
├── sql/
│   └── analysis_queries.sql    # 10 business queries
├── powerbi/
│   └── customer_dashboard.pbix
├── Customer_Shopping_Behavior_Project_Report.pdf
└── README.md
```

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
2. **Install dependencies**
   ```bash
   pip install pandas
   ```
3. **Run the cleaning and EDA script**
   ```bash
   python app.py
   ```
4. **Load the cleaned data into PostgreSQL**, then run the queries in the `sql/` folder.
5. **Open the `.pbix` file in Power BI Desktop** to explore the dashboard.

## 👤 Author

**Aayush**

- GitHub: [@your-username](https://github.com/aayush45123)
- LinkedIn: [your-profile](https://www.linkedin.com/in/aayush-bharda-399958311/)

---

⭐ If you found this project useful, consider giving it a star!
