import streamlit as st
import importlib.util
import sys
from pathlib import Path

# --- FUNCIÓN PARA CARGAR LA LIBRERÍA DESDE LA SUB-CARPETA ---
def cargar_mi_libreria():
    # Detectamos la carpeta donde está este archivo (la raíz del proyecto)
    ruta_raiz = Path(__file__).parent
    
    # Construimos la ruta: Raíz -> Carpeta Proyecto-X -> Archivo
    # NOTA: Verifica si tu archivo es "porcentajes" o "procentajes" (sin r)
    ruta_archivo = ruta_raiz / "Proyecto-X" / "porcentajes_versión_3.py"
    
    # Verificamos si la ruta existe para evitar el error de "File not found"
    if not ruta_archivo.exists():
        st.error(f"❌ No se encontró el archivo en: {ruta_archivo}")
        return None

    try:
        # Carga dinámica del módulo
        spec = importlib.util.spec_from_file_location("modulo_porcentajes", str(ruta_archivo))
        mi_modulo = importlib.util.module_from_spec(spec)
        sys.modules["modulo_porcentajes"] = mi_modulo
        spec.loader.exec_module(mi_modulo)
        return mi_modulo
    except Exception as e:
        st.error(f"Error al ejecutar el código de la librería: {e}")
        return None

# Intentamos cargar la librería al inicio
lib_porcentajes = cargar_mi_libreria()

# --- INTERFAZ DE STREAMLIT ---
st.set_page_config(page_title="Mi App Pro", layout="centered")

st.title("Welcome back! 👋")
st.subheader("¿Qué quieres hacer hoy?")

col1, col2 = st.columns(2)

with col1:
    # BOTÓN: CREAR NUEVO ESCENARIO
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        if lib_porcentajes:
            st.success("Conectado a Proyecto-X/porcentajes_versión_3.py")
            # Aquí llamas a tus funciones, por ejemplo:
            # lib_porcentajes.tu_funcion()
        else:
            st.error("La librería no está disponible.")

    if st.button("📊 Datos maestros", use_container_width=True):
        st.info("Cargando base de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Consultando logs anteriores...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Abriendo agenda...")
