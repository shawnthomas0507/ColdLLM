import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_groq import ChatGroq

def stream_app(llm,portfolio,clean_text):
    st.title("Cold Email Generator")
    url_input=st.text_input("Enter a URL:",value="https://jobs.nike.com/job/R-37526")
    submit_button=st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            skills = jobs[0]["description"]
            links = portfolio.query_links(skills)
            email = llm.write_mail(jobs, links)
            st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    stream_app(chain, portfolio, clean_text)