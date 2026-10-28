from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("LangChain Demo with gemma2:2b")
input_text = st.text_input("Enter your question here:")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond to the question asked."),
        ("user", "Question:{question}")
    ]
)

llm = ChatOllama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
