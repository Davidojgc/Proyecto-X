import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Optimización Sourcing 0833/0184", page_icon="🏭", layout="wide")

# --- LÓGICA DE CÁLCULO ---
@st.cache_data
def procesar_logica_optimizada(df_dem, df_mat, df_cli, coste_km_user):
    # Definición de centros actualizada
    CENTRO_ES = '0833'
    CENTRO_CH = '0184' # Cambiado de 0181 a 0184

    # 1. Preparación de datos
    df_dem['Fecha_DT'] = pd.to_datetime(df_dem['Fecha de necesidad'])
    df_dem['Semana_Label'] = df_dem['Fecha_DT'].dt.strftime('%Y-W%U')

    # 2. Unión de datos (Merge con maestros)
    df = df_dem.merge(df_mat, on=['Material', 'Unidad'], how='left')
    df = df.merge(df_cli, on='Cliente', how='left')

    def decidir_centro(r):
        # A. Prioridad a exclusividades
        if str(r.get('Exclusico DG')).strip().upper() == 'X': return CENTRO_ES, 0
        if str(r.get('Exclusivo MCH')).strip().upper() == 'X': return CENTRO_CH, 0

        # B. Obtención de variables dinámicas del Excel de Clientes y Materiales
        dist_es = r.get('Distancia a 0833', 0)
        dist_ch = r.get('Distancia a 0184', 0) # Columna actualizada
        
        c_fab_es = r.get('Coste fabricacion unidad DG', 0)
        c_fab_ch = r.get('Coste fabricacion unidad MCH', 0)
        cant = r.get('Cantidad', 0)

        # C. Cálculo de Coste Total: (Distancia * Precio/Km) + (Cantidad * Coste Fab)
        total_es = (dist_es * coste_km_user) + (cant * c_fab_es)
        total_ch = (dist_ch * coste_km_user) + (cant * c_fab_ch)
        
        # Selección del más óptimo
        centro_final = CENTRO_ES if total_es < total_ch else CENTRO_CH
        ahorro = abs(total_es - total_ch)
        
        return centro_final, ahorro

    # Aplicar lógica
    res_apply = df.apply(decidir_centro, axis=1)
    df['Centro_Final'] = [x[0] for x in res_apply]
    df['Ahorro_Estimado'] = [x[1] for x in res_apply]

    # 3. Agrupación y Generación de Lotes
    resultado_lotes = []
    df_agrupado = df.groupby(['Material', 'Unidad', 'Centro_Final', 'Fecha de necesidad', 'Semana_Label']).agg({
        'Cantidad': 'sum',
        'Tamaño lote mínimo': 'first',
        'Tamaño lote máximo': 'first',
        'Tiempo fabricación unidad DG': 'first',
        'Tiempo fabricación unidad MCH': 'first',
        'Ahorro_Estimado': 'sum'
    }).reset_index()

    for _, fila in df_agrupado.iterrows():
        cant_total = max(fila['Cantidad'], fila['Tamaño lote mínimo'])
        num_ordenes = math.ceil(cant_total / fila['Tamaño lote máximo'])
        cant_por_orden = round(cant_total / num_ordenes, 2)
        ahorro_por_orden = round(fila['Ahorro_Estimado'] / num_ordenes, 2)

        for i in range(num_ordenes):
            # Selección de tiempo de fabricación según centro final
            t_fab = fila['Tiempo fabricación unidad DG'] if fila['Centro_Final'] == CENTRO_ES else fila['Tiempo fabricación unidad MCH']
            
            resultado_lotes.append({
                'Material': fila['Material'],
                'Centro': fila['Centro_Final'],
                'Cantidad Propuesta': cant_por_orden,
                'Unidad': fila['Unidad'],
                'Semana': fila['Semana_Label'],
                'Fecha Carga': pd.to_datetime(fila['Fecha de necesidad']).strftime('%d/%m/%Y'),
                'Horas Totales': round(cant_por_orden * t_fab, 2),
                'Ahorro Optimización (€)': ahorro_por_orden
            })

    return pd.DataFrame(resultado_lotes)

# --- INTERFAZ DE USUARIO ---
st.title("📊 Optimizador de Sourcing: Centros 0833 y 0184")

with st.sidebar:
    st.header("Configuración")
    precio_km = st.number_input("Coste transporte (€/km)", value=0.15, format="%.2f")
    st.divider()
    st.caption("Nota: El sistema comparará el coste de envío + fabricación para elegir entre España (0833) y Suiza (0184).")

tab1, tab2 = st.tabs(["📥 Gestión de Archivos", "🚀 Ejecutar Propuesta"])

with tab1:
    st.subheader("Subida de Maestros")
    col1, col2 = st.columns(2)
    with col1:
        up_dem = st.file_uploader("1. Archivo de Demanda", type=["xlsx"])
        up_mat = st.file_uploader("2. Maestro Materiales (Costes DG/MCH)", type=["xlsx"])
    with col2:
        up_cli = st.file_uploader("3. Maestro Clientes (Distancias 0833/0184)", type=["xlsx"])

if up_dem and up_mat and up_cli:
    # Carga de datos
    df_dem = pd.read_excel(up_dem)
    df_mat = pd.read_excel(up_mat)
    df_cli = pd.read_excel(up_cli)

    with tab2:
        if st.button("GENERAR PROPUESTA ÓPTIMA"):
            with st.spinner("Calculando rutas y costes..."):
                df_res = procesar_logica_optimizada(df_dem, df_mat, df_cli, precio_km)
                
                # Visualización de métricas
                m1, m2, m3 = st.columns(3)
                m1.metric("Ahorro Total Estimado", f"{df_res['Ahorro Optimización (€)'].sum():,.2f} €")
                m2.metric("Carga de Trabajo (Horas)", f"{df_res['Horas Totales'].sum():,.1f} h")
                
                distribucion = df_res['Centro'].value_counts(normalize=True) * 100
                m3.metric("% Carga 0833", f"{distribucion.get('0833', 0):.1f}%")

                # Tabla de resultados
                st.subheader("📋 Detalle de la Propuesta")
                st.dataframe(df_res, use_container_width=True)

                # Exportación
                csv = df_res.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Descargar Propuesta en CSV", data=csv, file_name="propuesta_sourcing.csv")
