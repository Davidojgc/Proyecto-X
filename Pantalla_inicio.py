import streamlit as st
import importlib.util
import sys

# ==========================================
# 1. CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Proyecto-X - Grifols", layout="wide")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #004d85;
        }
        /* Botones del menú lateral siempre blancos y sin recuadro */
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
        .mosh-logo {
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding: 20px 0;
            text-align: center;
        }
        /* Botón del login */
        .stForm div.stButton > button {
            background-color: #004d85 !important;
            text-align: center !important;
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
# 3. SIDEBAR (PERMANENTE)
# ==========================================
with st.sidebar:
    st.markdown('<div class="mosh-logo">Proyecto-X</div>', unsafe_allow_html=True)
    
    # Inicializamos la página por defecto
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Nueva propuesta'

    # Botones que cambian el estado pero NO recargan la página completa
    if st.button("⚙️ Nueva propuesta"):
        st.session_state.current_page = 'Nueva propuesta'
    
    if st.button("📜 Historial de propuestas"):
        st.session_state.current_page = 'Historial de propuestas'

    if st.button("📅 Calendarios"):
        st.session_state.current_page = 'Calendarios'
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p style='color:white; margin-left:20px;'>👤 {st.session_state.usuario}</p>", unsafe_allow_html=True)
    
    if st.button("🚫 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

# ==========================================
# 4. CUERPO PRINCIPAL (CONTENIDO DINÁMICO)
# ==========================================

# Cabecera de Grifols (Siempre visible)
head_col1, head_col2 = st.columns([10, 2])
with head_col1: st.write("≡")
with head_col2: st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)
st.write("---")

# Lógica de despliegue
if st.session_state.current_page == 'Nueva propuesta':
    # Intentamos importar y ejecutar el archivo V3.py
    try:
        import V3
        # Importante: Aquí llamamos a la función principal de tu V3.py
        # Si tu V3.py no tiene funciones y es código directo, se ejecutará al importar
        # pero es mejor llamar a una función específica:
        V3.main() 
    except Exception as e:
        st.error(f"Error al cargar la librería V3: {e}")
        st.info("Asegúrate de que V3.py esté en la raíz de tu repositorio y tenga una función llamada main()")

elif st.session_state.current_page == 'Historial de propuestas':
    st.header("Historial de propuestas")
    st.write("Aquí se mostrará el histórico de datos.")

elif st.session_state.current_page == 'Calendarios':
    st.header("Calendarios de Producción")
    st.write("Vista de planificación.")
