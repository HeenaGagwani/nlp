import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=st.secrets["OPENAI_MODEL"],  # or whichever model you're using
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

