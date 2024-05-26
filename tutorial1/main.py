from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("give some information on the career of the author")
print(response)