import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="반장 도우미 챗봇",
    page_icon="📚"
)

# API 키 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

except Exception as e:
    st.error("API 키를 불러올 수 없습니다.")
    st.stop()

st.title("📚 반장 도우미 챗봇")
st.caption("반장 업무를 대신 정리하고 도와주는 AI 챗봇")

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 채팅 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("질문을 입력하세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 대화 기록 구성
        conversation = """
당신은 학교 반장을 도와주는 AI 챗봇입니다.

주요 역할:
- 공지문 작성
- 학급 행사 계획
- 역할 분담 정리
- 일정 관리
- 선생님께 보낼 메시지 작성
- 반 친구들에게 전달할 안내문 작성

친절하고 간결하게 답변하세요.

대화 내용:
"""

        for msg in st.session_state.messages:
            role = "사용자" if msg["role"] == "user" else "챗봇"
            conversation += f"\n{role}: {msg['content']}"

        response = model.generate_content(conversation)

        answer = response.text

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        error_message = f"오류가 발생했습니다.\n\n{str(e)}"

        st.session_state.messages.append(
            {"role": "assistant", "content": error_message}
        )

        with st.chat_message("assistant"):
            st.error(error_message)
