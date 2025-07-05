import streamlit as st
from components.sidebar import render_sidebar
from components.diary_form import render_diary_form
from components.diary_list import render_diary_list
from components.analytics_dashboard import render_analytics_dashboard
from config.database import init_db

# Arka plan tamamen görünsün, inputlar card gibi kutucuk olsun
st.markdown(
    """
    <style>
    body, .stApp {
        background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1500&q=80') no-repeat center center fixed !important;
        background-size: cover !important;
    }
    body::before, .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: none !important;
        z-index: 0;
    }
    .block-container {
        background: transparent !important;
        box-shadow: none !important;
        padding-top: 2rem;
    }
    .card-input {
        background: rgba(255,255,255,0.85);
        border-radius: 14px;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,0.10);
        padding: 1.2rem 1.5rem 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
    }
    .stButton>button {
        color: white;
        background: #ff9800;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: #e65100;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Dijital Günlük", layout="wide", initial_sidebar_state="expanded")

init_db()
render_sidebar()

PAGES = {
    "Günlük Yaz": render_diary_form,
    "Günlüklerim": render_diary_list,
    "Analiz & İstatistik": render_analytics_dashboard
}

selected_page = st.sidebar.radio("Sayfa Seç", list(PAGES.keys()))

with st.spinner("Yükleniyor..."):
    PAGES[selected_page]()
