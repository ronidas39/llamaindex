from llama_index.core import VectorStoreIndex,download_loader
from llama_index.readers.google import GoogleDocsReader

doc_id=["1NfsiWi1JWLf7XXvNW763UTI_lu4WrSxjRJkc_jRDpts"]
loader=GoogleDocsReader()
documents=loader.load_data(document_ids=doc_id)
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("How can progressive overload be effectively applied in a resistance training program to maximize muscle hypertrophy while minimizing fat gain?")
print(response)