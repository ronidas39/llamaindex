from llama_index.llms.openai import OpenAI
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.tools import FunctionTool
import numpy as np

llm=OpenAI(model="gpt-4o")

def add(a,b):
    """ add the given numbers and return the result as output"""
    return a+b


def mul(a,b):
    """ multiply the given numbers and return the result as output"""
    return a*b

def div(a,b):
    """ divide the first number by the second and return the result as output"""
    return a/b

def cosa(n):
    """ find the cosine value of the given angle and return the result"""
    return np.cos(n)

at=FunctionTool.from_defaults(fn=add)
mt=FunctionTool.from_defaults(fn=mul)
dt=FunctionTool.from_defaults(fn=div)
ct=FunctionTool.from_defaults(fn=cosa)

agent_worker=FunctionCallingAgentWorker.from_tools([at,mt,dt,ct], llm=llm, verbose=True,allow_parallel_tool_calls=False)
agent=agent_worker.as_agent()
response=agent.chat("what is the value of (77*2+2) divided by 78 and once your get the value get the cosine of that")
print(response)