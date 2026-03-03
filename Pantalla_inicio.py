import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS (BOTONES SIN RECUADRO)
# ==========================================
st.set_page_config(page_title="MOSH - Grifols", layout="wide")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        
        /* ESTILO BASE PARA LOS BOTONES DEL SIDEBAR */
        div.stButton > button {
            background-color: transparent; /* Sin fondo */
            color: white;
            border: none;                  /* QUITAMOS EL RECUADRO BLANCO */
            border-radius: 0px;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        /* Efecto Hover: Que se vea un sombreado azul al pasar el ratón */
        div.stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.1); 
            color: white;
            border: none;
        }

        /* Ajuste para el Expander de Datos Maestros */
        .stExpander {
            border: none !important;
            background-color: transparent !important;
        }
        
        /* Estilo para los sub-botones dentro de Datos Maestros */
        .sub-button div.stButton > button {
            padding-left: 40px !important;
            font-size: 14px;
            opacity: 0.8; /* Un poco más suaves */
        }

        .mosh-logo {
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
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
# 3. SIDEBAR (BOTONES LIMPIOS)
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    def set_page(name):
        st.session_state.current_page = name

    # Botón 1: Sin recuadro
    st.button("⚙️ Nueva propuesta de fabricación", on_click=set_page, args=('Nueva propuesta de fabricación',))

    # Botón 2: DATOS MAESTROS (Mantenemos el expander por funcionalidad)
    with st.expander("📊 Datos maestros", expanded=False):
        st.markdown('<div class="sub-button">', unsafe_allow_html=True)
        if st.button("• Materiales"):
            set_page("Datos maestros - Materiales")
        if st.button("• Clientes"):
            set_page("Datos maestros - Clientes")
        if st.button("• Plantas y capacidad"):
            set_page("Datos maestros - Plantas y capacidad")
        st.markdown('</div>', unsafe_allow_html=True)

    # Botón 3: Sin recuadro
    st.button("📜 Historial de propuestas", on_click=set_page, args=('Historial de propuestas',))
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p style='color:white; margin-left:20px; font-weight: bold;'>👤 {st.session_state.usuario}</p>", unsafe_allow_html=True)
    
    # El botón de cerrar sesión también lo he dejado limpio para que combine
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

st.info(f"Sección activa: {st.session_state.current_page}")
