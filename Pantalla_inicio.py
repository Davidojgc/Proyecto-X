import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS (AZUL INTEGRADO)
# ==========================================
st.set_page_config(page_title="MOSH - Grifols", layout="wide")

st.markdown("""
    <style>
        /* Fondo azul para el sidebar */
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        
        /* ESTILO DE LOS BOTONES: Fondo azul igual que el sidebar */
        div.stButton > button {
            background-color: #004d85; /* Mismo azul que el fondo */
            color: white;              /* Texto en blanco */
            border: 1px solid rgba(255, 255, 255, 0.2); /* Borde sutil casi invisible */
            border-radius: 0px;        /* Bordes rectos para un look más corporativo */
            width: 100%;
            text-align: left;          /* Alineado a la izquierda como en la foto */
            padding: 10px 20px;
            font-size: 16px;
        }

        /* Efecto al pasar el ratón (Hover) */
        div.stButton > button:hover {
            background-color: #003366; /* Un azul un poco más oscuro al pasar el mouse */
            color: #ffffff;
            border: 1px solid white;
        }

        /* Ajuste para el texto del usuario y logos */
        .mosh-logo {
            color: white;
            font-size: 36px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LÓGICA DE LOGIN
# ==========================================
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.autenticado:
    # Pantalla de Login centrada
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<h1 style='text-align: center; color: #004d85;'>💧 MOSH</h1>", unsafe_allow_html=True)
        usuario_input = st.text_input("Usuario")
        if st.button("Iniciar Sesión"):
            if usuario_input:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario_input
                st.rerun()
    st.stop()

# ==========================================
# 3. INTERFAZ PRINCIPAL (SIDEBAR AZUL)
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">MOSH</div>', unsafe_allow_html=True)
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Tablas maestras'

    def set_page(name):
        st.session_state.current_page = name

    # Botones que parecen parte del fondo
    st.button("🗺️ Tablas maestras 〉", on_click=set_page, args=('Tablas maestras',))
    st.button("📋 Set Up Planning 〉", on_click=set_page, args=('Set Up Planning',))
    st.button("📦 Lanzamientos", on_click=set_page, args=('Lanzamientos',))
    st.button("🏭 Órdenes de fabricación 〉", on_click=set_page, args=('Órdenes de fabricación',))
    st.button("🔍 Consulta / Trazabilidad", on_click=set_page, args=('Consulta / Trazabilidad',))
    st.button("⚙️ Administración 〉", on_click=set_page, args=('Administración',))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p style='color:white; margin-left:20px;'>👤 {st.session_state.usuario}</p>", unsafe_allow_html=True)
    
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# ==========================================
# 4. ÁREA DE TRABAJO
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
st.info(f"Panel de control activo para: {st.session_state.usuario}")
