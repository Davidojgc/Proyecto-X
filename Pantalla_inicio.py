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
        
        /* ESTILO BOTONES SIDEBAR (LIMPIOS) */
        div.stButton > button {
            background-color: transparent;
            color: white;
            border: none;
            border-radius: 0px;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            font-size: 16px;
        }

        div.stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.1); 
            color: white;
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
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LÓGICA DE AUTENTICACIÓN (REDEFINIDA)
# ==========================================

# Inicializamos variables de estado si no existen
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

# Función para procesar el login
def login():
    if st.session_state.user_input:
        st.session_state.autenticado = True
        st.session_state.usuario = st.session_state.user_input
    else:
        st.error("Por favor, introduce un usuario.")

# PANTALLA DE LOGIN
if not st.session_state.autenticado:
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #004d85;'>💧 MOSH</h1>", unsafe_allow_html=True)
        st.write("### Iniciar Sesión")
        
        # Usamos 'key' para vincular el input directamente al session_state
        st.text_input("Usuario", key="user_input")
        st.text_input("Contraseña", type="password")
        
        # El botón llama a la función login
        st.button("Entrar", on_click=login)
    
    # Detenemos la ejecución para que no cargue el resto si no está logueado
    st.stop()

# ==========================================
# 3. INTERFAZ PRINCIPAL (Solo accesible si autenticado = True)
# ==========================================

with st.sidebar:
    st.markdown('<div class="mosh-logo">MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    # Botones principales
    if st.button("⚙️ Nueva propuesta de fabricación"):
        st.session_state.current_page = 'Nueva propuesta de fabricación'

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
st.write("### Mosh")
st.write("---")
st.success(f"Sesión iniciada correctamente como: {st.session_state.usuario}")
