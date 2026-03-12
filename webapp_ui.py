import streamlit as st
import time
from app.pinecone_store import search_query
from app.llm import generate_answer

st.set_page_config(page_title="HR Policy Assistant", page_icon="💼")

st.title("💼 HR Policy RAG Assistant")
st.write("Ask questions about company policies.")

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input box
prompt = st.chat_input("Ask a question...")

if prompt:

    # show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # retrieve context
    context = search_query(prompt)

    # generate answer
    answer = generate_answer(context, prompt)

    # assistant message container
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        # typewriter effect
        for word in answer.split():
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.03)

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})