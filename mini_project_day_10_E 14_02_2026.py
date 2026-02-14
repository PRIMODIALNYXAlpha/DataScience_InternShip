
import numpy as np

np.random.seed(42)

days = 30

# 1️⃣ Daily customers (Poisson Distribution)
daily_customers = np.random.poisson(lam=120, size=days)

# 2️⃣ Purchase amount (Normal Distribution)
purchase_amount = np.random.normal(loc=1500, scale=300, size=days)

# 3️⃣ Product category selection (Multinomial Distribution)
product_selection = np.random.multinomial(
    n=120,
    pvals=[0.4, 0.3, 0.2, 0.1],
    size=days
)

# 4️⃣ Delivery time (Poisson Distribution)
delivery_time = np.random.poisson(lam=3, size=days)

# 5️⃣ Waiting time between orders (Exponential Distribution)
waiting_time = np.random.exponential(scale=2, size=days)

# 6️⃣ Product quality check (Binomial Distribution)
product_quality = np.random.binomial(n=100, p=0.95, size=days)

print("===== E-COMMERCE 30 DAY ANALYSIS =====")

# Customers Analysis
print("\n--- Customer Analysis ---")
print("Total Customers:", np.sum(daily_customers))
print("Average Customers per Day:", np.mean(daily_customers))
print("Maximum Customers in a Day:", np.max(daily_customers))

# Revenue Analysis
print("\n--- Revenue Analysis ---")
print("Total Revenue:", round(np.sum(purchase_amount), 2))
print("Average Revenue per Day:", round(np.mean(purchase_amount), 2))
print("Highest Revenue Day:", round(np.max(purchase_amount), 2))

# Product Sales Analysis
print("\n--- Product Sales (A, B, C, D) ---")
print("Total Sales:", np.sum(product_selection, axis=0))

# Delivery Analysis
print("\n--- Delivery Time Analysis ---")
print("Average Delivery Time:", np.mean(delivery_time))
print("Maximum Delivery Time:", np.max(delivery_time))

# Waiting Time Analysis
print("\n--- Waiting Time Between Orders ---")
print("Average Waiting Time:", round(np.mean(waiting_time), 2))
print("Maximum Waiting Time:", round(np.max(waiting_time), 2))

# Product Quality Analysis
print("\n--- Product Quality Analysis ---")
print("Total Good Products:", np.sum(product_quality))
print("Average Good Products per Day:", np.mean(product_quality))
