import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Student Performance Prediction")

st.title("🎓 Student Performance Classification")
st.write("Predict whether a student will PASS or FAIL")

# Load trained model
model = pickle.load(open("model/xgboost.pkl", "rb"))

# -------------------------------
# INPUT SECTION
# -------------------------------

st.header("📋 Enter Student Details")

# Demographic
school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["F", "M"])
age = st.slider("Age", 15, 22, 17)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parent Status", ["T", "A"])

# Parents Education
Medu = st.slider("Mother Education (0-4)", 0, 4, 2)
Fedu = st.slider("Father Education (0-4)", 0, 4, 2)

# Study Related
studytime = st.slider("Study Time (1-4)", 1, 4, 2)
failures = st.slider("Past Class Failures (0-4)", 0, 4, 0)

# Support
schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra Curricular Activities", ["yes", "no"])

# Lifestyle
internet = st.selectbox("Internet Access", ["yes", "no"])
romantic = st.selectbox("In Romantic Relationship", ["yes", "no"])

# Social
famrel = st.slider("Family Relationship (1-5)", 1, 5, 3)
freetime = st.slider("Free Time (1-5)", 1, 5, 3)
goout = st.slider("Going Out (1-5)", 1, 5, 3)
Dalc = st.slider("Workday Alcohol (1-5)", 1, 5, 1)
Walc = st.slider("Weekend Alcohol (1-5)", 1, 5, 2)
health = st.slider("Health Status (1-5)", 1, 5, 3)
absences = st.slider("Absences", 0, 100, 5)

# -------------------------------
# DATA PREPARATION
# -------------------------------

if st.button("🔍 Predict Performance"):

    input_dict = {
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }

    input_df = pd.DataFrame([input_dict])

    # Convert categorical variables to numeric (same mapping as training)
    binary_map = {"yes": 1, "no": 0}
    input_df.replace(binary_map, inplace=True)

    categorical_map = {
        "school": {"GP": 0, "MS": 1},
        "sex": {"F": 0, "M": 1},
        "address": {"U": 0, "R": 1},
        "famsize": {"LE3": 0, "GT3": 1},
        "Pstatus": {"T": 0, "A": 1},
    }

    for col in categorical_map:
        input_df[col] = input_df[col].map(categorical_map[col])

    # Scaling (same as training)
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_df)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🎉 Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")
