import streamlit as st
from services.analytics_service import get_entry_stats, get_tag_trends
import pandas as pd

def render_analytics_dashboard():
    st.header("Analiz & İstatistikler")
    stats = get_entry_stats()
    tag_trends = get_tag_trends()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Toplam Günlük", stats['total_entries'])
        st.metric("Ortalama Kelime Sayısı", f"{stats['avg_word_count']:.1f}" if stats['avg_word_count'] else "-")
        st.bar_chart(pd.DataFrame.from_dict(stats['mood_stats'], orient='index', columns=['Adet']))
        st.caption("Ruh hali dağılımı")
    with col2:
        st.bar_chart(pd.DataFrame.from_dict(stats['weather_stats'], orient='index', columns=['Adet']))
        st.caption("Hava durumu dağılımı")
        if tag_trends:
            st.bar_chart(pd.DataFrame.from_dict(tag_trends, orient='index', columns=['Adet']))
            st.caption("Etiket trendleri")
        else:
            st.info("Etiket verisi yok.")
