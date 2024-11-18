from llama_index.llms.openai import OpenAI
from llama_index.readers.papers import ArxivReader
from llama_index.core import VectorStoreIndex

loader=ArxivReader()
docs=loader.load_data(search_query="LLM",max_results=5)
index=VectorStoreIndex.from_documents(docs)
engine=index.as_query_engine(llm=OpenAI(model="gpt-4o"))
response=engine.query("give summary in few paragraph from the given text")
print(response)