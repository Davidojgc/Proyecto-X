import streamlit as st
# IMPORTANTE: Importamos las funciones de tu archivo específico
import porcentajes_v3 as lib_porcentajes

# Configuración visual
st.set_page_config(page_title="Panel de Control", layout="centered")

st.title("Sistema de Gestión 👋")
st.subheader("Selecciona una acción para comenzar")

# Separador visual
st.markdown("---")

# Creación de la interfaz de botones
col1, col2 = st.columns(2)

with col1:
    # BOTÓN CON TU LIBRERÍA
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        st.info("Accediendo a la librería: porcentajes _versión_3.py...")
        
        # Llamamos a la función que vive en tu otro archivo
        resultado = lib_porcentajes.calcular_escenario_base()
        datos = lib_porcentajes.generar_grafico_escenario()
        
        st.success(resultado)
        st.line_chart(datos) # Ejemplo visual de que algo ocurrió

    if st.button("📊 Datos maestros", use_container_width=True):
        st.write("Abriendo panel de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Cargando registros anteriores...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Sincronizando fechas...")

st.markdown("---")
