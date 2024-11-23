from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.tools import QueryEngineTool,ToolMetadata

llm=OpenAI(model="gpt-4o")

awsloader=SimpleDirectoryReader(input_files=["/Users/roni/Documents/GitHub/llamaindex/tutorial34/aws.pdf"])
awsdocs=awsloader.load_data()
awsindex=VectorStoreIndex.from_documents(awsdocs)
awsqe=awsindex.as_query_engine(similarity_top_k=4)

devopsloader=SimpleDirectoryReader(input_files=["/Users/roni/Documents/GitHub/llamaindex/tutorial34/devops.pdf"])
devopsdocs=devopsloader.load_data()
devopsindex=VectorStoreIndex.from_documents(devopsdocs)
devopsqe=devopsindex.as_query_engine(similarity_top_k=4)

qet=[
    QueryEngineTool(
    query_engine=awsqe, 
    metadata=ToolMetadata(name="awsdocs",description="provides information only on aws related questions"),
    ),
    QueryEngineTool(
    query_engine=devopsqe, 
    metadata=ToolMetadata(name="devopsdocs",description="provides information only on devops related questions"),
    )
]
agent_worker=FunctionCallingAgentWorker.from_tools(qet, llm=llm, verbose=True,allow_parallel_tool_calls=False)
agent=agent_worker.as_agent()
response=agent.chat("what are the benefits of using AWS")
print(response)