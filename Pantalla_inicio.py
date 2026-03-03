import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="MOSH - Grifols", layout="wide")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        
        /* Estilo para los botones principales y subbotones */
        div.stButton > button {
            background-color: #004d85;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 0px;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            font-size: 16px;
        }

        div.stButton > button:hover {
            background-color: #003366;
            color: white;
            border: 1px solid white;
        }

        /* Estilo específico para los subbotones (indentación) */
        .sub-button div.stButton > button {
            padding-left: 40px !important;
            font-size: 14px;
            background-color: #003d6a; /* Un tono ligeramente distinto para diferenciarlo */
        }

        .mosh-logo {
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
        }

        /* Ajuste para el Expander (el desplegable) */
        .stExpander {
            border: none !important;
            background-color: transparent !important;
        }
        .stExpander [data-testid="stExpanderDetails"] {
            padding-top: 0px;
            padding-bottom: 0px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LÓGICA DE SESIÓN (LOGIN)
# ==========================================
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.autenticado:
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #004d85;'>💧 MOSH</h1>", unsafe_allow_html=True)
        usuario_input = st.text_input("Usuario")
        if st.button("Entrar"):
            if usuario_input:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario_input
                st.rerun()
    st.stop()

# ==========================================
# 3. SIDEBAR CON SUBMENÚ DESPLEGABLE
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    def set_page(name):
        st.session_state.current_page = name

    # Botón 1: Directo
    st.button("⚙️ Nueva propuesta de fabricación", on_click=set_page, args=('Nueva propuesta de fabricación',))

    # Botón 2: DATOS MAESTROS (Usamos un Expander para el despliegue)
    with st.expander("📊 Datos maestros", expanded=False):
        st.markdown('<div class="sub-button">', unsafe_allow_html=True)
        if st.button("• Materiales"):
            set_page("Datos maestros - Materiales")
        if st.button("• Clientes"):
            set_page("Datos maestros - Clientes")
        if st.button("• Plantas y capacidad"):
            set_page("Datos maestros - Plantas y capacidad")
        st.markdown('</div>', unsafe_allow_html=True)

    # Botón 3: Directo
    st.button("📜 Historial de propuestas", on_click=set_page, args=('Historial de propuestas',))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p style='color:white; margin-left:20px;'>👤 {st.session_state.usuario}</p>", unsafe_allow_html=True)
    
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# ==========================================
# 4. CUERPO PRINCIPAL
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

# Ejemplo de contenido dinámico para las nuevas secciones
if "Materiales" in st.session_state.current_page:
    st.info("Listado maestro de materiales y SKUs.")
elif "Clientes" in st.session_state.current_page:
    st.info("Base de datos de clientes y centros de distribución.")
elif "Plantas" in st.session_state.current_page:
    st.info("Capacidad instalada por planta y líneas de producción.")
