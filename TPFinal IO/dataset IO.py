from pathlib import Path
import pandas as pd

# Ruta absoluta al archivo (ajústala si la movés)
csv_path = Path(r"C:\Users\User\Documents\IO\sales_data_sample.csv")


# Lectura robusta: intenta UTF-8 y si falla prueba cp1252 y latin1
encodings = ["utf-8", "cp1252", "latin1"]
last_err = None
for enc in encodings:
    try:
        DS = pd.read_csv(csv_path, encoding=enc, sep=None, engine="python", on_bad_lines="skip")
        print(f"Leído OK con encoding={enc}")
        break
    except Exception as e:
        last_err = e
else:
    raise last_err  # si todas fallan, muestra el último error

# Elimina filas duplicadas
DS_sin_duplicados = DS.drop_duplicates()

# Opcional: guarda el resultado en un nuevo CSV
DS_sin_duplicados.to_csv("sales_data_sample_sin_duplicados.csv", index=False)

# Muestra cuántas filas había antes y cuántas después de eliminar duplicados
print(f"Filas antes: {len(DS)}, después de eliminar duplicados: {len(DS_sin_duplicados)}")

# Función: Devuelve una lista de los productlines más vendidos (por cantidad), de mayor a menor
def productlines_mas_vendidos(df):
    # Agrupa por PRODUCTLINE y suma la cantidad vendida
    resumen = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().reset_index()
    # Ordena de mayor a menor cantidad
    resumen = resumen.sort_values(by='QUANTITYORDERED', ascending=False)
    # Convierte el resultado a una lista de listas
    matriz = resumen.values.tolist()
    return matriz

# Función: Devuelve el productline que más ganancia dejó y el monto total
def productline_mas_ganancia(df):
    # Agrupa por PRODUCTLINE y suma las ventas (SALES)
    resumen = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    # Ordena de mayor a menor ganancia
    resumen = resumen.sort_values(by='SALES', ascending=False)
    # Devuelve el nombre del productline y la ganancia máxima
    return resumen.iloc[0]['PRODUCTLINE'], resumen.iloc[0]['SALES']

# Función: Devuelve una lista de países ordenados por el volumen total de compras (ventas), de mayor a menor
def paises_mayor_volumen_compras(df):
    # Agrupa por COUNTRY y suma las ventas (SALES)
    resumen = df.groupby('COUNTRY')['SALES'].sum().reset_index()
    # Ordena de mayor a menor ventas
    resumen = resumen.sort_values(by='SALES', ascending=False)
    # Convierte el resultado a una lista de listas
    matriz = resumen.values.tolist()
    return matriz

# Función: Devuelve una lista de países ordenados por la cantidad total de compras, de mayor a menor
def paises_mayor_cantidad_compras(df):
    # Agrupa por COUNTRY y suma la cantidad vendida
    resumen = df.groupby('COUNTRY')['QUANTITYORDERED'].sum().reset_index()
    # Ordena de mayor a menor cantidad
    resumen = resumen.sort_values(by='QUANTITYORDERED', ascending=False)
    # Convierte el resultado a una lista de listas
    matriz = resumen.values.tolist()
    return matriz

# Función: Devuelve cada estado (STATUS) junto a la cantidad de filas que tiene
def cantidad_por_status(df):
    # Agrupa por STATUS y cuenta la cantidad de filas por cada estado
    resumen = df['STATUS'].value_counts().reset_index()
    resumen.columns = ['STATUS', 'CANTIDAD']
    # Convierte el resultado a una lista de listas
    matriz = resumen.values.tolist()
    return matriz

# Ejemplo de uso de las funciones anteriores

# Muestra los productlines más vendidos
resultado = productlines_mas_vendidos(DS_sin_duplicados)
print("Productlines más vendidos (cantidad):")
print(resultado)

# Muestra el productline con más ganancia
productline, ganancia = productline_mas_ganancia(DS_sin_duplicados)
print(f"Productline con más ganancia: {productline} (${ganancia:,.2f})")

# Muestra los países con mayor volumen de compras (ventas)
paises_volumen = paises_mayor_volumen_compras(DS_sin_duplicados)
print("Países por volumen de compras (ventas):")
print(paises_volumen)

# Muestra los países con mayor cantidad de compras
paises_cantidad = paises_mayor_cantidad_compras(DS_sin_duplicados)
print("Países por cantidad de compras:")
print(paises_cantidad)

# Muestra la cantidad de filas por cada estado
status_cantidades = cantidad_por_status(DS_sin_duplicados)
print("Estado        | Cantidad")
print("-------------------------")
for estado, cantidad in status_cantidades:
    print(f"{estado:<13} | {cantidad}")

