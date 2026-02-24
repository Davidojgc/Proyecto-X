import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(page_title="Planificador de Producción", layout="wide")

# ==========================================
# 1. CARGA DE DATOS (Con caché para velocidad)
# ==========================================
@st.cache_data
def cargar_datos():
    try:
        df_mat = pd.read_excel('Maestro_Materiales.xlsx')
        df_cli = pd.read_excel('Maestro_Clientes.xlsx')
        df_dem = pd.read_excel('Demanda.xlsx')
        df_cap = pd.read_excel('Capacidad_Planta.xlsx')
        
        for d in [df_mat, df_cli, df_dem, df_cap]:
            d.columns = d.columns.str.strip()
            
        df_dem['Fecha_DT'] = pd.to_datetime(df_dem['Fecha de necesidad'])
        df_dem['Semana_Label'] = df_dem['Fecha_DT'].dt.strftime('%Y-W%U')
        
        # Unimos maestros una sola vez
        df_base = df_dem.merge(df_mat, on=['Material', 'Unidad'], how='left')
        
        # Crear valor de azar fijo por fila para estabilidad
        def generar_azar(r):
            if r.get('Exclusico DG') == 'X': return 0.0 # Siempre 0833
            if r.get('Exclusivo MCH') == 'X': return 1.0 # Siempre 0181
            rng = np.random.RandomState(r.name)
            return rng.rand()
        
        df_base['Valor_Azar_Fijo'] = df_base.apply(generar_azar, axis=1)
        
        return df_base, df_mat, df_cap
    except Exception as e:
        st.error(f"Error cargando archivos: {e}")
        return None, None, None

df_base, df_mat, df_cap = cargar_datos()

if df_base is not None:
    CENTRO_ES = '0833'
    CENTRO_CH = '0181'
    semanas = sorted(df_base['Semana_Label'].unique())

    st.title("🚀 Optimización de Carga por Centro")
    
    # ==========================================
    # 2. BARRA LATERAL (SLIDERS)
    # ==========================================
    st.sidebar.header("Configuración por Semana")
    st.sidebar.write(f"Ajusta el % para el Centro {CENTRO_ES}")
    
    ajustes = {}
    for sem in semanas:
        ajustes[sem] = st.sidebar.slider(f"Semana {sem}", 0, 100, 50, key=sem)

    # ==========================================
    # 3. LÓGICA DE PROCESAMIENTO
    # ==========================================
    def procesar_produccion(df_input, dict_ajustes):
        df = df_input.copy()

        def decidir(r):
            # Si el azar fijo es 0 o 1 por exclusividad, se respeta
            if r['Valor_Azar_Fijo'] == 0.0 and r.get('Exclusico DG') == 'X': return CENTRO_ES
            if r['Valor_Azar_Fijo'] == 1.0 and r.get('Exclusivo MCH') == 'X': return CENTRO_CH
            
            umbral = dict_ajustes[r['Semana_Label']] / 100
            return CENTRO_ES if r['Valor_Azar_Fijo'] < umbral else CENTRO_CH

        df['Centro_Final'] = df.apply(decidir, axis=1)

        # Agrupación y Lotes
        df_agrup = df.groupby(['Material', 'Unidad', 'Centro_Final', 'Fecha de necesidad', 'Semana_Label']).agg({
            'Cantidad': 'sum',
            'Tamaño lote mínimo': 'first',
            'Tamaño lote máximo': 'first',
            'Tiempo fabricación unidad DG': 'first',
            'Tiempo fabricación unidad MCH': 'first'
        }).reset_index()

        resultado = []
        for i, fila in df_agrup.iterrows():
            cant_total = max(fila['Cantidad'], fila['Tamaño lote mínimo'])
            num_ordenes = math.ceil(cant_total / fila['Tamaño lote máximo'])
            for _ in range(num_ordenes):
                resultado.append({
                    'Material': fila['Material'],
                    'Centro': fila['Centro_Final'],
                    'Cantidad a fabricar': round(cant_total / num_ordenes, 2),
                    'Semana': fila['Semana_Label']
                })
        
        df_final = pd.DataFrame(resultado)
        
        # Calcular Horas
        df_h = df_final.merge(df_mat[['Material', 'Tiempo fabricación unidad DG', 'Tiempo fabricación unidad MCH']], on='Material', how='left')
        df_h['Horas'] = df_h.apply(lambda r: r['Cantidad a fabricar'] * (r['Tiempo fabricación unidad DG'] if r['Centro'] == CENTRO_ES else r['Tiempo fabricación unidad MCH']), axis=1)
        
        return df_final, df_h

    # Ejecutar proceso
    df_propuesta, df_horas = procesar_produccion(df_base, ajustes)

    # ==========================================
    # 4. VISUALIZACIÓN
    # ==========================================
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Distribución de Carga (Horas)")
        carga_graf = df_horas.groupby(['Semana', 'Centro'])['Horas'].sum().unstack().fillna(0)
        # Asegurar columnas
        for c in [CENTRO_ES, CENTRO_CH]:
            if c not in carga_graf.columns: carga_graf[c] = 0
            
        st.bar_chart(carga_graf[[CENTRO_ES, CENTRO_CH]], color=["#2E86C1", "#D35400"])

    with col2:
        st.subheader("Resumen Totales")
        totales = df_horas.groupby('Centro')['Horas'].sum()
        st.dataframe(totales)
        
        # Botón de descarga
        csv = df_propuesta.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar Propuesta (CSV)",
            data=csv,
            file_name='Propuesta_Fabricacion.csv',
            mime='text/csv',
        )

    st.subheader("Vista Previa de la Propuesta")
    st.dataframe(df_propuesta.head(50), use_container_width=True)
