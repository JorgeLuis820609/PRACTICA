import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de Vehículos en Venta (USA) 🚗")

# Botón de histograma
if st.button("Mostrar histograma de odómetro"):
    st.write("Histograma del kilometraje (odometer)")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón de gráfico de dispersión
if st.button("Mostrar gráfico de dispersión precio vs odómetro"):
    st.write("Relación entre precio y kilometraje")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
