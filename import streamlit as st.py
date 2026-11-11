import streamlit as st


LOGO_USS_URL = "https://mi.uss.cl/_next/static/media/logoUSSWithLabel.fc3b9027.svg"


with st.sidebar:
   
    st.header("Mi primera barra lateral de Streamlit")
    st.subheader("¡Hola, Barra Lateral!")
    st.write("Esto es una barra lateral")
    
   
    st.image(LOGO_USS_URL, width=200)
    
    
    st.button("Haz clic pero en la barra lateral")
    
    
    texto_barra = st.text_input("Escribe algo en la barra:")
    
   
    st.write(f"Escribiste en la barra: {texto_barra}")



st.header("Mi primera aplicación de Streamlit")
st.subheader("¡Hola, Streamlit!")
st.write("Esta es una aplicación simple")


st.image(LOGO_USS_URL, width=250)


st.button("Haz clic")


texto_principal = st.text_input("Escribe algo:")


st.write(f"Escribiste: {texto_principal}")
