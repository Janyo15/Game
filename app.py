import streamlit as st
import time

st.set_page_config(page_title="Anuncio Good Taste", page_icon="🎉", layout="centered")

st.markdown(
    """
    <style>
    .centered {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        color: white;
        background: linear-gradient(45deg, #ff0057, #ff7b00);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.3);
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='centered'><h1>🎉 ¡Hola aguacate! 🎉</h1><h3>¿como es pa jugar? estas linda hoy.</h3></div>", unsafe_allow_html=True)

with st.spinner("Cargando animación..."):
    time.sleep(2)

st.balloons()
