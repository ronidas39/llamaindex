from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
import logging
import sys
#for logging
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
#for index
documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("wgive some information on the career of the author here?")
print(response)