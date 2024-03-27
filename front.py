import streamlit as st
import chatbot_backend as demo
from mangum import Mangum

# Set Title for the Chatbot
st.title("Hi, This is assistant of my boss, Mr.KSK :sunglasses:")

# Initialize Chatbot memory using demo_memory function
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

# Initialize chat history if not already created
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.empty():
        st.write(f'{message["role"]}: {message["text"]}')

# Create a chat input box for user input
input_text = st.text_input("Enter your message here:")

if input_text:
    # Add user input to chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Get chatbot response using demo_conversation function
    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)

    # Add chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})

    # Display chatbot response
    st.write("Chatbot Anisha:", chat_response)

# Create Mangum handler for deploying the Streamlit app
handler = Mangum(st._server)
