from langchain_google_genai import GoogleGenerativeAI
# from langchain_anthropic import Anthropic
# from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-flash")
# llm = Anthropic(model='claude-3-opus-20240229')
# llm = OpenAI(model='gpt-3.5-turbo')

result = llm.invoke("What is capital of Pakistan?")
print(result)