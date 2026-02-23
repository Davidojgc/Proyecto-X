import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Carga de Excel",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Sistema de Carga de Archivos Excel")
st.markdown("---")

# Crear 2 filas de 2 columnas cada una
col1, col2 = st.columns(2)

# ==================== BOTÓN 1: CAPACIDAD DE PLANTA ====================
with col1:
    st.subheader("🏭 Capacidad de planta")
    file1 = st.file_uploader(
        "Carga tu archivo Excel",
        type=["xlsx", "xls"],
        key="file1"
    )
    
    if file1 is not None:
        try:
            df1 = pd.read_excel(file1)
            st.success("✅ Archivo cargado correctamente")
            st.dataframe(df1, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")

# ==================== BOTÓN 2: MAESTRO DE MATERIALES ====================
with col2:
    st.subheader("📦 Maestro de materiales")
    file2 = st.file_uploader(
        "Carga tu archivo Excel",
        type=["xlsx", "xls"],
        key="file2"
    )
    
    if file2 is not None:
        try:
            df2 = pd.read_excel(file2)
            st.success("✅ Archivo cargado correctamente")
            st.dataframe(df2, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")

# Nueva fila
col3, col4 = st.columns(2)

# ==================== BOTÓN 3: MAESTRO DE CLIENTES ====================
with col3:
    st.subheader("👥 Maestro de clientes")
    file3 = st.file_uploader(
        "Carga tu archivo Excel",
        type=["xlsx", "xls"],
        key="file3"
    )
    
    if file3 is not None:
        try:
            df3 = pd.read_excel(file3)
            st.success("✅ Archivo cargado correctamente")
            st.dataframe(df3, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")

# ==================== BOTÓN 4: DEMANDA ====================
with col4:
    st.subheader("📈 Demanda")
    file4 = st.file_uploader(
        "Carga tu archivo Excel",
        type=["xlsx", "xls"],
        key="file4"
    )
    
    if file4 is not None:
        try:
            df4 = pd.read_excel(file4)
            st.success("✅ Archivo cargado correctamente")
            st.dataframe(df4, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")

# Pie de página
st.markdown("---")
st.markdown("✨ Sistema de Carga de Excel - Versión 1.0")
