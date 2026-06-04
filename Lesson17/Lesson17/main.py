import  streamlit as st


col1,col2,col3,col4,col5 = st.columns(5,gap="small",vertical_alignment="center")

with col1:
    st.header("Kolona 1")
    st.write("Content fo column 1")


with col2:
    st.header("Column 2")
    st.write("Kolona e 2")

with col3:
    st.header("Kolona 3")
    st.write("Content for Column 3")


with col5:
    st.header("Kolona 4")
    st.write("Kontent for kolona 4")

with st.container():
    st.header("This is inside the container")
    st.write("This is inside the container")

st.write("This is outside the container")


st.sidebar.header("Sidebar")

st.sidebar.write("this is the sidebar")

st.sidebar.selectbox("chose an option",["Option 1","Option 2","Option3"])

st.sidebar.radio("go to",["Home","Data","Settings"])