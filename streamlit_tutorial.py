import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, You are on Streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets get started ")

name=st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name} !")

#Displaying Data and Charts
df = pd.DataFrame(np.random.rand(20,4), columns=['A','B','C','D'])
st.line_chart(df)
st.bar_chart(df)

# CSV upload
upload_file = st.file_uploader("Upload a CSV file", type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This is header")
st.subheader("This is subheader")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://www.google.com)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("Whats your name?")
st.text_area("Write Something....")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple","Banana","MAngo"])
st.multiselect("Choose toppings", ["Cheese","Tomato","Olive","ChilliFlakes"])
st.radio("Pick One",["Opt A","Opt B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details")

option = st.radio("Choose view", ["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear Here")

# This form demonstrates widgets only; it does not authenticate users.
with st.form("Login Form"):
    username = st.text_input("Username")
    password=st.text_input("Password", type='password')
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Welcome,{username}!")

st.image("assets/sample.svg", caption="Sample image", width="content")
st.video("https://www.youtube.com/watch?v=fVsONlc3OUY")