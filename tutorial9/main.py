from llama_index.core import Settings,VectorStoreIndex,SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding

#GLOBAL CONFIG
Settings.embed_model=OpenAIEmbedding()
#using var
embed_model=OpenAIEmbedding()

documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents,embed_model=embed_model)
engine=index.as_query_engine()
response=engine.query("What potential applications of smart contracts do you find most promising, and how do you think they could impact your industry?")
print(response)


# embeddings_text=embed_model.get_text_embedding("hello this roni")
# print(embeddings_text)