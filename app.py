import streamlit as st

# Configuración de página ancha y diseño
st.set_page_config(layout="wide")

# --- MEMORIA DE LA WEB (Caja Fuerte) ---
# Si la lista de alumnos no existe en la memoria, la creamos vacía por primera vez
if "lista_alumnos" not in st.session_state:
    st.session_state["lista_alumnos"] = []

# --- NUESTRA FUNCIÓN PERSONALIZADA ---
# Creamos un protocolo (función) para registrar alumnos de forma ordenada
def registrar_alumno(nombre_nuevo, objetivo_nuevo):
    # Creamos un diccionario (ficha de cliente) con sus datos
    ficha_cliente = {
        "nombre": nombre_nuevo,
        "objetivo": objetivo_nuevo
    }
    # Guardamos la ficha dentro de la caja fuerte de la sesión
    st.session_state["lista_alumnos"].append(ficha_cliente)


# --- INTERFAZ VISUAL ---
col1, col2 = st.columns(2)

with col1:
    st.title("Centrum: Clinical Pilates")
    st.subheader("Clases grupales e inteligentes")
    st.write("Mejoramos tu postura y reducimos tu dolor con base clínica.")
    
    st.write("---")
    st.markdown("### 🧘 Registro de Alumno Nuevo")
    
    # Formulario de entrada
    nombre = st.text_input("¿Cómo te llamas?", key="input_nombre")
    
    horarios_salud = {
        "Dolor de Espalda / Lumbalgia": "Martes y Jueves a las 8:30 AM",
        "Post-parto / Suelo Pélvico": "Lunes y Miércoles a las 10:30 AM",
        "Rendimiento Deportivo / Flexibilidad": "Lunes y Miércoles a las 19:30 PM",
        "Adulto Mayor / Movilidad": "Martes y Jueves a las 11:30 AM"
    }
    
    objetivo_salud = st.selectbox(
        "¿Cuál es tu principal objetivo de salud?",
        list(horarios_salud.keys())
    )
    
    # Botón que activa la función
    if st.button("Confirmar Registro e Inscripción"):
        if nombre.strip() != "": # Validamos que no esté vacío
            # LLAMAMOS a la función pasándole los datos de las cajas de texto
            registrar_alumno(nombre, objetivo_salud)
            st.success(f"¡Excelente {nombre}! Te has registrado correctamente para: {objetivo_salud}")
        else:
            st.warning("Por favor, introduce tu nombre antes de confirmar.")

with col2:
    st.markdown("### 📊 Panel de Administración (Simulación DB)")
    st.write("Aquí verás en tiempo real los alumnos que se van registrando en esta sesión:")
    
    # Leemos la lista desde la caja fuerte y la mostramos en pantalla
    if len(st.session_state["lista_alumnos"]) == 0:
        st.info("Aún no hay alumnos registrados en esta sesión. ¡Sé el primero!")
    else:
        # Recorremos la lista de alumnos registrados usando un bucle for
        for i, alumno in enumerate(st.session_state["lista_alumnos"], 1):
            st.markdown(f"**{i}. {alumno['nombre']}** — 🎯 Objetivo: *{alumno['objective_salud' if 'objective_salud' in alumno else 'objetivo']}*")
            
    st.write("---")
    st.caption("Nota: Esta lista se mantendrá viva mientras mantengas la pestaña abierta gracias a st.session_state.")
