import streamlit as st

from scrapping import (
    remove_unnecessery,
    clean_from_body,
    split_dom_content,
    scrape_website
)

from ollama import parse_with_ollama_model

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


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to check ")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the website ...")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama_model(dom_chunks, parse_description)
            st.write(parsed_result)