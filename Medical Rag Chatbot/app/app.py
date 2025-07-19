import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import streamlit as st
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.retriever import create_qa_chain

load_dotenv()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.set_page_config(page_title="QA Chatbot", layout="centered")

# UI
st.title("🧠 QA Chatbot")
st.markdown("Ask me anything related to the knowledge base!")

# Message display
for msg in st.session_state["messages"]:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Assistant"
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Append user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        qa_chain = create_qa_chain()
        if qa_chain is None:
            raise Exception("QA chain could not be created (LLM or VectorStore issue)")

        formatted_conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state["messages"]])
        combined_query = f"Previous conversation:\n{formatted_conversation}\n\nQuestion:\n{user_input}"
        response = qa_chain.invoke({"query": combined_query})
        result = response.get("result", "No response")
        
        # Append assistant response
        st.session_state["messages"].append({"role": "assistant", "content": result})
        with st.chat_message("assistant"):
            st.markdown(result)

    except Exception as e:
        error_msg = f"🚨 Error: {str(e)}"
        st.error(error_msg)

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state["messages"] = []
    st.rerun()
