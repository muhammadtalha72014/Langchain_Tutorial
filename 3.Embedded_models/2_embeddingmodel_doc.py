from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimensions = 32)

document = [
    "Islamabad is capital of Pakistan",
    "Karachi is the largest city of Pakistan",
    "Pakistan famous city for food is Lahore"
]

result = embeddings.embed_documents(document)
print(str(result))
# print(len(result))