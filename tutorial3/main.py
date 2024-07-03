from llama_index.core import VectorStoreIndex
from llama_index.core.schema import Document

text_lists=["langchain is powerfull","llamaindex is awesome","homa is strong"]
documents=[Document(text=t) for t in text_lists]
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
query="is langchain beautiful?"
response=query_engine.query(query)
print(response)