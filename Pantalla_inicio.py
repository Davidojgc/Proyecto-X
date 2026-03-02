import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi App Pro", layout="centered")

st.title("Welcome back! 👋")
st.subheader("¿Qué quieres hacer hoy?")

# Creamos una cuadrícula de 2x2 para los botones
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        st.write("Redirigiendo a Nuevo Escenario...")
        # Aquí puedes cambiar una variable de estado para moverte de página

    if st.button("📊 Datos maestros", use_container_width=True):
        st.info("Cargando base de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Consultando logs anteriores...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Abriendo agenda...")
