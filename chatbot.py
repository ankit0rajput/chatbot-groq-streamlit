from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

#streamlit page page setup

st.set_page_config(
    page_title="Chatbot",
    page_icon="",
    layout="centered"
)

st.title("AI chatbot")

#initiate chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



#show chat histiry
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])


#llm 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature= 0.0
)

user_input = st.chat_input("Ask: ")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role":"user","content":user_input})
    response = llm.invoke(
        input=[{"role":"system","content":"you are a helpful assistant"},*st.session_state.chat_history]
    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)