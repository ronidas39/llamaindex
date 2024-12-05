from llama_index.core import SimpleDirectoryReader,StorageContext,VectorStoreIndex
from llama_index.vector_stores.elasticsearch import ElasticsearchStore

# loader=SimpleDirectoryReader(input_files=["/Users/roni/Documents/GitHub/llamaindex/tutorial38/2411.13585v1.pdf"])
# docs=loader.load_data()
es=ElasticsearchStore(
               index_name="tutorial38",
               es_api_key="UHoxVmxwTUJEQ3premt2dURGLTc6c1hpN2dpbmlRd2lPcGd2RmM4Z2xRZw==",
               es_cloud_id="My_deployment:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbSRiMDExY2ZlODU0NDk0OTFmOWI1MmY3MWVlNTMzOWY0YyRmYThjNDFjM2MwOGM0YjM2YTUyNGZjOTI4NTUxZjY5Yw=="
               )
# sc=StorageContext.from_defaults(vector_store=es)
# index=VectorStoreIndex.from_documents(docs,storage_context=sc)


index=VectorStoreIndex.from_vector_store(vector_store=es)
qe=index.as_query_engine()
response=qe.query("write few use cases from the topic?")
print(response)
es.close()