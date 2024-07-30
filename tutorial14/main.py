from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate

llm=OpenAI(model="gpt-4o")
documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents)
template_str="""
with this given {context_str} you have to answer the below
{query_str}, use the context only to answer , if context is not helpful just write no context found
"""
text_qa_template=PromptTemplate(template_str)

#with out prompt
query_engine=index.as_query_engine(llm=llm)
response=query_engine.query("who is Cristiano Ronaldo?")
print(response)


#with prompt
query_engine=index.as_query_engine(text_qa_template=text_qa_template,llm=llm)
response=query_engine.query("who is Cristiano Ronaldo?")
print(response)