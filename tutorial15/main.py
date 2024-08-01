from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
import streamlit as st

st.write("condense chat app")
documents=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(documents)
chat_engine=index.as_chat_engine(chat_mode="condense_question",verbose=True)
input=st.text_input("ask your question")
if input is not None:
    btn=st.button("submit")
    if btn:
        response=chat_engine.stream_chat(input)
        st.write_stream(response.response_gen)