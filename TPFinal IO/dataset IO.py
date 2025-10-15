import pandas as pd
import numpy as np


# Cargar el dataset desde un archivo CSV
df = pd.read_csv(r'C:\Users\User\Documents\GitHub\RepoProyectoIO\TPFinal IO\sales_data_sample_clean.csv')

#eliminar las filas cuyo estado no sea delivered
df = df[df['STATUS'] == 'Shipped']

#guardar el dataset limpio en el mismo archivo
df.to_csv(r'C:\Users\User\Documents\GitHub\RepoProyectoIO\TPFinal IO\sales_data_sample_clean.csv', index=False)