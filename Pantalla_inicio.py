import streamlit as st
# Ahora importamos de la manera limpia y oficial
try:
    import V3 as lib_v3
except ImportError:
    st.error("No se pudo encontrar el archivo V3.py en la raíz del repositorio.")

# Configuración de la página
st.set_page_config(page_title="Mi App Pro", layout="centered")

st.title("Welcome back! 👋")
st.subheader("Panel de Control - Proyecto-X")

# Separador visual
st.divider()

# Creamos la cuadrícula de 2x2 para los botones
col1, col2 = st.columns(2)

with col1:
    # BOTÓN: CREAR NUEVO ESCENARIO
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        st.write("Accediendo a la librería V3...")
        
        # Aquí ya puedes llamar a tus funciones directamente
        # Ejemplo: resultado = lib_v3.tu_funcion_aqui()
        st.success("✅ Librería V3 conectada y ejecutada.")

    if st.button("📊 Datos maestros", use_container_width=True):
        st.info("Cargando base de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Consultando logs anteriores...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Abriendo agenda...")

st.divider()
