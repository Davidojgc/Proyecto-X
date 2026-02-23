import streamlit as st
import time

# Title of the web application
st.title("Ejemplo de Aplicación Streamlit")

# Button for executing a task
if st.button("Ejecutar"):
    st.write("Ejecutando...")
    
    # Progress bar
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)  # Simulating a long-running task
        progress_bar.progress(percent_complete + 1)
        
    st.write("Ejecución completada.")

    # Log execution output
    st.write("Registro de Ejecución:")
    st.write("Tarea completada exitosamente.")  # This would normally log more details.
