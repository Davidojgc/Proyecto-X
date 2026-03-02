import streamlit as st
import V3  # Importamos tu librería directamente

# 1. Configuración de la página
st.set_page_config(page_title="Panel de Control", layout="centered")

# 2. Inicialización del estado de la sesión (Navegación)
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'inicio'

# --- FUNCIÓN PARA VOLVER AL INICIO ---
def volver_inicio():
    st.session_state.pagina_actual = 'inicio'

# --- LÓGICA DE NAVEGACIÓN ---

# CASO A: PANTALLA DE INICIO
if st.session_state.pagina_actual == 'inicio':
    st.title("Bienvenido al Sistema 👋")
    st.subheader("Selecciona una opción")
    st.divider()

    # Creamos la cuadrícula de 2x2
    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Crear nuevo escenario", use_container_width=True):
            st.session_state.pagina_actual = 'crear_escenario'
            st.rerun()

        if st.button("📊 Datos Maestros", use_container_width=True):
            st.info("Has seleccionado: Datos Maestros")

    with col2:
        if st.button("📜 Historial", use_container_width=True):
            st.info("Has seleccionado: Historial")

        if st.button("📅 Calendario", use_container_width=True):
            st.info("Has seleccionado: Calendario")

# CASO B: PANTALLA DE NUEVO ESCENARIO (Llamando a V3.py)
elif st.session_state.pagina_actual == 'crear_escenario':
    if st.button("⬅️ Volver al menú"):
        volver_inicio()
        st.rerun()
    
    st.title("🛠️ Nuevo Escenario")
    st.write("Ejecutando lógica desde V3.py...")
    
    # LLAMADA A TU LIBRERÍA
    # Aquí asumo que tienes una función llamada 'ejecutar' o similar en V3.py
    try:
        # Ejemplo: llamamos a una función de V3 que dibuje algo o haga cálculos
        V3.ejecutar_interfaz() 
    except AttributeError:
        st.warning("La librería V3.py se cargó, pero no encontré la función 'ejecutar_interfaz()'.")
        st.info("Asegúrate de tener: def ejecutar_interfaz(): dentro de V3.py")
