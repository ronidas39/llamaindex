from llama_index.core import SimpleDirectoryReader

loader=SimpleDirectoryReader("data",recursive=True,required_exts=[".pdf",".txt"],exclude=[r"C:\Users\welcome\OneDrive\Documents\GitHub\llamaindex\tutorial18\data\payslip_1.pdf"],)
#loader=SimpleDirectoryReader("data",recursive=True,input_files=[r"C:\Users\welcome\OneDrive\Documents\GitHub\llamaindex\tutorial18\data\data_insie\data_inside_1\sample_inside.txt"])

documents=loader.load_data()
for document in documents:
    print(document)
    print(document.metadata["file_name"],document.metadata["file_path"])