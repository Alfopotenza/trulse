import streamlit as st
from scrape import *
from Parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL")
if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body = extract_body_content(result)
    clean_body = clean_body_content(body)
    st.session_state.dom_content = clean_body

    with st.expander("View DOM content"):
        st.text_area("DOM Content", clean_body, height=300)

if 'dom_content' in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)