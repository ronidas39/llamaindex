from llama_index.readers.web import WholeSiteReader
from llama_index.core import VectorStoreIndex,download_loader

scraper=WholeSiteReader(
    prefix="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/",
    max_depth=2
)
documents=scraper.load_data(
    base_url="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/"
)
index=VectorStoreIndex.from_documents(documents)
ending=index.as_query_engine()
