import pandas as pd
import matplotlib.pyplot as plt

# URL en formato CSV
url = "https://docs.google.com/spreadsheets/d/1IkaOPG1WRuUfkK05vamG-eOM_ZNt-VuyFCTx8zLx5JA/export?format=csv"
df = pd.read_csv(url)

# Agrupar ventas por año
ventas_por_año = df.groupby("YEAR_ID")["SALES"].sum()

# Graficar
plt.figure(figsize=(8,5))
ventas_por_año.plot(kind="bar", color="skyblue")
plt.title("Ventas totales por año")
plt.xlabel("Año")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()