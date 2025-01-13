import streamlit as st
import numpy as np

# Clase Neurona
class Neuron:
    def __init__(self, weights, bias, func):
        self.weights = weights
        self.bias = bias
        self.func = func

    def run(self, input_data):
        result = sum(w * i for w, i in zip(self.weights, input_data)) + self.bias
        if self.func == "ReLU":
            return max(0, result)
        elif self.func == "Sigmoide":
            return 1 / (1 + np.exp(-result))
        elif self.func == "Tangente hiperbólica":
            return np.tanh(result)
        return result

    def change_bias(self, new_bias):
        self.bias = new_bias

# Configuración de la página
st.set_page_config(page_title="Neurona Artificial", page_icon="🤖")
st.title("Simulación de Neurona Artificial")

# Control deslizante para el número de entradas/pesos
n = st.slider("Elige el número de entradas/pesos que tendrá la neurona", min_value=1, max_value=10, value=2)

# Contenedores para los pesos y las entradas
st.subheader("Pesos")
pesos = [st.number_input(f"w_{i}", min_value=-100.0, max_value=100.0, step=0.01, value=0.0) for i in range(n)]

st.subheader("Entradas")
entradas = [st.number_input(f"x_{i}", min_value=-100.0, max_value=100.0, step=0.01, value=0.0) for i in range(n)]

st.subheader("Sesgo y Función de activación")
sesgo = st.number_input("Introduce el valor del sesgo", min_value=-100.0, max_value=100.0, step=0.01, value=0.0)
funcion_activacion = st.selectbox("Elige la función de activación", ["Sigmoide", "ReLU", "Tangente hiperbólica"])

# Botón para calcular la salida
if st.button("Calcular la salida"):
    # Crear la instancia de la clase Neurona
    neurona = Neuron(weights=pesos, bias=sesgo, func=funcion_activacion)
    salida = neurona.run(input_data=entradas)

    # Mostrar el resultado
    st.subheader("Salida de la neurona")
    st.write(salida)

# Mostrar los valores actuales
st.write("Pesos (w) =", pesos)
st.write("Entradas (x) =", entradas)