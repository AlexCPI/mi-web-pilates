import streamlit as st

# 1. TÍTULO Y PRESENTACIÓN
st.title("Centrum: Clinical Pilates")
st.subheader("Clases grupales en el corazón de la ciudad")
st.write("Mejoramos tu postura, reducimos tu dolor y fortalecemos tu cuerpo con base clínica.")

# 2. LISTA DE SERVICIOS GENERALES
servicios_pilates = [
    "Clases Grupales Reducidas (Máx. 6 personas)",
    "Evaluación de Postura Inicial",
    "Pilates Terapéutico y Readaptación",
    "Control Motor y Flexibilidad"
]

st.markdown("### Lo que ofrecemos:")
for servicio in servicios_pilates:
    st.write(f"✅ {servicio}")

# --- AQUÍ EMPIEZA LA NUEVA OPCIÓN B ---
# 3. EL DICCIONARIO DE HORARIOS (El cerebro de la app)
# Asociamos cada objetivo de salud con su grupo recomendado
horarios_salud = {
    "Dolor de Espalda / Lumbalgia": "Martes y Jueves a las 8:30 AM (Enfoque terapéutico y descompresión)",
    "Post-parto / Suelo Pélvico": "Lunes y Miércoles a las 10:30 AM (Recuperación segura y control motor)",
    "Rendimiento Deportivo / Flexibilidad": "Lunes y Miércoles a las 19:30 PM (Progreso dinámico y fuerza)",
    "Adulto Mayor / Movilidad": "Martes y Jueves a las 11:30 AM (Movilidad suave y prevención de caídas)"
}

st.write("---")
st.markdown("### 🧘 Tu Recomendación de Salud Personalizada")

nombre = st.text_input("¿Cómo te llamas?")

# Creamos un selector desplegable con las claves de nuestro diccionario
objetivo_salud = st.selectbox(
    "¿Cuál es tu principal objetivo o necesidad de salud actual?",
    list(horarios_salud.keys()) # Esto extrae automáticamente las opciones del diccionario
)

# El Condicional Inteligente: extrae la información usando la clave seleccionada
if nombre:
    horario_recomendado = horarios_salud[objetivo_salud]
    st.info(f"Hola **{nombre}**, basándonos en tu objetivo de *{objetivo_salud}*, tu grupo ideal es:")
    st.success(f"🗓️ **{horario_recomendado}**")

# 4. BOTÓN FINAL DE CONTACTO
st.write("---")
if st.button("Consultar plazas y reservar"):
    st.success("¡Excelente decisión! Te esperamos en nuestro centro en la Calle Mayor, Nº 12 (Plaza Central).")
    st.info("📱 Envíanos un mensaje al WhatsApp: +34 600 000 000 para confirmar tu asistencia.")
