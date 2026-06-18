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

# ---------------- CUSTOM CSS ----------------

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
    margin-top:20px;
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
    padding:10px;
}

.stButton button{
    width:100%;
    border-radius:10px;
    background: linear-gradient(to right,#00c6ff,#0072ff);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    padding:10px;
}

.response-box{
    background:rgba(255,255,255,0.1);
    padding:20px;
    border-radius:10px;
    color:white;
    margin-top:20px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">🤖 Chat Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Powered by Groq AI</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT ----------------

user_input = st.text_input(
    "Ask Anything",
    placeholder="Type your question here..."
)

submit = st.button("Ask your query")

# ---------------- RESPONSE ----------------

if submit:

    if user_input:

        with st.spinner("Thinking..."):

            try:

                response = my_output(user_input)

                st.markdown(
                    f"""
                    <div class="response-box">
                        <h3>AI Response</h3>
                        <p>{response}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error("Error occurred 😅")
                st.code(str(e))

    else:
        st.warning("Please enter a question.")