# НОВЫЙ КРЕАТИВНЫЙ ДИЗАЙН
st.markdown("""
    <style>
    /* Градиентный фон для всего приложения */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Стиль заголовка */
    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-size: 3rem !important;
        padding-bottom: 20px;
    }

    /* Стиль карточек с фото */
    [data-testid="stVerticalBlock"] > div:has(img) {
        background: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border: 2px solid #ffffff;
    }

    /* Красивые кнопки */
    .stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white !important;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 65, 108, 0.6);
    }

    /* Текст темы дня */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.5) !important;
        border: none !important;
        border-left: 5px solid #ff416c !important;
        color: #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)
