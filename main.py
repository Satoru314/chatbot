import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory
from openai import AuthenticationError

st.title("こんにちわん！")

with st.sidebar:
    open_api_key = st.text_input("OpenAI API key プリーズ", type="password").strip()
    st.markdown("[OpenAI API Key](https://platform.openai.com/account)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"assistant","content":"写すの疲れたんご"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()

if prompt:
    if not open_api_key:
        st.info("APIキーがないよ!!")
        st.stop()
    st.session_state["messages"].append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    try:
        with st.spinner("お前のために回答作成中"):
            response = get_chat_response(prompt, st.session_state["memory"], openai_api_key=open_api_key)
            msg = {"role":"assistant","content":response}
            st.session_state["messages"].append(msg)
            st.chat_message("assistant").write(response)
    except AuthenticationError:
        st.error("APIキーが無効です。正しいキーを入力してください。")