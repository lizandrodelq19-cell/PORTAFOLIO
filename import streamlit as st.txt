import streamlit as st

# URL del logo institucional oficial de la USS
LOGO_USS_URL = "https://uss.cl"

# =========================================================================
# 1. COMPONENTES DE LA BARRA LATERAL (Sidebar)
# =========================================================================
with st.sidebar:
    # Títulos e información
    st.header("Mi primera barra lateral de Streamlit")
    st.subheader("¡Hola, Barra Lateral!")
    st.write("Esto es una barra lateral")
    
    # Imagen del logo institucional
    st.image(LOGO_USS_URL, width=200)
    
    # Botón interactivo
    st.button("Haz clic pero en la barra lateral")
    
    # Entrada de texto (Input)
    texto_barra = st.text_input("Escribe algo en la barra:")
    
    # Salida dinámica que procesa la entrada (Output)
    st.write(f"Escribiste en la barra: {texto_barra}")


# =========================================================================
# 2. COMPONENTES DEL ÁREA PRINCIPAL (Main Area)
# =========================================================================
# Títulos e información principal
st.header("Mi primera aplicación de Streamlit")
st.subheader("¡Hola, Streamlit!")
st.write("Esta es una aplicación simple")

# Imagen del logo institucional
st.image(LOGO_USS_URL, width=250)

# Botón interactivo
st.button("Haz clic")

# Entrada de texto (Input)
texto_principal = st.text_input("Escribe algo:")

# Salida dinámica que procesa la entrada (Output)
st.write(f"Escribiste: {texto_principal}")
