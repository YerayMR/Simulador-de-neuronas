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

# Sesgo
st.subheader("Sesgo")
sesgo = st.number_input("Introduce el valor del sesgo", min_value=-100.0, max_value=100.0, step=0.01, value=0.0)

# Selección de función de activación
st.subheader("Función de activación")
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





















#        # Pestaña 1: Una entrada y un peso
#        with tabs[0]:
#            st.subheader("Una neurona con una entrada y un peso")
#            peso = 0.5  # Peso ajustado
#            entrada = st.number_input("Introduzca el valor de la entrada", min_value=0.0, step=0.01, value=0.0)
#            if st.button("Calcular la salida", key="btn1"):
#                salida = peso * entrada
#                st.write(f"La salida de la neurona es: {salida:.2f}")
#        
#        # Pestaña 2: Dos entradas y dos pesos
#        with tabs[1]:
#            st.subheader("Dos entradas y dos pesos")
#            peso_w1 = 1.5  # Peso ajustado
#            peso_w2 = 2.5  # Peso ajustado
#            entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab2")
#            entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab2")
#            if st.button("Calcular la salida", key="btn2"):
#                salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2
#                st.write(f"La salida de la neurona es: {salida:.2f}")
#        
#        # Pestaña 3: Tres entradas, tres pesos y un sesgo
#        with tabs[2]:
#            st.subheader("Tres entradas, tres pesos y un sesgo")
#            peso_w1 = 1  # Peso ajustado
#            peso_w2 = 2  # Peso ajustado
#            peso_w3 = 3  # Peso ajustado
#            sesgo = 10  # Sesgo ajustado
#            entrada_x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, value=0.0, key="x1_tab3")
#            entrada_x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, value=0.0, key="x2_tab3")
#            entrada_x3 = st.number_input("Entrada x3", min_value=0.0, step=0.01, value=0.0, key="x3_tab3")
#            if st.button("Calcular la salida", key="btn3"):
#                salida = peso_w1 * entrada_x1 + peso_w2 * entrada_x2 + peso_w3 * entrada_x3 + sesgo
#                st.write(f"La salida de la neurona es: {salida:.2f}")