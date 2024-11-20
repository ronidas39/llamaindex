from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PandasCSVReader

parser=PandasCSVReader()
fe={".csv":parser}
loader=SimpleDirectoryReader("./",file_extractor=fe)
docs=loader.load_data()
for doc in docs:
    if doc.metadata['file_type']=="text/csv":
        print(doc.text)