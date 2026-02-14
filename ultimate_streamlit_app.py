
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ultimate Streamlit App", layout="wide")

st.title("🚀 Ultimate Streamlit Application")

# ================= SIDEBAR =================
st.sidebar.title("📚 Courses Menu")

course = st.sidebar.selectbox(
    "Select Course",
    ["Data Science", "Full Stack Java", "Full Stack Python", "Dot Net"]
)

st.sidebar.success(f"You selected {course}")

# ================= PROFILE SECTION =================
st.header("👤 My Profile")

st.write("Name: Subhakar R P")
st.write("Role: Data Scientist")
st.write("Skills: Python, SQL, Machine Learning")

# ================= USER INPUT SECTION =================
st.header("📝 User Input")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 0, 100)

if st.button("Submit Details"):
    st.success(f"Name: {name}")
    st.success(f"Age: {age}")

# ================= CHECKBOX =================
st.header("☑ Checkbox Example")

if st.checkbox("Show Secret Message"):
    st.write("🔥 This is hidden content!")

# ================= SELECTBOX =================
st.header("💻 Programming Language Selection")

language = st.selectbox(
    "Choose Programming Language",
    ["Python", "Java", "C++", "SQL"]
)

st.write(f"You selected: {language}")

# ================= COUNTER =================
st.header("🔢 Counter App")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase Counter"):
    st.session_state.count += 1

st.write("Counter Value:", st.session_state.count)

# ================= STATIC DATAFRAME =================
st.header("📊 Sample DataFrame")

data = {
    "Name": ["Rahul", "Anita", "Vikram"],
    "Salary": [80000, 60000, 25000]
}

df = pd.DataFrame(data)
st.dataframe(df)

# ================= FILE UPLOAD =================
st.header("📂 Upload CSV File")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    uploaded_df = pd.read_csv(file)
    st.subheader("Uploaded Data")
    st.dataframe(uploaded_df)

    # Salary Filter
    if "Salary" in uploaded_df.columns:
        filtered = uploaded_df[uploaded_df["Salary"] > 50000]
        st.subheader("Employees with Salary > 50,000")
        st.dataframe(filtered)

# ================= IMAGE DISPLAY =================
st.header("🖼 Image Display")

st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=200)

# ================= ROLE BASED CONTENT =================
st.header("👥 Role Based Content")

role = st.radio("Select Your Role", ["Student", "Teacher", "Admin"])

if role == "Student":
    st.write("🎓 Access courses and assignments.")

elif role == "Teacher":
    st.write("👨‍🏫 Manage classes and upload marks.")

elif role == "Admin":
    st.write("🔐 Full system access.")

st.success("✅ Application Loaded Successfully!")
