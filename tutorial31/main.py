from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
import numpy as np


llm=OpenAI(model="gpt-4o")

def multiply(a,b):
    """ multiply the given two numbers and return the result"""
    return a*b

def cosAngle(n):
    """find the cosine of the given angle and return the result"""
    return np.cos(n)

mt=FunctionTool.from_defaults(fn=multiply)
ct=FunctionTool.from_defaults(fn=cosAngle)
agent=ReActAgent.from_tools([mt,ct], llm=llm, verbose=True)
response=agent.chat("what the cosine of 76 degree")
print(response)