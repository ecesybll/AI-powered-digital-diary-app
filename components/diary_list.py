import streamlit as st
from services.diary_service import get_entries

def render_diary_list():
    st.header("Günlüklerim")
    entries = get_entries()
    if not entries:
        st.info("Henüz günlük eklenmedi.")
        return
    for entry in entries:
        with st.expander(f"{entry.date} - {entry.title}"):
            st.write(f"**Ruh Hali:** {entry.mood}  ")
            st.write(f"**Hava:** {entry.weather}  ")
            st.write(f"**Etiketler:** {', '.join(entry.tags) if entry.tags else '-'}  ")
            st.write(f"**Kelime Sayısı:** {entry.word_count}")
            st.write(entry.content)
