from operator import le
import pandas as pd 
print("------------- PANDAS ---------------")
SF = pd.read_csv("Map-Crime_Incidents-Previous_Three_Months.csv")
print(SF.head())
print(SF.columns)
print(SF.dtypes)
# pd.set_option('display.max_rows', 10)
print(SF)
print(len(SF))
print(SF.describe(include='all'))
print("------------- Sin ordenar ---------------")
print(SF['Category'].value_counts())
print("------------- Ascendente ----------------")
print(SF['Category'].value_counts(ascending=True))
print("------------- AugustCrimeB --------------")
AugustCrimeB = SF[SF['Category'] == 'BURGLARY']
print(len(AugustCrimeB))
print("------------- Actividad 5 ---------------")
SF.insert(12, "Nueva columna", 30)
print(SF.columns)

Variables_especificas = SF[["Category", "DayOfWeek"]]
print(Variables_especificas)

SF.drop('Nueva columna', inplace=True, axis=1)
print(SF.columns)

dias_Semana = SF['DayOfWeek']
print(dias_Semana)
dias_Semana.replace(to_replace="Sunday",
           value="Domingo", inplace=True)
print(dias_Semana)

print("------------- MATPLOTLIB ---------------")
import matplotlib.pyplot as plt
plt.plot(SF['X'], SF['Y'], 'ro')
plt.show()

print("------------- NUMPY ---------------")
import numpy as np
pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
print(pd_districts_levels)
SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])
plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()

