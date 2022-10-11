import matplotlib.pyplot as plt
import pandas as pd
print("------------- USO DE LA LIBRERIA PANDAS ---------------")
print("------------ DEPRESSION TWITTER DATASET ---------------")
DT = pd.read_csv("Mental-Health-Twitter.csv")
print(DT.head())
print(DT.columns)
print(DT.dtypes)
#pd.set_option('display.max_rows', 11)
print(DT)
print(len(DT))

print(DT.describe())
print("------------- Sin ordenar ---------------")
print(DT['followers'].value_counts())
print("------------- Ascendente ----------------")
print(DT['followers'].value_counts(ascending=True))
Variable = DT[DT['label'] == 0]
print(Variable)
print(len(Variable))
print(DT['retweets'].value_counts(ascending=True))
print(DT['user_id'].value_counts(ascending=True))


print("------------- MATPLOTLIB ---------------")

DT['text_length'] = DT['post_text'].apply(len)
DT['text_length'].plot(kind='hist', bins=50, figsize=(7, 5))
print(DT['text_length'].describe())
plt.show()

