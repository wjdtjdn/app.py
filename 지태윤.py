import streamlit as tf
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="디지털 디톡스 챌린지",
    page_icon="📱",
    layout="centered"
)

# 2. 활동 데이터 정의 (카테고리별)
ACTIVITIES = {
    "🏃‍♂️ 신체 활동": [
        "동네 한 바퀴 산책하며 하늘 사진 찍기",
        "유튜브 없이 스트레칭이나 요가 15분 하기",
        "방 청소나 서랍 정리하며 미니멀리즘 실천하기",
        "가벼운 홈트레이닝(스쿼트, 플랭크) 세트 완료하기",
        "자전거 타고 한 번도 안 가본 길 가보기"
    ],
    "🎨 창작 및 취미": [
        "종이와 펜을 꺼내 눈앞에 있는 물건 데생하기",
        "미뤄뒀던 책이나 소설 읽기 (최소 10페이지)",
        "일기장에 오늘 하루의 감정이나 감사한 일 3가지 쓰기",
        "좋아하는 노래 플레이리스트 만들고 가사 음미하기",
        "손글씨로 친구나 가족에게 짧은 편지 쓰기"
    ],
    "🧠 휴식 및 자기계발": [
        "눈을 감고 5분간 온전히 호흡에만 집중하기(명상)",
        "외우고 싶었던 외국어 문장 5개 암기하기",
        "따뜻한 차나 커피를 내리고 향 맡으며 마시기",
        "이번 주 혹은 올해 버킷리스트 작성해보기",
        "밀린 영양제 챙겨 먹고 스트레칭하기"
    ]
}

# 3. UI 구성
st.title("📱 스마트폰 대신 뭐 하지?")
st.subheader("도파민 중독 탈출! 지금 당장 할 수 있는 활동을 추천해 드려요.")
st.write("---")

# 4. 기능 선택 (특정 카테고리 vs 전체 랜덤)
option = st.radio(
    "어떤 종류의 활동을 원하시나요?",
    ["🎲 완전 무작위! ([선택])", "🏃‍♂️ 신체 활동", "🎨 창작 및 취미", "🧠 휴식 및 자기계발"],
    index=0
)

st.write("")

# 5. 추천 버튼 및 로직
if st.button("⚡ 활동 추천받기", type="primary"):
    with st.spinner("어떤 활동이 좋을지 고민 중..."):
        # 선택에 따른 데이터 필터링
        if option == "🎲 완전 무작위! ([선택])":
            # 모든 카테고리의 리스트를 하나로 합침
            all_activities = sum(ACTIVITIES.values(), [])
            selected_activity = random.choice(all_activities)
        else:
            selected_activity = random.choice(ACTIVITIES[option])
        
        # 결과 출력
        st.balloons()
        st.success("🎉 오늘의 디톡스 활동을 추천합니다!")
        
        # 돋보이는 가독성을 위한 카드 형태 디자인
        st.info(f"### **{selected_activity}**")
        st.write("👉 지금 바로 스마트폰 화면을 끄고 이 활동에 집중해보세요!")

st.write("---")
st.caption("💡 Streamlit Community Cloud를 통해 배포된 디지털 디톡스 앱입니다.")
