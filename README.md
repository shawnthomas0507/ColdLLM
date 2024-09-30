# ColdLLM
An LLM based project to create a cold email based on scraped website job description and personal stored github links or portfolio links in a vector database.

Basic Process explained:
-Using langchain WebLoader to scrape the job posting webpage.\n
-Using the Llama 3.1 8b from groq cloud to extract relevant info from the scraped data.\n
-Passing the output of the LLM and combining it with the potfolio links from chromadb.\n
-Pass the combined data to Llama 3.1 once more to generate the final cold e-mail.\n

Technologies:
LLM
Streamlit
Python
ChromaDB

