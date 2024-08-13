from s3fs import S3FileSystem
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
s3_fs=S3FileSystem()
reader=SimpleDirectoryReader(
    input_dir="llama-tutorial-aug",
    fs=s3_fs,
    recursive=True
)
documents=reader.load_data()
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("In what ways did King Solomon’s later years differ from the earlier part of his reign, and what were the consequences of these changes?")
print(response)