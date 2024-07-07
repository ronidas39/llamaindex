from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

llm=OpenAI(model="gpt-4o")
messages=[
    ChatMessage(role="system",content="you are a character from greek mythology"

    ),
    ChatMessage(role="user",content="what is your name?")
]
response=llm.chat(messages)
print(response)