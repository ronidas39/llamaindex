from llama_index.core import SimpleDirectoryReader
from llama_index.core.prompts import PromptTemplate
from llama_index.llms.openai import OpenAI
llm=OpenAI(model="gpt-4o")
rawdata=SimpleDirectoryReader("data").load_data()
text=rawdata[0].text
template="""
you have understand the given {context} to answer the below
{qsn} in simple english
"""
promptTemplate=PromptTemplate(template)
prompt=promptTemplate.format(context=text,qsn="How does doping affect the electrical properties of semiconductors?")
response=llm.complete(prompt)
print(response)