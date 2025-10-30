import streamlit as st
from google import genai

def main():
    st.title('💬 Gemini 챗봇')

    # Gemini 클라이언트 초기화
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    # 세션 상태에 메시지 저장
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 이전 메시지 출력
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 사용자 입력 받기
    user_input = st.chat_input("질문을 입력하세요...")
    if user_input:
        # 사용자 메시지 저장 및 출력
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Gemini 모델로부터 응답 받기
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
        )

        # Gemini 응답 저장 및 출력
        bot_reply = response.text
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

if __name__ == '__main__':
    main()
