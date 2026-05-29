# app.py
# 오늘의 옷 추천 앱 (Streamlit)
# 필요한 설치:
# pip install streamlit requests

import streamlit as st
import requests
import random

st.set_page_config(page_title="오늘의 옷 추천", page_icon="👕")

st.title("👕 오늘의 옷 추천 앱")
st.write("날씨와 요즘 스타일 느낌을 반영해서 코디를 추천해줘!")

# 사용자 입력
user_input = st.text_input(
    "오늘의 기분이나 원하는 느낌 입력",
    placeholder="예: 꾸안꾸, 힙한 느낌, 데이트룩"
)

# 날씨 가져오기 함수
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        data = requests.get(url).json()

        temp = int(data["current_condition"][0]["temp_C"])
        weather = data["current_condition"][0]["weatherDesc"][0]["value"]

        return temp, weather

    except:
        return None, None


# 코디 추천 함수
def recommend_outfit(temp, mood):

    if temp >= 28:
        outfit = {
            "상의": "오버핏 반팔 티셔츠",
            "하의": "나일론 반바지",
            "양말": "발목 양말",
            "신발": "러닝화",
            "악세서리": "실버 목걸이",
            "모자": "볼캡",
            "선글라스": "블랙 선글라스",
            "패션용 안경": "얇은 뿔테 안경",
            "헤어스타일": "내추럴 웨이브"
        }

    elif temp >= 20:
        outfit = {
            "상의": "반팔 니트",
            "하의": "와이드 데님 팬츠",
            "양말": "스트라이프 양말",
            "신발": "독일군 스니커즈",
            "악세서리": "가죽 시계",
            "모자": "버킷햇",
            "선글라스": "브라운 틴트 선글라스",
            "패션용 안경": "메탈 안경",
            "헤어스타일": "가르마 스타일"
        }

    elif temp >= 10:
        outfit = {
            "상의": "후드집업",
            "하의": "카고 팬츠",
            "양말": "스포츠 양말",
            "신발": "뉴발란스 운동화",
            "악세서리": "비즈 팔찌",
            "모자": "비니",
            "선글라스": "투명 안경",
            "패션용 안경": "블랙 뿔테",
            "헤어스타일": "다운펌 스타일"
        }

    else:
        outfit = {
            "상의": "패딩 + 니트",
            "하의": "기모 조거팬츠",
            "양말": "두꺼운 양말",
            "신발": "부츠",
            "악세서리": "머플러",
            "모자": "니트 비니",
            "선글라스": "다크 선글라스",
            "패션용 안경": "라운드 안경",
            "헤어스타일": "볼륨펌"
        }

    # 사용자가 입력한 분위기 반영
    if mood:
        outfit["추가 스타일"] = f"{mood} 느낌으로 연출 추천"

    return outfit


# 추천 버튼
if st.button("코디 추천받기 👗"):

    city = "Seoul"

    temp, weather = get_weather(city)

    if temp is None:
        st.error("날씨 정보를 불러오지 못했어 😢")

    else:
        st.subheader(f"📍 현재 날씨")
        st.write(f"도시: {city}")
        st.write(f"기온: {temp}°C")
        st.write(f"날씨: {weather}")

        outfit = recommend_outfit(temp, user_input)

        st.subheader("✨ 오늘의 추천 코디")

        for key, value in outfit.items():
            st.write(f"**{key}** : {value}")

        tips = [
            "오늘은 신발 색을 포인트로 주면 좋아!",
            "악세서리는 과하지 않게 1~2개 추천!",
            "상의가 심플하면 바지로 포인트 주기 👍",
            "실버 악세서리가 요즘 트렌드야 ✨"
        ]

        st.subheader("🔥 스타일 팁")
        st.write(random.choice(tips))
