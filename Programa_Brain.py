import matplotlib.pyplot as plt
import pandas as pd

brainFrame = pd.read_csv("brainsize.txt")
print(brainFrame.head())

import numpy as np
import matplotlib.pyplot as plt
menDf = brainFrame[(brainFrame.Gender == 'Male')]
menMeanSmarts = menDf[ [ "PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])
plt.show()


womenDf = brainFrame[(brainFrame.Gender == 'Female')]
womanMeanSmarts = womenDf[ [ "PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(womanMeanSmarts, womenDf["MRI_Count"])
plt.show()

print("Correlacion de Pearson")
print(brainFrame.corr(method='pearson'))

print("Correlacion de Pearson - Hombres")
print(menDf.corr(method='pearson'))

print("Correlacion de Pearson - Mujeres")
print(womenDf.corr(method='pearson'))

import seaborn as sns
womenNoGenderDf = womenDf.drop('Gender', axis=1)
womenNoGenderDf = womenNoGenderDf[womenNoGenderDf.columns].astype(float)
wcorr = womenNoGenderDf.corr()
sns.heatmap(wcorr)
plt.savefig("wHeatMap.png")

menNoGenderDf = menDf.drop('Gender', axis=1)
menNoGenderDf = menNoGenderDf[menNoGenderDf.columns].astype(float)
wcorr = menNoGenderDf.corr()
sns.heatmap(wcorr)
plt.savefig("mHeatMap.png")