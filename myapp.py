import streamlit as st
import os
st.title("Discipline And Motivation")
st.header("Wallpapers")
name=st.text_input("Enter your name")
age=st.number_input("Enter your Age",min_value=18,max_value=100,step=5)
st.write(f"Name: {name} your age is {age}")
gender=st.selectbox("Select your Gender",["Male","Female"])
Subject=st.multiselect("Select your choice",["Python","Java","C++","MySQL"])
login=st.button("Login")

if login:
    st.success("Form Submitted Successfully")
    st.write(name)
    st.write(age)
    st.write(gender)
    st.write(Subject)

st.divider()
st.image(r"C:\Users\user\CrossDevice\moto g34 5G\storage\Pictures\file_00000000db3c820b865f2f29ecee1029.png")
st.image(os.path.join(os.getcwd(),"Static","file_00000000829882119cd68a94e7a9ec3e.png"),width=100)