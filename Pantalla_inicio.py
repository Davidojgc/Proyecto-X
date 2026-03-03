import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# ==========================================
# Definimos el título que aparece en la pestaña del navegador
st.set_page_config(page_title="MOSH - Grifols", layout="wide")

# Usamos CSS para replicar los colores exactos de tu imagen.
# El azul de fondo y el color blanco del texto.
# También ocultamos el menú superior por defecto de Streamlit para una experiencia más limpia.
st.markdown("""
    <style>
        /* Fondo azul para el sidebar */
        [data-testid="stSidebar"] {
            background-color: #004d85;
            color: white;
        }
        
        /* Asegurar que el texto dentro del sidebar sea blanco por defecto */
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] .stButton button {
            color: white;
        }

        /* Estilo personalizado para el logo principal de MOSH */
        .mosh-logo {
            color: white;
            font-size: 36px;
            font-weight: bold;
            font-family: sans-serif;
            margin-bottom: 30px;
        }

        /* Estilo para simular los íconos (con emojis) */
        .icon {
            margin-right: 10px;
        }
        
        /* Ocultar elementos de Streamlit por defecto */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CREACIÓN DEL SIDEBAR (MENÚ IZQUIERDO)
# ==========================================
with st.sidebar:
    # --- Encabezado Principal (Logo MOSH) ---
    # Usamos HTML para aplicar el estilo de fuente grande y blanco
    st.markdown('<div class="mosh-logo">💧 MOSH</div>', unsafe_allow_html=True)
    
    # Creamos un estado de sesión para guardar cuál es la página actual.
    # Por defecto, empieza en 'Tablas maestras'.
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Tablas maestras'

    # --- Funciones para cambiar de página ---
    # Estas funciones se ejecutan cuando se pulsa un botón.
    def set_page(name):
        st.session_state.current_page = name

    # --- Elementos del Menú ---
    # Los creamos como botones para que sean interactivos.
    # Usamos emojis para simular los iconos de tu imagen.
    
    st.markdown("### ") # Espaciador
    
    # Menú 1: Tablas maestras
    if st.button("🗺️ Tablas maestras 〉", use_container_width=True, on_click=set_page, args=('Tablas maestras',)):
        pass

    # Menú 2: Set Up Planning
    if st.button("📋 Set Up Planning 〉", use_container_width=True, on_click=set_page, args=('Set Up Planning',)):
        pass

    # Menú 3: Lanzamientos
    if st.button("📦 Lanzamientos", use_container_width=True, on_click=set_page, args=('Lanzamientos',)):
        pass

    # Menú 4: Órdenes de fabricación
    if st.button("🏭 Órdenes de fabricación 〉", use_container_width=True, on_click=set_page, args=('Órdenes de fabricación',)):
        pass

    # Menú 5: Consulta / Trazabilidad
    if st.button("🔍 Consulta / Trazabilidad", use_container_width=True, on_click=set_page, args=('Consulta / Trazabilidad',)):
        pass

    # Menú 6: Administración
    if st.button("⚙️ Administración 〉", use_container_width=True, on_click=set_page, args=('Administración',)):
        pass
    
    # Usuario actual
    st.write("---")
    st.write(f"👤 David")
    st.write("---")

    # Botón de Cerrar Sesión (al final)
    st.button("🚫 Cerrar Sesión", use_container_width=True)

# ==========================================
# 3. CUERPO PRINCIPAL DE LA PÁGINA
# ==========================================

# --- Cabecera Superior ---
# Dos columnas: una para el menú hamburguesa (simulado) y otra para el logo de Grifols
head_col1, head_col2 = st.columns([10, 2])

with head_col1:
    st.write("≡") # Símbolo de menú hamburguesa

with head_col2:
    # Usamos HTML para que el logo de Grifols aparezca en azul oscuro y a la derecha
    st.markdown('<div style="color: #003366; font-size: 24px; font-weight: bold; text-align: right;">GRIFOLS</div>', unsafe_allow_html=True)

st.write("---") # Línea divisoria horizontal

# --- Contenido Dinámico ---
# Mostramos un título diferente según la página seleccionada en el menú.
# Debajo del título, mostramos el encabezado "Mosh" con una línea divisoria.

st.write(f"## {st.session_state.current_page}")
st.write("### Mosh")
st.write("---")

# Aquí añadirías el contenido específico de cada página. De momento, mostramos un texto de ejemplo.
st.write(f"Estás visualizando el contenido de la sección: **{st.session_state.current_page}**.")
st.write("Este es el área principal donde irán las tablas, gráficos y formularios.")
