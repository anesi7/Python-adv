import streamlit as st
st.title("Hello")

st.button("Click me")

if st.button("Hello"):
    st.write("butoni eshte klikuar")


if st.button("buttoni3"):
    st.success("Operation was successful")