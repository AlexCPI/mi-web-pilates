# NUEVO: Formulario de recomendación de horarios
st.write("---")
st.markdown("### 🧘 Descubre tu horario ideal")

# Pedimos el nombre del cliente
nombre = st.text_input("¿Cómo te llamas?")

# Ofrecemos las opciones de nivel
nivel = st.radio(
    "Selecciona tu nivel de experiencia en Pilates:",
    ["Principiante", "Intermedio/Avanzado"]
)

# El Condicional: Evaluamos la respuesta para recomendar un horario
if nombre: # Si el usuario ha escrito su nombre...
    if nivel == "Principiante":
        st.write(f"Hola {nombre}, te recomendamos el grupo de **Martes y Jueves a las 9:30 AM** (Enfoque en técnicas básicas).")
    else:
        st.write(f"Hola {nombre}, tu grupo ideal es el de **Lunes y Miércoles a las 19:30 PM** (Progreso y control dinámico).")
