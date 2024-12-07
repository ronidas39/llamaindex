from llama_index.readers.remote import RemoteReader
from llama_index.core import VectorStoreIndex

loader=RemoteReader()
docs=loader.load_data("https://www.gutenberg.org/cache/epub/74849/pg74849.txt")
index=VectorStoreIndex.from_documents(docs)
qe=index.as_query_engine()
response=qe.query("who is Ethel , give some information on her")
print(response)

