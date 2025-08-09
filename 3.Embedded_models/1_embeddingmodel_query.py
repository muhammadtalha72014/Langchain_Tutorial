from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimensions = 32)

result = embeddings.embed_query("Islamabad is the capital of Pakistan?")
print(str(result))