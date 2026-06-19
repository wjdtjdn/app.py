import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 초기화
st.set_page_config(
    page_title="스마트폰 정뚝떨 프로젝트",
    page_icon="🚫",
    layout="centered"
)

# 세션 상태 초기화 (CSS 스타일 제어용)
if "ugly_style" not in st.session_state:
    st.session_state.ugly_style = "normal"

# CSS 주입을 통한 화면 변형 기능 구현
if st.session_state.ugly_style == "monochrome":
    st.markdown("<style>html, body, [data-testid=\"stAppViewContainer\"] { filter: grayscale(100%) !important; }</style>", unsafe_allow_html=True)
elif st.session_state.ugly_style == "neon_hell":
    st.markdown("<style>html, body, [data-testid=\"stAppViewContainer\"] { background-color: #00ff00 !important; color: #ff00ff !important; font-family: 'Comic Sans MS', cursive !important; }</style>", unsafe_allow_html=True)

# 2. AI 기능 설정 (Secrets 예외 처리 포함)
ai_available = False
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        ai_available = True
    else:
        st.sidebar.warning("🔑 AI 기능을 쓰시려면 Secrets에 GEMINI_API_KEY를 등록해 주세요.")
except Exception as e:
    st.sidebar.error(f"API 로드 오류: {e}")

# --- 메인 화면 시작 ---
st.title("🚫 스마트폰 정뚝떨 프로젝트")
# st.subtitle 대신 안전한 마크다운 형태로 부제목 구현
st.markdown("##### **스마트폰 화면을 세상에서 가장 보기 싫게 만들어 중독을 치료하세요!**")
st.write("---")

# 기능 1: 화면 테러 시뮬레이터 (체험존)
st.header("🎨 1단계: 화면 매력도 떨어뜨리기 체험")
st.write("아래 버튼을 눌러 화면을 변형시켜 보세요. 스마트폰 흥미를 떨어뜨리는 효과를 직접 체감할 수 있습니다.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚫ 완전 흑백 모드"):
        st.session_state.ugly_style = "monochrome"
        st.sidebar.success("흑백 모드가 적용되었습니다!")
with col2:
    if st.button("🤢 눈 테러 형광 모드"):
        st.session_state.ugly_style = "neon_hell"
        st.sidebar.success("형광 모드가 적용되었습니다!")
with col3:
    if st.button("🔄 원래대로 되돌리기"):
        st.session_state.ugly_style = "normal"
        st.sidebar.success("정상 화면으로 복구되었습니다.")

st.info("💡 **실제 스마트폰 팁:** 아이폰/갤럭시의 '접근성' 설정에서 화면을 **그레이스케일(흑백)**로 바꾸는 것만으로도 도파민 분비가 확 줄어들어 폰을 덜 보게 됩니다.")
st.write("---")

# 기능 2: 나의 스마트폰 매력도 자가진단
st.header("📊 2단계: 내 폰은 얼마나 중독적인가?")
st.write("현재 본인의 스마트폰 상태를 체크해 보세요.")

app_count = st.slider
