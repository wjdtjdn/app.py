프로젝트명: 스마트폰 중독 예방 앱

폴더 구조

smartphone_addiction_prevention/
│
├── app.py
├── requirements.txt
└── README.md

requirements.txt

streamlit

app.py

import streamlit as st
import json
import os
from datetime import datetime, date

DATA_FILE = "data.json"

def load_data():
if os.path.exists(DATA_FILE):
with open(DATA_FILE, "r", encoding="utf-8") as f:
return json.load(f)
return {
"limit": 60,
"used": 0,
"warning_date": ""
}

def save_data(data):
with open(DATA_FILE, "w", encoding="utf-8") as f:
json.dump(data, f)

data = load_data()

today = str(date.today())

# 다음날이 되면 경고 해제

if data["warning_date"] != today:
data["used"] = 0
data["warning_date"] = ""
save_data(data)

st.title("📵 스마트폰 중독 예방 앱")

st.write("하루 사용 시간을 설정하고 관리하세요.")

limit = st.number_input(
"하루 허용 사용 시간(분)",
min_value=1,
value=data["limit"]
)

data["limit"] = limit
save_data(data)

st.subheader("오늘 사용 시간")

minutes = st.number_input(
"사용한 시간 추가(분)",
min_value=0,
step=1
)

if st.button("사용 시간 기록"):
data["used"] += minutes

```
if data["used"] >= data["limit"]:
    data["warning_date"] = today

save_data(data)
st.rerun()
```

st.write(f"현재 사용 시간: {data['used']}분")
st.write(f"허용 시간: {data['limit']}분")

if data["warning_date"] == today:

```
st.error(
    "⚠️ 경고! 오늘 허용된 스마트폰 사용 시간을 초과했습니다."
)

st.markdown(
    '''
    # 🚫 사용 제한 상태

    오늘의 사용 시간을 초과했습니다.

    경고는 내일 자동으로 해제됩니다.

    스마트폰 대신 다음 활동을 추천합니다.

    - 산책하기
    - 독서하기
    - 운동하기
    - 가족과 대화하기
    '''
)
```

else:
st.success("✅ 정상 사용 중")

README.md

# 스마트폰 중독 예방 앱

## 기능

* 하루 사용 시간 설정
* 사용 시간 기록
* 사용 시간 초과 시 경고 표시
* 경고 상태 유지
* 다음날 자동 초기화

## 실행

pip install -r requirements.txt

streamlit run app.py

## 배포

1. GitHub에 업로드
2. Streamlit Community Cloud 로그인
3. New App 선택
4. GitHub 저장소 연결
5. app.py 선택
6. Deploy
