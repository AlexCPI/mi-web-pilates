import streamlit as st

# 1. TÍTULO Y PRESENTACIÓN DE TU MARCA
st.title("Centrum: Clinical Pilates")
st.subheader("Clases grupales en el corazón de la ciudad")
st.write("Mejoramos tu postura, reducimos tu dolor y fortalecemos tu cuerpo con base clínica.")

# 2. LISTA DE SERVICIOS
servicios_pilates = [
    "Clases Grupales Reducidas (Máx. 6 personas)",
    "Evaluación de Postura Inicial",
    "Pilates Terapéutico y Readaptación",
    "Control Motor y Flexibilidad"
]

st.markdown("### Lo que ofrecemos:")
for servicio in servicios_pilates:
    st.write(f"✅ {servicio}")

# 3. FORMULARIO DE NIVELACIÓN
st.write("---")
st.markdown("### 🧘 Descubre tu horario ideal")

nombre = st.text_input("¿Cómo te llamas?")
nivel = st.radio(
    "Selecciona tu nivel de experiencia en Pilates:",
    ["Principiante", "Intermedio/Avanzado"]
)

if nombre: 
    if nivel == "Principiante":
        st.write(f"Hola {nombre}, te recomendamos el grupo de **Martes y Jueves a las 9:30 AM** (Enfoque en técnicas básicas).")
    else:
        st.write(f"Hola {nombre}, tu grupo ideal es el de **Lunes y Miércoles a las 19:30 PM** (Progreso y control dinámico).")

# 4. BOTÓN FINAL DE CONTACTO
st.write("---")
if st.button("Consultar horarios y reservar plaza"):
    st.success("¡Excelente decisión! Te esperamos en nuestro centro en la Calle Mayor, Nº 12 (Plaza Central).")
    st.info("📱 Envíanos un mensaje al WhatsApp: +34 600 000 000 para asignarte tu grupo.")
