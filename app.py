import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title("💪 BMI Calculator")
st.write("Enter your height and weight below to calculate your Body Mass Index.")

st.divider()

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
with col2:
    height_cm = st.number_input("📏 Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

if st.button("Calculate BMI", use_container_width=True):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.divider()

    st.metric(label="Your BMI", value=f"{bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
        color = "info"
    elif bmi < 25:
        category = "Normal weight"
        color = "success"
    elif bmi < 30:
        category = "Overweight"
        color = "warning"
    else:
        category = "Obese"
        color = "error"

    getattr(st, color)(f"Category: {category}")

    scale_position = min(max((bmi - 15) / (40 - 15), 0), 1)
    st.progress(scale_position)
    st.caption("Scale from 15 (very underweight) to 40 (severely obese)")

with st.sidebar:
    st.header("ℹ️ About BMI")
    st.write(
        "Body Mass Index (BMI) is a simple screening measure using weight "
        "and height. It doesn't account for muscle mass, bone density, or "
        "body composition, so it's a general guide rather than a diagnosis."
    )