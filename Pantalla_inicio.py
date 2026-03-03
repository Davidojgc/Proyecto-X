import streamlit as st
# Importamos tu archivo de GitHub como un módulo
try:
    import V3 
except ImportError:
    V3 = None

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Proyecto-X - Grifols", layout="wide")

st.markdown("""
    <style>
        [data-testid="stSidebar"] { background-color: #004d85; }
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
        div.stButton > button:hover { background-color: rgba(255, 255, 255, 0.1); }
        .mosh-logo { color: white; font-size: 32px; font-weight: bold; padding: 20px 0; text-align: center; }
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

if not st.session_state.autenticado:
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #004d85;'>💧 Proyecto-X</h1>", unsafe_allow_html=True)
        with st.form("login_form"):
            user_val = st.text_input("Usuario")
            pass_val = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Acceder al Programa", use_container_width=True):
                if user_val:
                    st.session_state.autenticado = True
                    st.session_state.usuario = user_val
                    st.rerun()
    st.stop()

# ==========================================
# 3. INTERFAZ PRINCIPAL
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">Proyecto-X</div>', unsafe_allow_html=True)
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta'

    if st.button("⚙️ Nueva propuesta"):
        st.session_state.current_page = 'Nueva propuesta'
    if st.button("📜 Historial de propuestas"):
        st.session_state.current_page = 'Historial de propuestas'
    if st.button("📅 Calendarios"):
        st.session_state.current_page = 'Calendarios'
    
    st.write("---")
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# --- CABECERA ---
head_col1, head_col2 = st.columns([10, 2])
with head_col1: st.write("≡")
with head_col2: st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# 4. LLAMADA A TU LIBRERÍA V3.py
# ==========================================
if st.session_state.current_page == 'Nueva propuesta':
    st.write(f"## {st.session_state.current_page}")
    st.write("### Ejecutando motor V3...")
    
    if V3 is not None:
        # Aquí llamas a la función que contiene tu código en V3.py
        # Ejemplo: V3.main() o V3.ejecutar_logica()
        try:
            V3.main() # <-- CAMBIA ESTO por el nombre de la función en tu V3.py
        except AttributeError:
            st.error("Error: No se encontró la función 'main()' en V3.py")
        except Exception as e:
            st.error(f"Error al ejecutar V3.py: {e}")
    else:
        st.error("No se pudo cargar el archivo V3.py. Asegúrate de que esté en el mismo repositorio.")

elif st.session_state.current_page == 'Historial de propuestas':
    st.write(f"## {st.session_state.current_page}")
    st.info("Consulta de propuestas anteriores.")

elif st.session_state.current_page == 'Calendarios':
    st.write(f"## {st.session_state.current_page}")
    st.info("Vista de planificación y calendarios de planta.")
