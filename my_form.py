import streamlit as st

st.title("Registration Form")
student_details={
      "name":None,
      "salary":None,
      "age":None,
      "gender":None
}

with st.form("Important Information"):
    student_details["name"] = st.text_input("Enter your name*")
    salary = st.number_input("Enter your salary*",min_value=10000,max_value=50000,step=10000,)
    #age = st.slider("Enter your age",min_value=1,max_value=100)
    student_details["age"] = st.number_input("Enter your age",min_value=1,max_value=100)
    
    student_details["gender"] = st.selectbox("Enter your gender (optional)",["Male","Female"])


    submitted = st.form_submit_button()
    if submitted:
        st.write("Form submitted successfully")
        if not student_details["name"].strip():
            st.error("Kindly fill the name field")
        #elif not age:
            #st.error("kindly fill the age")
        elif not student_details["gender"]:
                    st.error("Enter your gender")
        else:
              st.write(f"{student_details["name"]} your name ")
              st.write(f"{student_details["age"]} your age ")
              st.write(f"{salary} your salary ")
              st.write(f"{student_details["gender"]} your gender ")