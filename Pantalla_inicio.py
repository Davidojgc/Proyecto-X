import streamlit as st
import importlib.util
import sys

# --- FUNCIÓN PARA CARGAR TU LIBRERÍA CON NOMBRE ESPECIAL ---
def cargar_mi_libreria():
    nombre_archivo = "porcentajes_versión_3.py"
    spec = importlib.util.spec_from_file_location("mi_modulo", nombre_archivo)
    mi_modulo = importlib.util.module_from_spec(spec)
    sys.modules["mi_modulo"] = mi_modulo
    spec.loader.exec_module(mi_modulo)
    return mi_modulo

# Cargamos la librería
lib_porcentajes = cargar_mi_libreria()

# --- CONFIGURACIÓN DE LA INTERFAZ ---
st.set_page_config(page_title="Mi App Pro", layout="centered")

st.title("Welcome back! 👋")
st.subheader("¿Qué quieres hacer hoy?")

col1, col2 = st.columns(2)

with col1:
    # BOTÓN: CREAR NUEVO ESCENARIO
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        st.write("Accediendo a la librería: porcentajes_versión_3...")
        
        # Aquí llamas a las funciones que tengas dentro de tu archivo
        # Ejemplo: resultado = lib_porcentajes.nombre_de_tu_funcion()
        st.success("Librería cargada correctamente.")

    if st.button("📊 Datos maestros", use_container_width=True):
        st.info("Cargando base de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Consultando logs anteriores...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Abriendo agenda...")
