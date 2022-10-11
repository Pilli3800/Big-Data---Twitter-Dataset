import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv("peso_caja_controlQ.csv")
print(datos.describe())

datos['rounded'] = datos.weight.round(2)
datos['diff'] = datos['rounded'] - 20
print(datos.describe())

freq = datos['rounded'].value_counts().reset_index()
print(freq.describe())
freq.columns = ['weight', 'frequency']
print(freq)
plt.figure(figsize=(18, 8))
plt.ylabel('Frequency')
plt.xlabel('Weight')
plt.plot(freq.weight, freq.frequency, "o", markersize=10, color='g')
plt.show()

# import numpy as np
# mtcars = pd.read_csv("peso_caja_controlQ.csv")
# print (mtcars)

# mtcars['weight'].value_counts().plot(kind = 'bar')
# plt.show()

# new_df = pd.value_counts(mtcars.weight).reset_index()
# new_df.columns = ['weight', 'frequency']
# print (new_df)

