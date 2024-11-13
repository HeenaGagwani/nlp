import streamlit as st
from query_handler import handle_query

# Page Config
st.set_page_config("Movies Bot", page_icon=":movie_camera:")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the Movie Recommendation Chatbot! Ask me about movies, actors, or anything related!"},
    ]

# Function to display chat messages
def write_message(role, content, save=True):
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

    # Save the message in session state if save is True
    if save:
        st.session_state.messages.append({"role": role, "content": content})

# Handle user query and response
def handle_submit(user_input):
    with st.spinner('Processing...'):
        response = handle_query(user_input)
        write_message('assistant', response)

# Display previous messages
for message in st.session_state.messages:
    write_message(message["role"], message["content"], save=False)

# Chat input for user
if user_input := st.chat_input("Ask me about movies, actors, or anything related!"):
    write_message('user', user_input)
    handle_submit(user_input)
