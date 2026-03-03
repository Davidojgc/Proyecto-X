import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Proyecto X - Login", layout="wide")

st.markdown("""
    <style>
        /* Estilos generales para botones rojos */
        div.stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 5px;
            font-weight: bold;
            width: 100%;
        }
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        .mosh-logo {
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LÓGICA DE CONTROL DE SESIÓN
# ==========================================
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

# --- PANTALLA DE LOGIN ---
if not st.session_state.autenticado:
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #004d85;'>💧 Proyecto-X</h1>", unsafe_allow_html=True)
        st.subheader("Inicio de Sesión")
        
        usuario_input = st.text_input("Introduce tu nombre de usuario:")
        password_input = st.text_input("Contraseña:", type="password") # Simulado
        
        if st.button("Entrar"):
            if usuario_input: # Si el nombre no está vacío
                st.session_state.autenticado = True
                st.session_state.usuario = usuario_input
                st.rerun()
            else:
                st.error("Por favor, introduce un nombre de usuario.")
    st.stop() # Detiene la ejecución aquí si no está autenticado

# ==========================================
# 3. INTERFAZ PRINCIPAL (Solo si está logueado)
# ==========================================

# Sidebar
with st.sidebar:
    st.markdown('<div class="mosh-logo">💧 Proyecto-X</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Tablas maestras'

    def set_page(name):
        st.session_state.current_page = name

    st.button("🗺️ Tablas maestras 〉", on_click=set_page, args=('Tablas maestras',))
    st.button("📋 Set Up Planning 〉", on_click=set_page, args=('Set Up Planning',))
    st.button("📦 Lanzamientos", on_click=set_page, args=('Lanzamientos',))
    st.button("🏭 Órdenes de fabricación 〉", on_click=set_page, args=('Órdenes de fabricación',))
    st.button("🔍 Consulta / Trazabilidad", on_click=set_page, args=('Consulta / Trazabilidad',))
    st.button("⚙️ Administración 〉", on_click=set_page, args=('Administración',))
    
    st.write("---")
    # Mostramos el usuario que entró en la primera pantalla
    st.markdown(f"<p style='color:white;'>👤 Usuario: <b>{st.session_state.usuario}</b></p>", unsafe_allow_html=True)
    
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.session_state.usuario = ""
        st.rerun()

# Cabecera
head_col1, head_col2 = st.columns([10, 2])
with head_col1:
    st.write("≡")
with head_col2:
    st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)

st.write("---")
st.write(f"## {st.session_state.current_page}")
st.write(f"Bienvenido al sistema, **{st.session_state.usuario}**.")
