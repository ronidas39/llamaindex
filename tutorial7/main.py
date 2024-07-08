from llama_index.core import KeywordTableIndex,SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

documents=SimpleDirectoryReader("data").load_data()
llm=OpenAI(model="gpt-4o")
index=KeywordTableIndex.from_documents(documents,llm=llm)
query_engine=index.as_query_engine()
response=query_engine.query("give some information on nlp")
print(response)