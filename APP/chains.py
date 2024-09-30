import langchain
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
import langchain_community
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd 
import chromadb
import uuid
from langchain_core.exceptions import OutputParserException
from langchain_groq import ChatGroq

class Chain:
    def __init__(self):
        self.llm=ChatGroq(temperature=0,groq_api_key="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",model="llama-3.1-70b-versatile")
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys:`role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### INSTRUCTION:
            You are Shawn Thomas, an Artificial Intelligence and Machine Learning student at Drexel University 
            currently looking for a job in the Tech industry.Your job is to write a concise and to the point cold email to the hiring manager regarding the job description: {job_description}. Using this description describe your capability to fulfill their needs.
            Also add the most relevant projects from the following links to showcase from Shawn's important added links like linkedin and github project links: {link_list}.
            Remember you are Shawn, a graduate student at Drexel University. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content