import streamlit as st

def render_sidebar():
    st.sidebar.title("Dijital Günlük")
    st.sidebar.markdown("---")
    st.sidebar.info("Günlüklerini yaz, analiz et, istatistikleri keşfet!")
    st.sidebar.markdown("---")
    st.sidebar.write("[GitHub](https://github.com/) | [Yardım](#)")
