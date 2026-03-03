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
        
        /* ESTILO DE LOS BOTONES: Azul integrado */
        div.stButton > button {
            background-color: #004d85;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 0px;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            font-size: 16px;
            margin-bottom: -10px;
        }

        div.stButton > button:hover {
            background-color: #003366;
            color: #ffffff;
            border: 1px solid white;
        }

        .mosh-logo {
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
            font-family: sans-serif;
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
        st.write("### Identificación de Usuario")
        usuario_input = st.text_input("Nombre de usuario")
        if st.button("Entrar"):
            if usuario_input:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario_input
                st.rerun()
    st.stop()

# ==========================================
# 3. SIDEBAR (MENÚ SIMPLIFICADO)
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta de fabricación'

    def set_page(name):
        st.session_state.current_page = name

    # LOS 3 BOTONES SOLICITADOS
    st.button("⚙️ Nueva propuesta de fabricación", on_click=set_page, args=('Nueva propuesta de fabricación',))
    st.button("📊 Datos maestros", on_click=set_page, args=('Datos maestros',))
    st.button("📜 Historial de propuestas", on_click=set_page, args=('Historial de propuestas',))
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
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

# Contenido por sección
if st.session_state.current_page == 'Nueva propuesta de fabricación':
    st.write("Aquí puedes configurar los parámetros para una nueva orden de fabricación.")
elif st.session_state.current_page == 'Datos maestros':
    st.write("Gestión de bases de datos, materiales y centros de producción.")
elif st.session_state.current_page == 'Historial de propuestas':
    st.write("Listado de todas las propuestas generadas anteriormente.")
