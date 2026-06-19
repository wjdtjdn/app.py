import streamlit as st
import datetime

# 1. 페이지 기본 설정 (네이버 감성의 와이드 레이아웃 및 타이틀)
st.set_page_config(
    page_title="Naver Mind - 스마트폰 중독 예방 포털",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 고정 스타일 정의 (네이버 시그니처 그린 컬러 및 UI 스타일링)
st.markdown("""
    <style>
    .naver-header {
        font-size: 42px;
        font-weight: 900;
        color: #03C75A;
        font-family: 'Malgun Gothic', sans-serif;
        text-align: center;
        margin-bottom: 5px;
    }
    .naver-sub {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-bottom: 25px;
    }
    .ad-box {
        background-color: #f8f9fa;
        border: 1px solid #dae1e6;
        padding: 15px;
        border-radius: 4px;
        text-align: center;
        margin-bottom: 20px;
    }
    .ad-title {
        font-size: 11px;
        color: #888;
        text-align: left;
        margin-bottom: 5px;
    }
    .news-title {
        font-weight: bold;
        font-size: 16px;
        color: #222;
        border-bottom: 2px solid #03C75A;
        padding-bottom: 8px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 상단 레이아웃 (네이버 로고 및 검색창) ---
st.markdown('<div class="naver-header">NAVER Mind</div>', unsafe_allow_html=True)
st.markdown('<div class="naver-sub">스마트폰을 내려놓고, 진짜 나의 삶을 검색해보세요.</div>', unsafe_allow_html=True)

# 검색창 기능 (네이버 스타일 검색 바)
search_query = st.text_input("🔍 디지털 디톡스 관련 정보나 예방법을 검색해보세요!", placeholder="예: 스마트폰 중독 자가진단, 도파민 단식, 주말 취미 추천")

if search_query:
    st.info(f"💡 '{search_query}'에 대한 통합검색 결과: 스마트폰 사용을 줄이기 위해 현재 화면을 끄고 5분간 스트레칭을 해보는 건 어떨까요?")

st.markdown("---")

# --- 메인 콘텐츠 영역 (3단 분할로 네이버 느낌 재현) ---
col1, col2, col3 = st.columns([2, 3, 2])

# [왼쪽 열: 각종 뉴스 및 칼럼]
with col1:
    st.markdown('<div class="news-title">📰 데일리 디톡스 뉴스</div>', unsafe_allow_html=True)
    
    news_list = [
        ("IT", "⚠️ '화면 너머의 세상'… 청소년 스마트폰 중독 심각성 경고", "https://www.nia.or.kr"),
        ("건강", "👁️ 거북목과 안구건조증, 하루 스마트폰 3시간만 줄여도 완화", "https://www.khidi.or.kr"),
        ("사회", "🧘 빌 게이츠도 실천하는 '자녀 스마트폰 제한 규칙'의 비밀", "https://www.unicef.or.kr"),
        ("문화", "📚 '숏폼 대신 롱폼'… 서점가에 부는 '책 읽기 챌린지' 열풍", "https://www.nl.go.kr")
    ]
    
    for category, title, link in news_list:
        st.caption(f"[{category}]")
        st.markdown(f"[{title}]({link})")
        st.markdown("<div style='margin-bottom:10px;'></div>", unsafe_allow_html=True)

# [중앙 열: 메인 기능 - 스마트폰 중독 자가진단]
with col2:
    st.markdown('<div class="news-title">📊 1분 스마트폰 중독 자가진단</div>', unsafe_allow_html=True)
    
    # 렉 방지를 위해 st.form 적용
    with st.form(key='diagnosis_form'):
        q1 = st.checkbox("1. 스마트폰이 없으면 불안하거나 초조하다.")
        q2 = st.checkbox("2. 스마트폰 사용 시간을 줄이려고 시도했으나 실패했다.")
        q3 = st.checkbox("3. 화장실에 갈 때도 스마트폰을 반드시 챙긴다.")
        q4 = st.checkbox("4. 스마트폰 때문에 학업이나 업무에 지장이 있다.")
        q5 = st.checkbox("5. 밤늦게까지 스마트폰을 하느라 잠을 설친다.")
        
        submit_button = st.form_submit_button(label='결과 확인하기')
        
    if submit_button:
        score = sum([q1, q2, q3, q4, q5])
        if score >= 4:
            st.error(f"🚨 위험 ({score}/5점): 스마트폰 의존도가 매우 높습니다! 지금 바로 의도적인 스크린타임 제한이 필요합니다.")
        elif score >= 2:
            st.warning(f"⚠️ 주의 ({score}/5점): 조금씩 중독 증상이 나타나고 있습니다. 주말 하루는 '폰 없는 날'로 지정해보세요.")
        else:
            st.success(f"✅ 안전 ({score}/5점): 건강한 디지털 라이프를 유지하고 계시네요! 지금처럼만 유지하세요.")

# [오른쪽 열: 배너 광고 및 바로가기 사이트]
with col3:
    # 광고 영역 (네이버 우측 배너 감성)
    st.markdown("""
        <div class="ad-box">
            <div class="ad-title">AD</div>
            <h4 style="color: #333; margin: 5px 0;">📱 스마트폰은 잠시 OFF</h4>
            <p style="font-size: 13px; color: #666;">숲 속을 걷는 듯한 온전한 휴식<br><b>'디지털 디톡스 템플스테이'</b> 신청 중</p>
            <a href="https://www.templestay.com" target="_blank">
                <button style="background-color: #03C75A; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 12px;">자세히 보기</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    # 게임/대안 활동 사이트 바로가기
    st.markdown('<div class="news-title">🎮 스마트폰 대신 할 수 있는 곳</div>', unsafe_allow_html=True)
    st.markdown("📱 **스마트폰 게임 대신 두뇌를 쓰는 건전한 대안 사이트 리스트입니다.**")
    
    st.link_button("🧩 스도쿠/퍼즐 게임 하러가기", "https://www.websudoku.com/")
    st.link_button("🌐 스마트폰 중독 상담 (스마트쉼센터)", "https://www.iapc.or.kr/")
    st.link_button("🏃 국민체력 100 (운동 루틴 찾기)", "https://nfa.kspo.or.kr/")

# --- 하단 푸터 (네이버 푸터 스타일 및 최하단 unsafe_allow_html 수정완료) ---
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: #888; font-size: 12px;'>"
    f"Copyright © <b>NAVER Mind Corp.</b> All Rights Reserved. (현재 접속 시간: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})"
    f"</div>", 
    unsafe_allow_html=True
)
