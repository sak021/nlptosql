import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import llm_prompt_to_generate_sql


def initialise_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
        )
    return llm


def fetch_llm_response(natural_language_query):
    llm = initialise_llm()
    # Define the prompt for SQL query generation
    prompt = ChatPromptTemplate.from_messages(llm_prompt_to_generate_sql)

    try:
        chain = prompt | llm
        output_raw_response = chain.invoke(
            {
                "input": natural_language_query
            }
        )
        print(f"Generated SQL Query: \n {output_raw_response.content}")
        return output_raw_response

    except Exception as e:
        return f"An error occurred: {e}"
    

def parse_llm_response(llm_response):
    match = re.search(r'\*\|\*(.*?)\*\|\*', llm_response)
    if match:
        output_response = match.group(1).strip()
    else:
        print("No Output Response.")
    return output_response
