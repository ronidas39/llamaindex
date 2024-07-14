from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-4o")
documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents,llm=llm)
query_engine=index.as_query_engine()
response=query_engine.query("plain the concept of a decision tree in machine learning. How does it handle classification and regression tasks, and what are its advantages and limitations?")
print(response)