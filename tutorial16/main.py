from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
llm=OpenAI(model="gpt-4o")
documents=SimpleDirectoryReader("data").load_data()
parser=SentenceSplitter()
nodes=parser.get_nodes_from_documents(documents)
index=VectorStoreIndex(nodes)
engine=index.as_query_engine(llm=llm)
response=engine.query("How have welfare programs like Pradhan Mantri Ujjwala Yojana and Swachh Bharat Abhiyan impacted rural households in India?")
print(response)