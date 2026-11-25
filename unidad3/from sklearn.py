from sklearn.linear_model import LinearRegression

# Datos de ejemplo
X = [[50], [60], [70], [80]]  # metros cuadrados
y = [150000, 180000, 210000, 240000]  # precios

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción para una casa de 75 m2
print("Precio estimado:", modelo.predict([[75]])[0])