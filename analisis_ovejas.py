import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Cargar datos
df = pd.read_csv("ovejas.csv")

# Mostrar información
print(df.head())
print(df.describe())

# Conteo de enfermedades
enfermedades = df["Enfermedad"].value_counts()
print(enfermedades)

# Promedio de peso por tipo de alimento
peso_promedio = df.groupby("Tipo_Alimento")["Peso"].mean()
print(peso_promedio)

# Gráfico
peso_promedio.plot(kind="bar")
plt.title("Peso promedio por tipo de alimento")
plt.xlabel("Tipo de alimento")
plt.ylabel("Peso")
plt.show()