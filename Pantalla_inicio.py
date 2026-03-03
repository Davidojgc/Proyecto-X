import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS (BOTONES ROJOS)
# ==========================================
st.set_page_config(page_title="MOSH - Grifols", layout="wide")

st.markdown("""
    <style>
        /* Fondo azul para el sidebar */
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        
        /* ESTILO DE LOS BOTONES: Color Rojo */
        div.stButton > button {
            background-color: #FF4B4B; /* Rojo vibrante */
            color: white;
            border-radius: 5px;
            border: none;
            height: 3em;
            width: 100%;
            transition: all 0.3s ease;
            font-weight: bold;
        }

        /* Efecto al pasar el ratón (hover) */
        div.stButton > button:hover {
            background-color: #D32F2F; /* Rojo más oscuro al pasar el mouse */
            color: white;
            border: 1px solid white;
        }

        /* Logo MOSH */
        .mosh-logo {
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR CON BOTONES ROJOS
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">💧 MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Tablas maestras'

    # Función para navegar
    def set_page(name):
        st.session_state.current_page = name

    # Botones del menú
    st.button("🗺️ Tablas maestras 〉", on_click=set_page, args=('Tablas maestras',))
    st.button("📋 Set Up Planning 〉", on_click=set_page, args=('Set Up Planning',))
    st.button("📦 Lanzamientos", on_click=set_page, args=('Lanzamientos',))
    st.button("🏭 Órdenes de fabricación 〉", on_click=set_page, args=('Órdenes de fabricación',))
    st.button("🔍 Consulta / Trazabilidad", on_click=set_page, args=('Consulta / Trazabilidad',))
    st.button("⚙️ Administración 〉", on_click=set_page, args=('Administración',))
    
    st.write("---")
    st.markdown(f"<p style='color:white;'>👤 David</p>", unsafe_allow_html=True)
    st.button("🚫 Cerrar Sesión")

# ==========================================
# 3. CONTENIDO PRINCIPAL
# ==========================================
head_col1, head_col2 = st.columns([10, 2])
with head_col1:
    st.write("≡")
with head_col2:
    st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)

st.write("---")
st.write(f"## {st.session_state.current_page}")
st.write("### Mosh")
st.write("---")

st.info(f"Sección activa: {st.session_state.current_page}")
