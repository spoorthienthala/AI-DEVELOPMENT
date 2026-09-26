import streamlit as st
st.title("My First Streamlit App!!!")
st.write("Welcome to my AI application!")
name=st.text_input("Enter your name:")
age=st.number_input("Enter your age:")
st.write("Hello",name)
st.write("age:",age)