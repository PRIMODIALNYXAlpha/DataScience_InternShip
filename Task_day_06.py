# Run with: `streamlit run app.py` — do NOT use `python app.py` (session state won't work)
import streamlit as st
import pandas as pd

st.title("Employee Salary Filter App")

# Load CSV
df = pd.read_csv("employees.csv")

# Role selection
role = st.selectbox("Select Your Role", ["Admin", "HR", "Developer", "Manager"])

st.subheader("Employees with Salary > 50,000")
filtered_df = df[df["Salary"] > 50000]
st.dataframe(filtered_df)

st.subheader("Role-Based Content")

if role == "Admin":
    st.success("Welcome Admin! You have full access.")
elif role == "HR":
    st.info("Welcome HR! You can manage employee records.")
elif role == "Developer":
    st.warning("Welcome Developer! You can view project details.")
elif role == "Manager":
    st.error("Welcome Manager! You can view reports and analytics.")
