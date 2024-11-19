

from llama_index.readers.google import GoogleMapsTextSearchReader
from llama_index.core import VectorStoreIndex,Settings
from llama_index.llms.openai import OpenAI

Settings.chunk_size=2000

loader=GoogleMapsTextSearchReader(api_key="AIzaSyDY9FDv8ZpyUaiq_qtp7wK4yPxWZMlGcqQ")
docs=loader.load_data(
    text="things to do in Dubai",
    number_of_results=100
    )
print(docs)
index=VectorStoreIndex.from_documents(docs)
engine=index.as_query_engine(llm=OpenAI(model="gpt-4o"))
response=engine.query("which place is most expensive?")
print(response)