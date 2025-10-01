import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde archivo local con encoding adecuado
df = pd.read_csv(r"C:\Users\User\Documents\GitHub\RepoProyectoIO\TPFinal IO\sales_data_sample_clean.csv", encoding="latin1")

# Crear columna MES_GLOBAL: enero 2003 = 1, ..., mayo 2005 = 29
df["MES_GLOBAL"] = (df["YEAR_ID"] - 2003) * 12 + df["MONTH_ID"]

# Filtrar solo los meses 1 a 29
df = df[df["MES_GLOBAL"].between(1, 29)]

# Agrupar cantidad de ventas por MES_GLOBAL y PRODUCTLINE
ventas_por_mes = df.groupby(["MES_GLOBAL", "PRODUCTLINE"]).size().unstack(fill_value=0)

# Graficar
plt.figure(figsize=(14,6))
for productline in ventas_por_mes.columns:
    plt.plot(ventas_por_mes.index, ventas_por_mes[productline], marker="o", label=productline)

plt.title("Cantidad de ventas por ProductLine y mes (1-29)")
plt.xlabel("Mes global")
plt.ylabel("Cantidad de ventas")
plt.xticks(ticks=range(1,30), labels=range(1,30), rotation=0)
plt.legend(title="ProductLine")
plt.grid(True)
plt.tight_layout()
plt.show()

