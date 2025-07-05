import streamlit as st
from services.diary_service import add_entry
from models.database_models import Entry
from datetime import date
from services.gemini_service import analyze_text

def render_diary_form():
    st.markdown("<h2 style='color:#ff9800;'>Yeni Günlük Yaz</h2>", unsafe_allow_html=True)
    with st.form("diary_form"):
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        entry_date = st.date_input("Tarih", value=date.today())
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        title = st.text_input("Başlık")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        content = st.text_area("Günlük İçeriği", height=200)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        mood = st.selectbox("Ruh Hali", ["Mutlu", "Üzgün", "Stresli", "Nötr", "Heyecanlı", "Yorgun", "Diğer"])
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        weather = st.selectbox("Hava Durumu", ["Güneşli", "Yağmurlu", "Bulutlu", "Karlı", "Rüzgarlı", "Diğer"])
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        tags = st.multiselect("Etiketler", ["iş", "aile", "arkadaş", "sağlık", "spor", "hobiler", "öğrenme", "diğer"])
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-input">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            submitted = st.form_submit_button("Kaydet")
        with col2:
            ai_advice = st.form_submit_button("AI'dan Tavsiye Al")
        with col3:
            ai_emotion = st.form_submit_button("AI ile Duygu Analizi")
        st.markdown('</div>', unsafe_allow_html=True)
        if submitted:
            word_count = len(content.split())
            entry = Entry(
                id=None,
                date=str(entry_date),
                title=title,
                content=content,
                mood=mood,
                weather=weather,
                tags=tags,
                word_count=word_count
            )
            entry_id = add_entry(entry)
            st.success(f"Günlük kaydedildi! (ID: {entry_id})")
        if ai_advice and content.strip():
            with st.spinner("AI tavsiyesi alınıyor..."):
                prompt = f"Bir kullanıcı şu günlüğü yazdı: '{content}'. Ona gününü daha iyi geçirmek için kısa bir öneri ver."
                advice = analyze_text(prompt)
                st.info(f"AI Tavsiyesi: {advice}")
        elif ai_advice:
            st.warning("AI tavsiyesi için önce günlük içeriği girin.")
        if ai_emotion and content.strip():
            with st.spinner("AI duygu analizi yapıyor..."):
                prompt = f"Aşağıdaki günlük metninin duygusunu (ör: mutlu, üzgün, stresli, nötr, heyecanlı, yorgun, diğer) kısa ve net şekilde analiz et: '{content}'"
                emotion = analyze_text(prompt)
                st.info(f"AI Duygu Analizi: {emotion}")
        elif ai_emotion:
            st.warning("Duygu analizi için önce günlük içeriği girin.")
