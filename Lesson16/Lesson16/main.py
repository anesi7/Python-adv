import streamlit as st
from watchdog.observers.fsevents2 import message


def main():
    st.title("Hello,Word")

    st.button("Click me")

    st.checkbox("check me")

if st.checkbox("check me to show some text"):
    st.write("qiky tekst po shfaqet sepse ti e ke check katrorin e zbrazet")

if st.button("Click"):
    st.write("Button Clicked")

name = st.text_input("Enter your name")
st.write("your name is:" ,name)

age = st.number_input("enter your age",max_value=100,min_value=0)
st.write("your age is:",age)

message = st.text_area("Enter a message ")

if st.button("Success"):
    st.success("Operation is successful")


if __name__=="__main__":
    main()