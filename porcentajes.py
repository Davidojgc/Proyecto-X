import streamlit as st
import pandas as pd
import numpy as np
import os
import math
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Sistema de Cálculo de Fabricación",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS CSS PERSONALIZADOS
# ==========================================
st.markdown("""
<style>
    .main { padding-top: 2rem; }
    h1 { color: #1f77b4; text-align: center; font-size: 2.5rem; margin-bottom: 1rem; }
    .section-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 1.5rem;
    }
    .footer {
        text-align: center; color: #7f8c8d; font-size: 0.9rem; margin-top: 2rem;
        padding-top: 1rem; border-top: 1px solid #ecf0f1;
    }
</style>
""", unsafe_allow_html=True)

# Crear carpeta para guardar archivos
UPLOAD_DIR = "archivos_cargados"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# ==========================================
# FUNCIONES DE LÓGICA Y CÁLCULO
# ==========================================

def procesar_logica_estable(df_dem, df_mat, df_cli, df_cap, ajustes_semanales):
    # 0. Identificación Dinámica de Centros desde Capacidad Planta
    # Obtenemos la lista de centros (ej: ['0833', '0184'])
    centros = [str(c).strip() for c in df_cap['Centro'].unique()]
    
    # Identificamos cuál es España y cuál Suiza para no cruzarlos
    # Buscamos '0833' para España y cualquier otro (como '0184') para Suiza
    centro_es = next((c for c in centros if "0833" in c), centros[0])
    centro_ch = next((c for c in centros if c != centro_es), centros[1] if len(centros) > 1 else centros[0])

    # 1. Preparación de Fechas
    df_dem['Fecha_DT'] = pd.to_datetime(df_dem['Fecha de necesidad'])
    df_dem['Semana_Label'] = df_dem['Fecha_DT'].dt.strftime('%Y-W%U')

    # 2. Unión con Maestros
    df = df_dem.merge(df_mat, on=['Material', 'Unidad'], how='left')
    df = df.merge(df_cli, on='Cliente', how='left')

    # 3. Decisión de Centro (Optimización de Coste)
    def decidir_centro(r):
        # A. Prioridad a exclusividades
        if str(r.get('Exclusico DG')).strip().upper() == 'X': return centro_es
        if str(r.get('Exclusivo MCH')).strip().upper() == 'X': return centro_ch

        # B. Parámetros de Coste desde Excel Clientes y Materiales
        dist_es = r.get(f'Distancia a {centro_es}', 0)
        dist_ch = r.get(f'Distancia a {centro_ch}', 0)
        coste_km = r.get('precio KM', 0.15) # Extraído del Maestro Clientes
        
        c_fab_es = r.get('Coste fabricacion unidad DG', 0)
        c_fab_ch = r.get('Coste fabricacion unidad MCH', 0)
        cant = r.get('Cantidad', 0)

        # C. Cálculo de Coste Total
        coste_total_es = (dist_es * coste_km) + (cant * c_fab_es)
        coste_total_ch = (dist_ch * coste_km) + (cant * c_fab_ch)

        # D. Decisión estricta por coste mínimo
        if coste_total_es < coste_total_ch:
            return centro_es
        elif coste_total_ch < coste_total_es:
            return centro_ch
        else:
            # Empate: Azar según slider
            rng = np.random.RandomState(r.name)
            umbral = ajustes_semanales.get(r['Semana_Label'], 50) / 100
            return centro_es if rng.rand() < umbral else centro_ch

    df['Centro_Final'] = df.apply(decidir_centro, axis=1)

    # 4. Agrupación y Lotes
    df_agrupado = df.groupby(['Material', 'Unidad', 'Centro_Final', 'Fecha de necesidad', 'Semana_Label']).agg({
        'Cantidad': 'sum',
        'Tamaño lote mínimo': 'first',
        'Tamaño lote máximo': 'first',
        'Tiempo fabricación unidad DG': 'first',
        'Tiempo fabricación unidad MCH': 'first'
    }).reset_index()

    resultado_lotes = []
    cont = 1
    for _, fila in df_agrupado.iterrows():
        cant_total = max(fila['Cantidad'], fila['Tamaño lote mínimo'])
        num_ordenes = math.ceil(cant_total / fila['Tamaño lote máximo'])
        cant_por_orden = round(cant_total / num_ordenes, 2)

        for _ in range(num_ordenes):
            # Tiempo de fabricación según el centro que ganó la optimización
            t_fab = fila['Tiempo fabricación unidad DG'] if fila['Centro_Final'] == centro_es else fila['Tiempo fabricación unidad MCH']
            
            resultado_lotes.append({
                'Nº de propuesta': cont,
                'Material': fila['Material'],
                'Centro': fila['Centro_Final'],
                'Clase de orden': 'NORM',
                'Cantidad a fabricar': cant_por_orden,
                'Unidad': fila['Unidad'],
                'Fecha de fabricación': pd.to_datetime(fila['Fecha de necesidad']).strftime('%Y%m%d'),
                'Semana': fila['Semana_Label'],
                'Horas': round(cant_por_orden * t_fab, 2)
            })
            cont += 1

    return pd.DataFrame(resultado_lotes)

# --- RESTO DE LA INTERFAZ STREAMLIT ---
st.markdown("<h1>📊 Sistema de Cálculo de Fabricación</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📥 1. Carga de Archivos", "⚙️ 2. Ajuste y Ejecución"])

with tab1:
    st.subheader("📁 Carga los 4 archivos maestros")
    col1, col2 = st.columns(2)
    with col1:
        f_cap = st.file_uploader("Capacidad", type=["xlsx"], key="u1")
        f_mat = st.file_uploader("Materiales", type=["xlsx"], key="u2")
    with col2:
        f_cli = st.file_uploader("Clientes", type=["xlsx"], key="u3")
        f_dem = st.file_uploader("Demanda", type=["xlsx"], key="u4")

data_ready = False
if f_cap and f_mat and f_cli and f_dem:
    try:
        df_cap = pd.read_excel(f_cap)
        df_mat = pd.read_excel(f_mat)
        df_cli = pd.read_excel(f_cli)
        df_dem = pd.read_excel(f_dem)
        for d in [df_cap, df_mat, df_cli, df_dem]: d.columns = d.columns.str.strip()
        
        df_dem['Semana_Label'] = pd.to_datetime(df_dem['Fecha de necesidad']).dt.strftime('%Y-W%U')
        lista_semanas = sorted(df_dem['Semana_Label'].unique())
        data_ready = True
    except Exception as e:
        st.error(f"Error al leer archivos: {e}")

with tab2:
    if not data_ready:
        st.warning("⚠️ Carga los archivos en la pestaña 1.")
    else:
        # Detectamos nombres para los sliders
        centros_l = [str(c).strip() for c in df_cap['Centro'].unique()]
        c_es_n = next((c for c in centros_l if "0833" in c), centros_l[0])
        
        ajustes = {}
        cols = st.columns(4)
        for i, sem in enumerate(lista_semanas):
            with cols[i % 4]:
                ajustes[sem] = st.slider(f"Sem {sem} (% {c_es_n})", 0, 100, 50)

        if st.button("🚀 EJECUTAR CÁLCULO", use_container_width=True):
            df_res = procesar_logica_estable(df_dem, df_mat, df_cli, df_cap, ajustes)
            st.success("✅ Propuesta generada correctamente.")
            
            # Mostrar tabla
            st.dataframe(df_res, use_container_width=True)
            
            # Descarga
            output = os.path.join(UPLOAD_DIR, "Resultado.xlsx")
            df_res.to_excel(output, index=False)
            with open(output, "rb") as f:
                st.download_button("📥 Descargar Excel", f, file_name="Propuesta.xlsx")

st.markdown('<div class="footer"><p>✨ Sistema de Cálculo de Fabricación - V3.2</p></div>', unsafe_allow_html=True)
