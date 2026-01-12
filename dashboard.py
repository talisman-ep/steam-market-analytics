import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Steam Analytics", layout="wide")
st.title("🔫 Steam Market Dashboard (Demo)")

@st.cache_data
def load_data():
    df = pd.read_csv("steam_data.csv")
    return df

try:
    df = load_data()

    st.sidebar.header("Фільтри")
    search_skin = st.sidebar.text_input("Пошук скіна", "")
    
    if search_skin:
        df = df[df['skin_name'].str.contains(search_skin, case=False)]

    col1, col2, col3 = st.columns(3)
    col1.metric("Всього скінів", len(df))
    col2.metric("Найдорожчий скін", f"${df['price'].max():.2f}")
    col3.metric("Середня ціна", f"${df['price'].mean():.2f}")

    st.subheader("🏆 Топ-10 найдорожчих скінів")
    top_skins = df.sort_values(by="price", ascending=False).head(10)
    
    fig = px.bar(
        top_skins, 
        x="skin_name", 
        y="price", 
        title="Ціни на скіни",
        color="price"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Детальна таблиця")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Помилка: {e}")