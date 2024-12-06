import chromadb
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex,StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

embed_model=OpenAIEmbedding()
loader=SimpleDirectoryReader(input_files=["/Users/roni/Documents/GitHub/llamaindex/tutorial39/2410.22390v1.pdf"])
docs=loader.load_data()

db=chromadb.PersistentClient(path="./db")
cc=db.get_or_create_collection("tutorial39")
vs=ChromaVectorStore(chroma_collection=cc)
#sc=StorageContext.from_defaults(vector_store=vs)
#index=VectorStoreIndex.from_documents(docs,storage_context=sc,embed_model=embed_model)
index=VectorStoreIndex.from_vector_store(vector_store=vs)
qe=index.as_query_engine()
response=qe.query("what is role of AI to minimise the impact of fake news?")
print(response)