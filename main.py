from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI #chat비서2 - 대화형
chat_model = ChatOpenAI()

import streamlit as st
st.title("디지털 정보창  "+chat_model.model_name)

subject = st.text_input("알고 싶은것 입력해주세요.")

if st.button("궁금증 해결해줘", type="secondary",icon="🔥"):
    with st.spinner("Wait for it...", show_time=True):
    # with st.spinner("Wait for it..."):
        response = chat_model.invoke(subject+"에 대해 설명해줘")
        st.write(response.content)
        # print(chat_model.model_name)
