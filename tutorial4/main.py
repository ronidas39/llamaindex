from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.core.schema import MetadataMode
documents=SimpleDirectoryReader("data").load_data()

# for doc in documents:
#     print(doc.get_content(metadata_mode=MetadataMode.LLM))
#     print("\n\n")

index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("write a summary on The Impact of Artificial Intelligence")
print(response)