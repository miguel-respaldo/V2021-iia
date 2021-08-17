import tensorflow as tf
import numpy as np
import matplotlib as plt

# Programa que convierte de grados Celsius a grados Fahrenheit

# ejemplos que la red usará para aprender
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Unit es el número de neuronas de salida
# input_shape es el número de neuronas de entrada
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    # 0.1 es la taza a prendizaje
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
# Con fit entrenamos nuestra red neuronal
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

#plt.xlabel("# Epoca")
#plt.ylabel("Magnitud de pérdida")
#plt.plot(historial.history["loss"])

print("Hagamos una predicción!")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado) + " fahrenheit!")