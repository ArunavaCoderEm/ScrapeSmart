import streamlit as st

st.title("ScrapeSmart")
scrappable_url = st.text_input("Enter an URL here - ")

if (st.button("Get Data")):
    st.write("Working")
    