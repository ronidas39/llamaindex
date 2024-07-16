from llama_index.core import SimpleDirectoryReader
from llama_index.multi_modal_llms.openai import OpenAIMultiModal

llm=OpenAIMultiModal(model="gpt-4o")
images=SimpleDirectoryReader("images").load_data()
response=llm.complete(prompt="count the female and male in the images?",image_documents=images)
print(response)