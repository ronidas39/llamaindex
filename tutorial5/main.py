from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

# NON STREAMING

llm=OpenAI(model="gpt-4o")
# response=llm.chat([ChatMessage(role="user",content="write an essasy on LLM")])
# print(response)

#with streaming
response=llm.stream_chat([ChatMessage(role="user",content="write an essasy on LLM")])
for gen in response:
        print(gen.delta, end="", flush=True)