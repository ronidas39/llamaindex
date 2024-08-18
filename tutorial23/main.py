from llama_index.readers.youtube_transcript import YoutubeTranscriptReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
links=["https://www.youtube.com/watch?v=K4Ze-Sp6aUE"]
loader=YoutubeTranscriptReader()
documents=loader.load_data(ytlinks=links)
index=VectorStoreIndex.from_documents(documents)
engine=index.as_query_engine(llm=OpenAI(model="gpt-4o"))
response=engine.query("give a diet plan from the context with step by step details")
print(response)
