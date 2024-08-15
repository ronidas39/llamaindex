from llama_index.core import VectorStoreIndex
from llama_index.readers.google import GoogleDocsReader

doc_ids=["1NfsiWi1JWLf7XXvNW763UTI_lu4WrSxjRJkc_jRDpts",
         "1sfXDhIW65Hw0K_MHGycEzzf03wens8eIFixaeEX7bBM",
         "1kaZfceu_hKBPZjGuXr2GpL-A3-sU1nWHs3Eqla05zrM",
         "1_gTEygYH4EdP1gQjcmtUQFHf_dbgkE8chki5scoAw98"]
loader=GoogleDocsReader()
documents=loader.load_data(document_ids=doc_ids)
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
response=query_engine.query("How can progressive overload be effectively applied in a resistance training program to maximize muscle hypertrophy while minimizing fat gain?")
print(response)