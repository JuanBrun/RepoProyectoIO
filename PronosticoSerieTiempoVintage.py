import os
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Cargar el archivo CSV ===
# Intentamos varias rutas comunes: misma carpeta del script y la subcarpeta 'TPFinal IO'
filename = 'sales_data_sample_clean.csv'
base_dir = os.path.dirname(__file__) or os.getcwd()
candidate_paths = [
    os.path.join(base_dir, filename),
    os.path.join(base_dir, 'TPFinal IO', filename),
    os.path.join(base_dir, 'TPFinal_IO', filename),
]

file_path = None
for p in candidate_paths:
    if os.path.exists(p):
        file_path = p
        break

if file_path is None:
    tried = '\n'.join(candidate_paths)
    raise SystemExit(f"Archivo no encontrado. Rutas probadas:\n{tried}\n\nColoca '{filename}' en una de esas rutas o ejecuta el script desde la carpeta que lo contenga.")

df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)

# Convertir ORDERDATE a datetime si no lo está ya
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Agregar columnas de año y mes
df['Year_Month'] = df['ORDERDATE'].dt.to_period('M')

# Filtrar DataFrames por PRODUCTLINE
df_vintage = df[df['PRODUCTLINE'] == 'Vintage Cars']

# === 2. Gráfica de Ventas Mensuales ===
# Agrupar datos por año-mes y contar apariciones
vintage_monthly = df_vintage.groupby('Year_Month')['ORDERNUMBER'].count()

# Crear la gráfica
plt.figure(figsize=(15, 6))

# Graficar ambas líneas
plt.plot(vintage_monthly.index.astype(str), vintage_monthly.values, 
         marker='s', label='Vintage Cars', linewidth=2)

# Personalizar la gráfica
plt.title('Ventas Mensuales de vintage cars', fontsize=14)
plt.xlabel('Año-Mes', fontsize=12)
plt.ylabel('Número de Ventas', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

# Rotar etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45)

# Ajustar márgenes
plt.tight_layout()

# Mostrar la gráfica
plt.show()
print("\nVintage Cars:")
print(f"Total de ventas: {vintage_monthly.sum()}")
print(f"Promedio mensual: {vintage_monthly.mean():.2f}")
print(f"Máximo mensual: {vintage_monthly.max()}")
print(f"Mínimo mensual: {vintage_monthly.min()}")

# Crear DataFrame con número de mes y ventas
monthly_sales = pd.DataFrame({
    'Mes': range(1, len(vintage_monthly) + 1),
    'Ventas': vintage_monthly.values
})

# Guardar a CSV
output_path = os.path.join(base_dir, 'vintage_monthly_sales.csv')
monthly_sales.to_csv(output_path, index=False)

print(f"\nArchivo CSV generado en: {output_path}")