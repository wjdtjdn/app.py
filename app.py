import streamlit as st
import google.generativeai as genai

# --- 1. 페이지 설정 ---
st.set_page_config(page_title="연애 상담 챗봇", page_icon="💖")
st.title("💖 마음을 들어주는 연애 상담소")
st.caption("당신의 연애 고민을 편하게 이야기해주세요. 따뜻하고 현실적인 조언을 해드릴게요!")

# --- 2. API 키 설정 (Streamlit Secrets 사용) ---
# Secrets에 키가 없는 경우를 위한 오류 처리
if "GEMINI_API_KEY" not in st.secrets:
    st.error("🔑 API 키가 설정되지 않았습니다. Streamlit Cloud 설정에서 Secrets를 추가해주세요.")
    st.stop()

# Gemini API 설정
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. 모델 설정 및 초기화 ---
# 시스템 지침(System Instruction)을 통해 챗봇의 성격 부여
system_instruction = """
당신은 따뜻하고 공감 능력이 뛰어난 연애 상담사입니다. 
내담자의 감정에 깊이 공감하되, 현실적이고 도움이 되는 조언을 부드럽게 전달해주세요. 
친근하고 다정한 말투(해요체)를 사용하고, 너무 길지 않게 대화하듯 답변해주세요.
"""

# gemini-2.5-flash-lite 모델 인스턴스 생성
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction=system_instruction
)

# --- 4. 세션 상태 초기화 (대화 기록 유지) ---
# 모델의 자체 채팅 객체(문맥 유지용)와 UI 표시용 메시지 리스트를 각각 저장
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = []

# 기존 대화 기록을 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. 사용자 입력 및 챗봇 응답 처리 ---
if prompt := st.chat_input("연애 고민을 적어주세요..."):
    
    # 1) 사용자 메시지를 UI에 표시하고 세션에 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2) Gemini API 호출 및 응답 출력 (오류 처리 포함)
    with st.chat_message("assistant"):
        try:
            # 대화 문맥을 유지하며 메시지 전송
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
            
            # 모델의 응답을 세션에 저장
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            # API 호출 실패, 네트워크 오류 등의 예외 처리
            st.error("앗, 답변을 생성하는 중에 문제가 발생했어요. 😢")
            st.warning(f"오류 내용: {e}")
            st.info("잠시 후 다시 시도해주시거나, API 키가 유효한지 확인해주세요.")
