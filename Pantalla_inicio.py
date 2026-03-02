import streamlit as st
import importlib.util
import sys
from pathlib import Path

# --- FUNCIÓN DE CARGA DEFINITIVA ---
def cargar_mi_libreria():
    # En Streamlit Cloud, el archivo raíz es donde está Pantalla_inicio.py
    # Si porcentajes_versión_3.py está al mismo nivel, la ruta es solo el nombre del archivo.
    nombre_archivo = "porcentajes_versión_3.py"
    
    # Obtenemos la ruta absoluta del directorio actual
    directorio_actual = Path(__file__).parent.absolute()
    ruta_completa = directorio_actual / nombre_archivo

    # Depuración: Esto aparecerá en tu app para que veamos qué ve el servidor
    # st.write(f"Buscando archivo en: {ruta_completa}") 

    if not ruta_completa.exists():
        # Si falla, intentamos buscarlo sin la ruta absoluta (a veces necesario en ciertos contenedores)
        ruta_completa = Path(nombre_archivo)
        if not ruta_completa.exists():
            st.error(f"❌ No se encuentra '{nombre_archivo}'. Asegúrate de que el nombre en GitHub tiene la tilde exactamente igual.")
            return None

    try:
        # Carga del módulo con soporte para caracteres especiales
        spec = importlib.util.spec_from_file_location("modulo_porcentajes", str(ruta_completa))
        mi_modulo = importlib.util.module_from_spec(spec)
        sys.modules["modulo_porcentajes"] = mi_modulo
        spec.loader.exec_module(mi_modulo)
        return mi_modulo
    except Exception as e:
        st.error(f"Error al leer el contenido del archivo: {e}")
        return None

# Intentar cargar
lib_porcentajes = cargar_mi_libreria()

# --- INTERFAZ ---
st.set_page_config(page_title="Mi App Pro", layout="centered")

st.title("Welcome back! 👋")
st.subheader("Proyecto-X")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Crear nuevo escenario", use_container_width=True):
        if lib_porcentajes:
            st.success("✅ Librería cargada con éxito desde la raíz.")
            # Aquí puedes llamar a tus funciones: lib_porcentajes.tu_funcion()
        else:
            st.error("No se pudo conectar con la librería.")

    if st.button("📊 Datos maestros", use_container_width=True):
        st.info("Cargando base de datos...")

with col2:
    if st.button("📜 Historial", use_container_width=True):
        st.write("Consultando logs...")

    if st.button("📅 Calendario", use_container_width=True):
        st.write("Abriendo agenda...")
