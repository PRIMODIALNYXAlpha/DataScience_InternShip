
import numpy as np

np.random.seed(42)

print("=======================================")
print(" NUMPY DATA DISTRIBUTION COMPLETE PROJECT ")
print("=======================================\n")

# =====================================================
# 1️⃣ Salary Analysis – Normal Distribution
# =====================================================
salary = np.random.normal(loc=50000, scale=8000, size=100)

print("===== Salary Analysis =====")
print("Mean Salary:", np.mean(salary))
print("Maximum Salary:", np.max(salary))
print("Total Salary Expense:", np.sum(salary))


# =====================================================
# 2️⃣ Website Visitors – Poisson (365 days)
# =====================================================
website_visitors = np.random.poisson(lam=500, size=365)

print("\n===== Website Visitors (1 Year) =====")
print("Average Visitors per Day:", np.mean(website_visitors))
print("Peak Day Visitors:", np.max(website_visitors))


# =====================================================
# 3️⃣ Hospital Emergency Cases – Poisson (30 days)
# =====================================================
hospital_cases = np.random.poisson(lam=40, size=30)

print("\n===== Hospital Emergency Cases =====")
print("Total Cases:", np.sum(hospital_cases))
print("Maximum Cases in a Day:", np.max(hospital_cases))


# =====================================================
# 4️⃣ Exam Pass/Fail – Binomial
# =====================================================
exam_results = np.random.binomial(n=100, p=0.7, size=30)

print("\n===== Exam Results =====")
print("Total Passed:", np.sum(exam_results))
print("Pass Percentage:", np.mean(exam_results) * 100)


# =====================================================
# 5️⃣ Product Selection – Multinomial
# =====================================================
product_choice = np.random.multinomial(
    n=200,
    pvals=[0.4, 0.3, 0.2, 0.1],
    size=1
)

print("\n===== Product Selection (A, B, C, D) =====")
print("Sales Distribution:", product_choice)


# =====================================================
# 6️⃣ Server Response Time – Exponential
# =====================================================
server_response = np.random.exponential(scale=1.5, size=100)

print("\n===== Server Response Time =====")
print("Average Response Time:", np.mean(server_response))
print("Maximum Response Time:", np.max(server_response))


# =====================================================
# 7️⃣ Call Center (24 Hours) – Poisson
# =====================================================
call_center = np.random.poisson(lam=30, size=24)

print("\n===== Call Center (24 Hours) =====")
print("Total Calls:", np.sum(call_center))
print("Peak Hour Calls:", np.max(call_center))


# =====================================================
# 8️⃣ Manufacturing Quality – Binomial
# =====================================================
quality_check = np.random.binomial(n=100, p=0.95, size=30)

print("\n===== Manufacturing Quality =====")
print("Total Good Products:", np.sum(quality_check))
print("Average Good Products per Day:", np.mean(quality_check))


# =====================================================
# 9️⃣ Bank Loan Approval – Binomial
# =====================================================
loan_approval = np.random.binomial(n=50, p=0.6, size=30)

print("\n===== Bank Loan Approval =====")
print("Total Approved Loans:", np.sum(loan_approval))
print("Average Approval per Day:", np.mean(loan_approval))


# =====================================================
# 🔟 E-Commerce 30 Day Simulation (Mini Project)
# =====================================================
days = 30

daily_customers = np.random.poisson(lam=120, size=days)
purchase_amount = np.random.normal(loc=1500, scale=300, size=days)
product_selection = np.random.multinomial(
    n=120,
    pvals=[0.4, 0.3, 0.2, 0.1],
    size=days
)
delivery_time = np.random.poisson(lam=3, size=days)
waiting_time = np.random.exponential(scale=2, size=days)
product_quality = np.random.binomial(n=100, p=0.95, size=days)

print("\n===== 30-Day E-Commerce Analysis =====")
print("Total Customers:", np.sum(daily_customers))
print("Average Customers per Day:", np.mean(daily_customers))
print("Total Revenue:", round(np.sum(purchase_amount), 2))
print("Most Sold Product (A,B,C,D):", np.sum(product_selection, axis=0))
print("Average Delivery Time:", np.mean(delivery_time))
print("Average Waiting Time:", np.mean(waiting_time))
print("Total Good Products:", np.sum(product_quality))

print("\nProject Execution Completed Successfully ✅")
