import streamlit as st

st.title('Calculator')
st.markdown("Welcome To My First Streamlit App 😎")

c1, c2 = st.columns(2)
fnum = c1.number_input("Enter First Number")
snum = c2.number_input("Enter Second Number")

options = ["Add", "Sub", "Mul", "Div"]
choice = st.radio("Select an Operation", options, horizontal=True)

button = st.button("Calculate")

if button:
    if choice == "Add":
        result = fnum + snum
    if choice == "Sub":
        result = fnum - snum
    if choice == "Mul":
        result = fnum*snum
    if choice == "Div":
        result = fnum/snum

st.success(f'result is {result}')