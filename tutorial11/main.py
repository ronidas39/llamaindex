from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.core import SimpleDirectoryReader,StorageContext
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.vector_stores.lancedb import LanceDBVectorStore

llm=OpenAIMultiModal(model="gpt-4o")

text_store=LanceDBVectorStore(uri="lancedb",table_name="text_collection")
image_store=LanceDBVectorStore(uri="lancedb",table_name="image_collection")
storage_context=StorageContext.from_defaults(vector_store=text_store,image_store=image_store)
documents=SimpleDirectoryReader("data").load_data()
index=MultiModalVectorStoreIndex.from_documents(documents,storage_context=storage_context)
engine=index.as_query_engine(llm=llm)
response=engine.query("what you see in the images?")
print(response)