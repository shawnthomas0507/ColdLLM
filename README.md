# **ColdLLM: AI-Powered Cold Email Generator**

ColdLLM is an AI-powered tool designed to simplify the process of writing effective and personalized cold emails. Using advanced Large Language Models (LLMs), web scraping, and vector databases, ColdLLM automates the extraction of job descriptions and leverages personal portfolio data to craft tailored emails for job applications in the tech industry.

---

## **Features**

### 1. **Job Description Extraction**
- Automatically scrapes job postings from career pages using **LangChain WebLoader**.
- Extracts key details like the role, required skills, experience, and job descriptions from the scraped data.
  
### 2. **Portfolio Integration**
- Uses **ChromaDB** to store and query your portfolio links, such as GitHub repositories or LinkedIn projects.
- Matches the most relevant portfolio links to the extracted job requirements.

### 3. **AI-Powered Cold Email Creation**
- Employs **Llama 3.1 (70B model)** via Groq Cloud to generate professional, concise, and personalized cold emails.
- Ensures the email highlights your qualifications and relevant projects, improving your chances of catching a hiring manager's attention.

### 4. **User-Friendly Interface**
- Built with **Streamlit**, providing a clean, interactive interface for users.
- Easy-to-use input fields for URL submission and instant email generation.

---

## **Workflow**

### **Step-by-Step Process**
1. **Input Job Posting URL**  
   Enter the URL of a job posting webpage in the application.

2. **Web Scraping**  
   The webpage is scraped using **LangChain WebBaseLoader**, and the job description is cleaned using custom text-cleaning utilities.

3. **Job Information Extraction**  
   The scraped text is processed by Llama 3.1 to extract essential job details in JSON format (role, skills, experience, description).

4. **Portfolio Matching**  
   Queries **ChromaDB** for portfolio links that best align with the job's required skills.

5. **Email Generation**  
   Combines job details and portfolio links to craft a compelling cold email using Llama 3.1.

6. **Output**  
   The generated email is displayed in markdown format, ready for use.

---

## **Technologies Used**

| **Technology**  | **Purpose**                                         |
|------------------|-----------------------------------------------------|
| **LangChain**    | Web scraping and prompt chaining.                   |
| **Groq Cloud**   | Hosts Llama 3.1 (70B versatile model) for text generation. |
| **ChromaDB**     | Vector database to store and query portfolio links. |
| **Streamlit**    | User interface for seamless interaction.            |
| **Python**       | Core programming language for integration.          |

---

## **Installation and Setup**

### **Prerequisites**
1. Python 3.8 or higher installed.
2. API key for Groq Cloud Llama 3.1.
3. Portfolio data in CSV format with columns: `Techstack` and `Github-Links`.
4. ChromaDB installation for persistent vector database.

### **Steps to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ColdLLM.git
   cd ColdLLM
