from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import FunctionCallingAgentWorker
import requests


llm=OpenAI(model="gpt-4o")

def getPrice(token):
    """this function calls the coincap api to get the crypto price and return the price ass result"""
    url="https://api.coincap.io/v2/assets/"
    tokenName=token.lower()
    final_url=url+tokenName
    response=requests.get(final_url)
    price=response.json()["data"]["priceUsd"]
    return price


pt=FunctionTool.from_defaults(fn=getPrice)
agent_worker=FunctionCallingAgentWorker.from_tools([pt],llm=llm,verbose=True,allow_parallel_tool_calls=False)
agent=agent_worker.as_agent()
response=agent.chat("what is the price tesla")
print(response)