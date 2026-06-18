import streamlit as st
from groq import Groq

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Chat Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- GROQ CLIENT ----------------

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ---------------- FUNCTION ----------------

def my_output(query):

    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role": "user",
                "content": query
            }
        ],

        model="llama-3.1-8b-instant",
        temperature=0.5,
        max_tokens=150
    )

    return chat_completion.choices[0].message.content

# ---------------- UI ----------------

st.title("🤖 AI Chat Bot")

user_input = st.text_input("Ask Anything")

if st.button("Ask"):

    if user_input:

        response = my_output(user_input)

        st.write(response)