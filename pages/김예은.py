import streamlit as st
import json
import os
from datetime import date

DATA_FILE = "data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass

    return {
        "limit": 60,
        "used": 0,
        "warning_date": ""
    }


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)


# 데이터 불러오기
data = load_data()

today = str(date.today())

# 날짜가 바뀌면 초기화
if data["warning_date"] and data["warning_date"] != today:
    data["used"] = 0
    data["warning_date"] = ""
    save_data(data)

st.set_page_config(
    page_title="스마트폰 중독 예방",
    page_icon="📵",
    layout="centered"
)

st.title("📵 스마트폰 중독 예방 앱")

st.write(
    "하루 사용 시간을 설정하고 관리하세요.\n"
    "제한 시간을 초과하면 경고가 표시되며 다음날까지 유지됩니다."
)

# 제한 시간 설정
limit = st.number_input(
    "하루 허용 사용 시간(분)",
    min_value=1,
    max_value=1440,
    value=int(data["limit"])
)

data["limit"] = limit
save_data(data)

st.divider()

st.subheader("오늘 사용 시간")

st.metric(
    label="현재 사용 시간",
    value=f"{data['used']}분"
)

add_time = st.number_input(
    "추가할 사용 시간(분)",
    min_value=1,
    max_value=300,
    value=10
)

if st.button("사용 시간 기록"):
    data["used"] += add_time

    if data["used"] >= data["limit"]:
        data["warning_date"] = today

    save_data(data)
    st.rerun()

st.divider()

# 경고 상태
if data["warning_date"] == today:
    st.error("⚠️ 경고! 오늘 허용 시간을 초과했습니다.")

    st.markdown("""
    ## 🚫 사용 제한 상태

    오늘 설정한 사용 시간을 초과했습니다.

    경고는 **다음날 자동으로 해제**됩니다.

    ### 추천 활동
    - 📚 독서하기
    - 🚶 산책하기
    - 🏃 운동하기
    - 🎨 그림 그리기
    - 👨‍👩‍👧 가족과 대화하기
    """)
else:
    remaining = max(0, data["limit"] - data["used"])

    st.success("✅ 정상 사용 중")

    st.info(f"남은 사용 가능 시간: {remaining}분")
