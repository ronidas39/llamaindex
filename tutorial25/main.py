from llama_index.core.query_engine import JSONalyzeQueryEngine
from readjson import readfile
from llama_index.llms.openai import OpenAI

llm=OpenAI(model="gpt-4o")
query_engine=JSONalyzeQueryEngine(
    list_of_dict=readfile(r"C:\Users\welcome\OneDrive\Documents\GitHub\llamaindex\tutorial25\employees_simple.json"),
    llm=llm,
    verbose=True
)
response=query_engine.query("list top 15 email and department,vacation days in ascending order as per vacation days")
print(response)