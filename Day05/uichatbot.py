import ollama
import streamlit as st
st.set_page_config(
    page_title="My Chatbot App",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #e0f7fa, #fff8e1);
}
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #8a2be2;
    padding: 20px;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #ff1493;
}
div.stButton > button {
    background: linear-gradient(90deg, #ff4081, #7c4dff);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fce4ec, #e8eaf6, #e0f2f1);
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">🌈 Welcome to My Chatbot App 🤖</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">✨ Chat • Ask • Explore • Have Fun ✨</div>',
    unsafe_allow_html=True
)
if "messages" not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.header("🧹 Chat Clear")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.success("🎉 Chat cleared successfully! ✨")
    st.header("😊 Personality")
    personalities = {
        "👶 Kid":
        "Answer the questions like you are explaining to a 5 year old kid. Give answer in 2 lines.",
        "😎 Friend":
        "Answer the question in friendly and casual manner. Give answer in 2 lines.",
        "🏠 Roommates":
        "Answer the question like roommates behave in hostel. Give answer in 2 lines."
    }
    personality = st.selectbox(
        "Select a personality",
        personalities.keys()
    )
    st.header("📂 File Upload")
    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt"]
    )
    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        content = uploaded_file.read().decode("utf-8")
        if st.button("👀 Display File"):
            st.write(content)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):

        st.write(msg["content"])
question = st.chat_input("💬 Ask the question")
if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("🤖 Loading..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": personalities[personality]
                }
            ]
            + st.session_state.messages
        )
        answer = response["message"]["content"]
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
    with st.chat_message("assistant"):
        st.write(answer)