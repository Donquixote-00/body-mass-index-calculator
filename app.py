import streamlit as st

# This is the title shown at the top of the page
st.title("BMI Calculator")

st.write("Enter your height and weight to calculate your BMI.")

# Widgets: these create the input boxes on the page
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

# A button — the code below only runs when it's clicked
if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write(f"Your BMI is: **{bmi:.2f}**")

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")