import streamlit as st
from PIL import Image, ImageFilter
import os

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="Bilelikde", page_icon="❤️")

# НОВЫЙ КРЕАТИВНЫЙ ДИЗАЙН
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
        font-size: 3rem !important;
    }
    [data-testid="stVerticalBlock"] > div:has(img) {
        background: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white !important;
        border-radius: 50px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ВАШЕ ОБЩЕЕ ФОТО (ЛОГОТИП)
if os.path.exists("we.jpg"):
    st.image("we.jpg", use_column_width=True)

st.markdown("<h1>SAHYGUW</h1>", unsafe_allow_html=True)

# 3. ТЕМА ДНЯ
st.info("📍 **Тема дня:** Бокал сверху (ракурс 90°)")

# Инициализация сессии
if 'p1' not in st.session_state: st.session_state.p1 = None
if 'p2' not in st.session_state: st.session_state.p2 = None

c1, c2 = st.columns(2)

with c1:
    st.write("🤵 **Муж**")
    if st.session_state.p1 is None:
        f1 = st.file_uploader("Твой кадр", key="f1")
        if f1: 
            st.session_state.p1 = f1
            st.rerun()
    else:
        img1 = Image.open(st.session_state.p1)
        if st.session_state.p2 is None:
            st.image(img1.filter(ImageFilter.GaussianBlur(radius=30)), caption="Ожидание...")
        else:
            st.image(img1)

with c2:
    st.write("👰 **Жена**")
    if st.session_state.p2 is None:
        f2 = st.file_uploader("Твой кадр", key="f2")
        if f2: 
            st.session_state.p2 = f2
            st.rerun()
    else:
        img2 = Image.open(st.session_state.p2)
        if st.session_state.p1 is None:
            st.image(img2.filter(ImageFilter.GaussianBlur(radius=30)), caption="Ожидание...")
        else:
            st.image(img2)

# 4. ФИНАЛ
if st.session_state.p1 and st.session_state.p2:
    st.balloons()
    if st.button("Сделать новый пазл"):
        st.session_state.p1 = None
        st.session_state.p2 = None
        st.rerun()
        
