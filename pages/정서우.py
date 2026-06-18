import random
import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="디지털 디톡스: 스마트폰 중독 진단",
    page_icon="📱",
    layout="centered",
)

# --- 세션 상태 초기화 ---
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False
if "random_mission" not in st.session_state:
    st.session_state.random_mission = ""

# --- 디지털 디톡스 미션 리스트 ---
MISSIONS = [
    "📱 식사할 때 스마트폰 보지 않고 음식 맛에 집중하기",
    "🛏️ 침대에 눕기 30분 전에는 스마트폰 멀리 두기",
    "🚶 1시간 동안 스마트폰 없이 산책하거나 가벼운 운동하기",
    "🔇 불필요한 앱 알림(특히 SNS) 모두 끄기",
    "📚 스마트폰 대신 책이나 잡지 10페이지 읽기",
    "🧼 스마트폰 화면 깨끗하게 닦고 1시간 동안 홈 화면 안 열기",
]

# --- 앱 타이틀 & 헤더 ---
st.title("📱 스마트폰 중독 진단 및 디톡스 케어")
st.markdown(
    """
    혹시 눈을 뜨자마자 스마트폰을 찾으시나요? 
    정확한 테스트를 통해 나의 스마트폰 과의존 상태를 확인하고, 맞춤형 디톡스 미션을 받아보세요!
    """
)
st.write("---")

# --- 테스트 문항 정의 ---
questions = [
    "1. 스마트폰 사용 시간을 줄이려고 시도해보았지만 실패한 적이 있다.",
    "2. 스마트폰이 옆에 없으면 불안하거나 초조해진다.",
    "3. 스마트폰 사용 때문에 계획했던 일(공부, 업무 등)을 미루거나 하지 못한다.",
    "4. 스마트폰을 하느라 밤을 새우거나 수면 부족을 겪은 적이 자주 있다.",
    "5. 스마트폰을 보지 않고 있을 때도 자꾸 알림이 온 것 같은 착각이 든다.",
    "6. 가족이나 친구와 함께 있는 시간에도 스마트폰을 자주 본다.",
    "7. 스마트폰 사용 시간을 스스로 통제하기 어렵다고 느낀다.",
    "8. 스마트폰이 없으면 일상생활(길 찾기, 계산 등)이 마비될 것 같다.",
    "9. 화장실에 갈 때 스마트폰을 챙기지 않으면 허전하고 불안하다.",
    "10. 스마트폰 사용으로 인해 목, 손목 통증 등 신체적 불편함을 느낀 적이 있다.",
]

# --- 설문지 폼 영역 ---
st.subheader("📋 자가 진단 테스트")
st.caption("※ 각 문항에 대해 솔직하게 답변해 주세요. (점수: 전혀 아니다 1점 ~ 매우 그렇다 4점)")

# 사용자 응답을 저장할 리스트
responses = []

with st.form(key="addiction_test_form"):
    for idx, q in enumerate(questions):
        response = st.radio(
            q,
            options=[1, 2, 3, 4],
            format_func=lambda x: {
                1: "전혀 아니다 (1점)",
                2: "아니다 (2점)",
                3: "그렇다 (3점)",
                4: "매우 그렇다 (4점)",
            }[x],
            index=1,  # 기본값: 아니다
            key=f"q_{idx}",
        )
        responses.append(response)

    # 제출 버튼
    submit_button = st.form_submit_button(label="📊 결과 분석하기")

# --- 결과 처리 영역 ---
if submit_button:
    st.session_state.test_submitted = True
    st.session_state.random_mission = random.choice(MISSIONS)

if st.session_state.test_submitted:
    total_score = sum(responses)
    max_score = len(questions) * 4
    min_score = len(questions) * 1

    st.write("---")
    st.subheader("📊 당신의 진단 결과")

    # 점수 시각화 (Progress Bar 계산을 위해 0~1 사이로 정규화)
    progress_val = (total_score - min_score) / (max_score - min_score)
    st.progress(progress_val)

    # 결과 분석 및 등급 지정
    if total_score <= 18:
        status = "🟢 안전 (스마트폰의 주인이십니다)"
        color = "green"
        jail_time = "0초"
        advice = "스마트폰을 매우 건강하게 사용하고 계십니다. 지금처럼 훌륭한 균형을 유지하세요!"
    elif total_score <= 28:
        status = "🟡 주의 (조금씩 중독의 늪으로...)"
        color = "orange"
        jail_time = "3
