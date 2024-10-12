import streamlit as st

from scrapping import scrape_website

st.title("ScrapeSmart")
scrappable_url = st.text_input("Enter an URL here - ")

if (st.button("Get Data")):

    st.write("Working")
    
    data = scrape_website(scrappable_url)
    
    print(data)
    