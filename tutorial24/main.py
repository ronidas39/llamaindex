from llama_index.readers.web import NewsArticleReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
llm=OpenAI(model="gpt-4o")
reader=NewsArticleReader(use_nlp=True)
documents=reader.load_data(
    [
        "https://www.news18.com/cricket/csk-requests-bcci-to-retain-ms-dhoni-as-uncapped-player-for-ipl-2025-franchise-ceo-responds-9019222.html",
        "https://www.news18.com/cricket/extremely-hungry-to-turn-things-around-and-get-border-gavaskar-trophy-back-nathan-lyon-9019245.html"
    ]
)
index=VectorStoreIndex.from_documents(documents)
engine=index.as_query_engine(llm=llm)
response=engine.query("please summarise the contgext in few well written paragraphs")
print(response)