import streamlit as st
st.sidebar.header("sidebar")
st.sidebar.write("butoni eshte klikuar")

tab1,tab2,tab3, = st.tabs(["tab1","tab2","tab3"])

with tab1:
st.header("hello there")
st.write("butoni eshte klikuar")

with tab2:
st.header("hello there")
st.write("butoni eshte klikuar")