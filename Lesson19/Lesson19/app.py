import streamlit as st
import requests
import pandas as pd

st.title("Project managment App")

st.header("Add a Developer")
dev_name= st.text_input("Devoloper NAme")
dev_experience = st.number_input("Experience (Years)",min_value=0,max_value=50,value=0)