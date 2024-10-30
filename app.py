import streamlit as st

st.write("Halllo World")
st.title("Demo Aplikasi Ashoka / Viume")

import streamlit as st

st.button("Reset", type="primary")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

import streamlit as st

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)

st.write("this will be shown on the latest deploy")