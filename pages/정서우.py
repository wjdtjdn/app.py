import streamlit as st
import google.generativeai as genai

# 1. 페이지 기본 설정 및 스타일 초기화
st.set_page_config(
    page_title="스마트폰 정뚝떨 프로젝트",
    page_icon="🚫",
    layout="centered"
)

# 세션 상태 초기화 (CSS 스타일 제어용)
if "ugly_style" not in st.session_state:
    st.session_state.ugly_style = "normal"

# CSS 효과 반영을 위한 고정 주입
if st.session_state.ugly_style == "monochrome":
    st.markdown("<style>html, body, [data-testid=\"stAppViewContainer\"] { filter: grayscale(100%) !important; }</style>", unsafe_allow_html=True)
elif st.session_state.ugly_style == "neon_hell":
    st.markdown("<style>html, body, [data-testid=\"stAppViewContainer\"] { background-color: #00ff00 !important; color: #ff00ff !important; font-family: 'Comic Sans MS', cursive !important; }</style>", unsafe_allow_html=True)

# 2. API 키 설정 및 Gemini 초기화 (예외 처리 포함)
ai_available = False
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        ai_available = True
    else:
        st.sidebar.warning("🔑 Secrets에 GEMINI_API_KEY를 등록하면 AI 맞춤형 잔소리 기능을 사용할 수 있습니다.")
except Exception as e:
    st.sidebar.error(f"API 로드 중 오류 발생: {e}")

# --- 메인 화면 레이아웃 ---
st.title("🚫 스마트폰 정뚝떨(정두두둑) 프로젝트")
st.subtitle("스마트폰 화면을 세상에서 가장 보기 싫게 만들어 중독을 치료하세요!")
st.write("---")

# 기능 1: 화면 테러 시뮬레이터 (체험존)
st.header("🎨 1단계: 화면 매력도 떨어뜨리기 체험")
st.write("스마트폰 화면을 아래 버튼들을 눌러 변형시켜 보세요. 얼마나 보기 싫어지는지 체감할 수 있습니다.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚫ 완전 흑백 모드 (도파민 차단)"):
        st.session_state.ugly_style = "monochrome"
        st.rerun()
with col2:
    if st.button("🤢 눈 테러 형광 모드"):
        st.session_state.ugly_style = "neon_hell"
        st.rerun()
with col3:
    if st.button("🔄 원래대로 되돌리기"):
        st.session_state.ugly_style = "normal"
        st.rerun()

st.info("💡 **실제 스마트폰 꿀팁:** 아이폰/갤럭시의 '설정 -> 접근성'에서 화면을 **흑백(그레이스케일)**으로 바꾸는 것만으로도 스마트폰 흥미가 70% 이상 떨어집니다.")
st.write("---")

# 기능 2: 나의 스마트폰 매력도 자가진단
st.header("📊 2단계: 내 폰은 얼마나 중독적인가?")
st.write("현재 스마트폰 상태를 체크해보세요.")

app_count = st.slider("홈 화면에 나와있는 앱(아이콘)의 개수는?", 0, 50, 15)
has_red_badge = st.checkbox("앱 아이콘 위에 빨간색 알림 숫자(배지)가 항상 떠 있다.")
bright_wallpaper = st.checkbox("화려하고 밝은 연예인, 풍경, 캐릭터 배경화면을 쓰고 있다.")

if st.button("진단 결과 보기"):
    score = 0
    if app_count > 20: score += 30
    if has_red_badge: score += 40
    if bright_wallpaper: score += 30
    
    st.subheader(f"당신의 스마트폰 중독 유발 점수: **{score}점**")
    if score >= 70:
        st.error("🚨 위험! 당신의 폰은 뇌를 유혹하는 최적의 도파민 공장입니다. 당장 화면을 숨겨야 합니다!")
    elif score >= 40:
        st.warning("⚠️ 주의! 보기 좋은 떡이 먹기도 좋다고, 폰이 너무 예뻐서 자꾸 손이 가네요.")
    else:
        st.success("✅ 훌륭합니다! 상당히 지루한 형태의 폰을 유지하고 계시군요.")

st.write("---")

# 기능 3: AI 디톡스 잔소리 빌더 (Gemini 2.5 Flash Lite)
st.header("🤖 3단계: AI 맞춤형 '정뚝떨' 솔루션")
st.write("가장 끊기 힘든 앱이나 주 사용 목적을 입력하면, AI가 해당 화면을 꼴도 보기 싫게 만드는 기발한 방법을 처방해 드립니다.")

user_target_app = st.text_input("끊고 싶은 앱 이름이나 스마트폰 습관을 입력하세요:", placeholder="예: 인스타그램 릴스, 유튜브 쇼츠, 밤새 웹툰 보기")

if st.button("🤖 AI 처방전 받기"):
    if not ai_available:
        st.error("💡 AI 기능을 사용하려면 Streamlit Cloud의 Secrets에 `GEMINI_API_KEY`를 설정해야 합니다. (하단 가이드 참고)")
    elif not user_target_app.strip():
        st.warning("내용을 입력해 주세요!")
    else:
        with st.spinner("AI 의사 선생님이 독설 처방전을 작성 중입니다..."):
            try:
                # 규칙에 명시된 gemini-2.5-flash-lite 모델 사용
                model = genai.GenerativeModel("gemini-2.5-flash-lite")
                
                prompt = f"""
                사용자는 스마트폰 중독(특히 '{user_target_app}')에서 벗어나고 싶어합니다.
                스마트폰 화면이나 해당 앱을 '보기 싫고, 지루하고, 매력 없게' 만들어서 사용자가 폰을 닫게 만드는 기발하고 구체적인 솔루션 3가지를 제안해주세요.
                유머러스하면서도 약간의 독설을 섞어, 가독성 좋게 이모지를 섞어서 작성해주세요.
                """
                
                response = model.generate_content(prompt)
                
                st.subheader("💊 AI의 눈물 쏙 빼는 정뚝떨 처방전")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"AI 응답 생성 중 오류가 발생했습니다: {e}")
