import streamlit as st

from scrapping import (
    remove_unnecessery,
    clean_from_body,
    split_dom_content,
    scrape_website
)

st.title("ScrapeSmart")
scrappable_url = st.text_input("Enter an URL here - ")

if (st.button("Get Data")):

    st.write("Working ...")
    
    data = scrape_website(scrappable_url)
    body_content = remove_unnecessery(data)
    cleaned_content = clean_from_body(body_content)

    st.session_state.dom_content = cleaned_content


    with st.expander("View Website Content"):
        st.text_area("Website Content", cleaned_content, height=300)

