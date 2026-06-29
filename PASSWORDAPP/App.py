import streamlit as st

st.title("PassWord Analyser") 

password = st.text_input("Enter the password", type="password")

# st.button("Validate")
if st.button("Validate"):
    upper=lower=digit=special=False

    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and digit and special:
        st.success("Strong Password...Thank you!")
    else:
        st.error("Invalid Password!")    

        if len(password)<8:
            st.write("Password must contain at aleast 8 characters")
        if not upper:
            st.write("must contain a uppercase")
        if not lower:
            st.write("must contain a lowercase")
        if not digit:
            st.write("must contain digit")
        if not special:
            st.write("must contain special")                                