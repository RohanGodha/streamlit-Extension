import streamlit as st

# Title of the app
st.title("My Streamlit Extension")

# Add some text to the app
st.write("Welcome to my Streamlit extension!")

# Add a button
if st.button("Click me"):
    st.write("Button clicked!")

# Add a slider
number = st.slider("Select a number", 0, 10)
st.write(f"You selected: {number}")

# Add a checkbox
if st.checkbox("Show/hide text"):
    st.write("You can see this text!")

# Add a selectbox
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")
