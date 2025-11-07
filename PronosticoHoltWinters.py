# ==========================================
# Pronóstico de serie de tiempo con Holt-Winters
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv(r"C:\Users\User\Documents\GitHub\RepoProyectoIO\classic_monthly_sales.csv")


modelo = ExponentialSmoothing(
    df["Ventas"],
    trend="add",          # tendencia aditiva
    seasonal="add",       # estacionalidad aditiva
    seasonal_periods=12   # 12 meses en un ciclo anual
).fit()

# === 4. Pronóstico hasta el mes 36 ===
# Queremos llegar hasta 36 meses, así que proyectamos 36 - 29 = 7 períodos más
pasos_futuros = 36 - len(df)
pronostico = modelo.forecast(pasos_futuros)

# === 5. Combinar histórico + pronóstico ===
serie_completa = pd.concat([df["Ventas"], pronostico])

# === 6. Visualizar resultados ===
plt.figure(figsize=(15, 6))
plt.plot(df.index, df["Ventas"], label="Histórico", marker="o")
plt.plot(pronostico.index, pronostico, label="Pronóstico (Holt-Winters)", color="red", marker="x")
plt.axvline(df.index[-1], color="gray", linestyle="--", alpha=0.7)
plt.title("Pronóstico de Ventas - Método de Holt-Winters")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.legend()
plt.grid(True)

# Modificar el eje X para mostrar todos los meses
plt.xticks(serie_completa.index, rotation=45)
plt.tight_layout()  # Ajustar layout para que no se corten las etiquetas

plt.show()

# === 7. Mostrar valores pronosticados ===
print("\nPronóstico de ventas (meses 30 a 36):")
print(pronostico)
