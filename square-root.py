import streamlit as st
import math

# Title of the app
st.title("Square Root Calculator")

# Input field for the number
number = st.number_input("Enter a number", value=0.0, step=0.1)
# Calculate and display the square root
if st.button("Calculate"):
    square_root = math.sqrt(number)
    st.success(f"The square root of {number} is {square_root:.2f}")
