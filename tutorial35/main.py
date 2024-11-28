from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core import VectorStoreIndex
llm=OpenAI(model="gpt-4o")
embed_model=OpenAIEmbedding()
reader=DoclingReader()
node_parser=MarkdownNodeParser()
docs=reader.load_data("https://arxiv.org/pdf/2411.05442")
index=VectorStoreIndex.from_documents(documents=docs,transformations=[node_parser],embed_model=embed_model)