import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline model
model = joblib.load("campus_placement_svm.pkl")

st.set_page_config(page_title="Campus Placement Predictor", layout="centered")

st.title("🎓 Campus Placement Prediction App")
st.write("Fill student details to predict placement status")

# ---------- User Inputs ----------
age = st.number_input("Age", min_value=17, max_value=40, value=21)

gender = st.selectbox("Gender", ["Male", "Female"])

degree = st.selectbox(
    "Degree",
    ["B.Tech", "B.Sc", "BCA", "MCA", "M.Tech"]
)

branch = st.selectbox(
    "Branch",
    ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"]
)

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)

internships = st.number_input("Number of Internships", 0, 10, 1)
projects = st.number_input("Number of Projects", 0, 10, 2)

coding_skills = st.slider("Coding Skills (1-10)", 1, 10, 6)
communication_skills = st.slider("Communication Skills (1-10)", 1, 10, 6)

aptitude_score = st.slider("Aptitude Test Score", 0, 100, 70)
soft_skills = st.slider("Soft Skills Rating (1-10)", 1, 10, 6)

certifications = st.number_input("Number of Certifications", 0, 10, 1)
backlogs = st.number_input("Number of Backlogs", 0, 10, 0)

# ---------- Prediction ----------
if st.button("🔮 Predict Placement"):
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Degree": degree,
        "Branch": branch,
        "CGPA": cgpa,
        "Internships": internships,
        "Projects": projects,
        "Coding_Skills": coding_skills,
        "Communication_Skills": communication_skills,
        "Aptitude_Test_Score": aptitude_score,
        "Soft_Skills_Rating": soft_skills,
        "Certifications": certifications,
        "Backlogs": backlogs
    }])

    prediction = model.predict(input_data)[0]

    if prediction == "Placed":
        st.success("✅ Student is likely to be **PLACED**")
    else:
        st.error("❌ Student is likely **NOT PLACED**")