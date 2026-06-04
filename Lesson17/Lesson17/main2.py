from cProfile import label

import streamlit as st

with st.form("my form",clear_on_submit=True):
    name = st.text_input("Name")

    age = st.slider("Age",min_value=0,max_value=100)

    email = st.text_input("email")

    biography = st.text_input("Short biio")

    terms = st.checkbox("I agree to the terms an condition")

    submit_button = st.form_submit_button(label="submit")

if submit_button:
    st.write(f"Name :{name}")
    st.write(f"Age :{age}")
    st.write(f"Email :{email}")
    st.write(f"Short Bio :{biography}")


    if terms:
        st.write("you agreed to the terms and conditions")
    else:
        st.write("you did not agree to the terms and conditions")
