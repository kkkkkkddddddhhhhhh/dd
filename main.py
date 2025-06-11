import streamlit as st
import pandas as pd

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv("subway_data.csv")

df = load_data()

st.title("지하철 엘리베이터 가까운 차량 찾기 🚇")

# 사용자 입력
station = st.selectbox("역 이름을 선택하세요", sorted(df['역이름'].unique()))
line = st.selectbox("호선을 선택하세요", sorted(df[df['역이름'] == station]['호선'].unique()))
direction = st.selectbox("방향을 선택하세요", sorted(df[(df['역이름'] == station) & (df['호선'] == line)]['방향'].unique()))

# 결과 필터링
result = df[(df['역이름'] == station) & (df['호선'] == line) & (df['방향'] == direction)]

if not result.empty:
    row = result.iloc[0]
    st.success(f"✅ 엘리베이터 위치: {row['엘리베이터위치']}")
    st.info(f"🚃 가장 가까운 차량칸: {row['가까운차량칸']}")
else:
    st.error("❌ 해당 정보가 없습니다.")

