from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_anthropic import ChatAnthropic
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# model = ChatAnthropic(model='claude-3-opus-20240229')
# model = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5, max_completion_tokens=50)

result = model.invoke("What is capital of Pakistan?")
print(result.content)