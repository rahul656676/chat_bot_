from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from groq import Groq

# ---------------- GROQ CLIENT ----------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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

st.set_page_config(
    page_title="Chat Bot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right, #141e30, #243b55);
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
}

.sub-title{
    text-align:center;
    color:#d3d3d3;
    margin-bottom:30px;
}

.stTextInput > div > div > input{
    background:white;
    color:black;
    border-radius:10px;
}

.stButton button{
    width:100%;
    border-radius:10px;
    background: linear-gradient(to right,#00c6ff,#0072ff);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.response-box{
    background:rgba(255,255,255,0.1);
    padding:20px;
    border-radius:10px;
    color:white;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🤖 Chat Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Powered by Groq AI</div>',
    unsafe_allow_html=True
)

input = st.text_input(
    "Ask Anything",
    placeholder="Type your question here..."
)

submit = st.button("Ask your query")

if submit:

    if input:

        with st.spinner("Thinking..."):

            try:

                response = my_output(input)

                st.markdown(
                    f"""
                    <div class="response-box">
                    <h3>AI Response</h3>
                    {response}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error("API limit reached 😅 Try again later.")
                st.code(str(e))

    else:
        st.warning("Please enter a question.")