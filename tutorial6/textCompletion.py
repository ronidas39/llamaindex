from llama_index.llms.openai import OpenAI

#non streaming
# response=OpenAI(model="gpt-4o").complete("India is a ")
# print(response)

# with streaming
llm=OpenAI(model="gpt-4o")
responses=llm.stream_complete("India is a ")
for response in responses:
    print(response.delta,end="")



