import ollama
import streamlit as st
st.markdown(":rainbow[welcome to my chatbot app!!]")
with st.sidebar:
    st.header(":red[chat clear]")
    if st.button("clearchat "):
        st.session_state.messages=[]
        st.success("chat cleared successfully")
    personalities={
        "Kid":"Answer the questions like you are explaining to a 5 year kid.Give answer in 2 lines",
        "Friend":"Answer the question in friendly and casual manner.Give answer in 2 lines",
        "Rommates":"Answer the question how the roomates were behave in hostel.Give answer in 2 lines",
    }
    personality=st.selectbox("Select a personality",personalities.keys())    
    st.session_state.messages = []
    st.header("File Upload")
    uploaded_file = st.file_uploader("upload a text file")
    try:
        if uploaded_file:
            st.success("file uploaded successfully")
            content = uploaded_file.read().decode("utf-8")
            st.write(content)
            if st.button:
                st.write("display the file")
    except:
        st.error("sorry this file is not exixts")    
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("ask the question:")
if question:
    st.session_state.messages .append(
        {"role":"user",
         "content": question})
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Loading..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role":"system","content":personalities[personality]
                }
            ]
            +st.session_state.messages)
        st.session_state.messages .append(
            {"role":"assistant",
            "content":response["message"]["content"]}
        )
    with st.chat_message("assistant"):
            st.write("AI:",response["message"]["content"])