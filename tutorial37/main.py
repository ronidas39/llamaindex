from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,StorageContext
from llama_index.vector_stores.duckdb import DuckDBVectorStore

# loader=SimpleDirectoryReader(input_files=["/Users/roni/Documents/GitHub/llamaindex/tutorial37/2411.13585v1.pdf"])
# docs=loader.load_data()

# vs=DuckDBVectorStore("llama.db",persist_dir="./dir")
# sc=StorageContext.from_defaults(vector_store=vs)
# index=VectorStoreIndex.from_documents(docs,storage_context=sc)

vs=DuckDBVectorStore.from_local("./dir/llama.db")
index=VectorStoreIndex.from_vector_store(vector_store=vs)
qe=index.as_query_engine()
reponse=qe.query("what is the role of ai in us cyber security")
print(reponse)