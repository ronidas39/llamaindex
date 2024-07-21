from llama_index.core import SimpleDirectoryReader,VectorStoreIndex,Settings
from llama_index.llms.openai import OpenAI

Settings.llm=OpenAI(model="gpt-4o",max_tokens=1050)

documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents)
engine=index.as_query_engine()
response=engine.query("explain the usage of smart contract , explain every use case in detail")
print(response)