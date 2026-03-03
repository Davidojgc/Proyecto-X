import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestor de Escenarios", layout="wide")

def main():
    st.title("🚀 Sistema de Gestión Operativa")
    st.markdown("---")

    # Sidebar para la navegación (opcional, pero recomendado)
    st.sidebar.header("Menú de Navegación")
    
    # Creamos columnas para los botones principales
    col1, col2, col3 = st.columns(3)

    # Inicializamos el estado de la aplicación si no existe
    if 'menu_actual' not in st.session_state:
        st.session_state.menu_actual = "Inicio"

    # Lógica de los botones
    with col1:
        if st.button("🆕 Crear Escenario", use_container_width=True):
            st.session_state.menu_actual = "crear"

    with col2:
        if st.button("📜 Historial", use_container_width=True):
            st.session_state.menu_actual = "historial"

    with col3:
        if st.button("📊 Datos Maestros", use_container_width=True):
            st.session_state.menu_actual = "datos"

    st.markdown("---")

    # Despliegue de contenido según el botón presionado
    if st.session_state.menu_actual == "crear":
        st.header("🛠️ Configuración de Nuevo Escenario")
        st.text_input("Nombre del Escenario")
        st.date_input("Fecha de inicio")
        st.button("Guardar Escenario")

    elif st.session_state.menu_actual == "historial":
        st.header("📜 Historial de Registros")
        st.info("Aquí aparecerán los escenarios guardados anteriormente.")
        # Ejemplo de tabla de datos
        st.table({"ID": [1, 2], "Nombre": ["Escenario A", "Escenario B"], "Estado": ["Finalizado", "Pendiente"]})

    elif st.session_state.menu_actual == "datos":
        st.header("📊 Gestión de Datos Maestros")
        st.write("Carga y edición de parámetros base del sistema.")
        st.file_uploader("Cargar archivo CSV/Excel", type=["csv", "xlsx"])

    else:
        st.write("Selecciona una opción arriba para comenzar.")

if __name__ == "__main__":
    main()
