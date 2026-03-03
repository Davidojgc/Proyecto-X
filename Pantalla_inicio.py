import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Proyecto-X - Grifols", layout="wide")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        
        /* ESTILO BOTONES SIDEBAR (LIMPIOS) */
        div.stButton > button {
            background-color: transparent;
            color: white !important;
            border: none;
            border-radius: 0px;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            font-size: 16px;
        }

        div.stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.1); 
            color: white !important;
        }

        /* FORZAR COLOR BLANCO EN EL TEXTO DE 'DATOS MAESTROS' (EXPANDER) */
        details[data-testid="stExpander"] summary p {
            color: white !important;
        }
        
        /* Color de la flecha del expander en blanco */
        details[data-testid="stExpander"] summary svg {
            fill: white !important;
        }

        .mosh-logo {
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
        }
        
        /* Estilo para sub-botones */
        .sub-button div.stButton > button {
            padding-left: 40px !important;
            font-size: 14px;
        }

        /* Estilo para el botón de la pantalla de login */
        .stForm div.stButton > button {
            background-color: #004d85 !important;
            color: white !important;
            text-align: center !important;
            border-radius: 5px !important;
            border: 1px solid white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LÓGICA DE AUTENTICACIÓN
# ==========================================

if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.autenticado:
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #004d85;'>💧 Proyecto-X</h1>", unsafe_allow_html=True)
        st.write("### Identificación")
        
        with st.form("login_form"):
            user_val = st.text_input("Usuario")
            pass_val = st.text_input("Contraseña", type="password")
            submit_button = st.form_submit_button("Acceder al Programa", use_container_width=True)
            
            if submit_button:
                if user_val:
                    st.session_state.autenticado = True
                    st.session_state.usuario = user_val
                    st.rerun()
                else:
                    st.error("Por favor, introduce tu nombre de usuario.")
    st.stop()

# ==========================================
# 3. INTERFAZ PRINCIPAL
# ==========================================

with st.sidebar:
    st.markdown('<div class="mosh-logo">Proyecto-X</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    # Botones principales
    if st.button("⚙️ Nueva propuesta de fabricación"):
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    # Expander con texto forzado a blanco vía CSS
    with st.expander("📊 Datos maestros", expanded=False):
        st.markdown('<div class="sub-button">', unsafe_allow_html=True)
        if st.button("• Materiales"):
            st.session_state.current_page = "Datos maestros - Materiales"
        if st.button("• Clientes"):
            st.session_state.current_page = "Datos maestros - Clientes"
        if st.button("• Plantas y capacidad"):
            st.session_state.current_page = "Datos maestros - Plantas y capacidad"
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("📜 Historial de propuestas"):
        st.session_state.current_page = 'Historial de propuestas'
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p style='color:white; margin-left:20px;'>👤 {st.session_state.usuario}</p>", unsafe_allow_html=True)
    
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CABECERA ---
head_col1, head_col2 = st.columns([10, 2])
with head_col1:
    st.write("≡")
with head_col2:
    st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)

st.write("---")
st.write(f"## {st.session_state.current_page}")
st.write("### Proyecto-X")
st.write("---")
