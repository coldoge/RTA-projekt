import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from statsmodels.api import OLS

df = pd.read_csv('data/final_audi_a6_data.csv', index_col=0)
df.drop("Rok produkcji", axis=1, inplace=True)

categorical_columns = ['Oferta od', 'Rodzaj paliwa', 'Skrzynia biegów', 'Napęd', 'Typ nadwozia', 'Kolor', 'Stan']
numerical_columns = [x for x in df.columns if x not in categorical_columns and x != 'Cena']
df_cat = pd.get_dummies(df[categorical_columns], drop_first=True)

df_numeric = df[numerical_columns]

X = df_cat.join(df_numeric)
y = df['Cena']
# 4 na 4 dolaczony automatycznie
# bezowy
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2137, test_size=0.2)

model = OLS(y_train, X_train, hasconst=True)
res = model.fit()
print(res.summary())

X_train.drop(['Typ nadwozia_Sedan', 'Napęd_Na przednie koła', 'Pojemność skokowa', 'Napęd_4x4 (stały)'], axis=1, inplace=True)
X_test.drop(['Typ nadwozia_Sedan', 'Napęd_Na przednie koła', 'Pojemność skokowa', 'Napęd_4x4 (stały)'], axis=1, inplace=True)

model2 = OLS(y_train, X_train, hasconst=True)
res2 = model2.fit()
print(res2.summary())

y_pred = model2.predict(res2.params, X_test)
plt.plot(y_pred)
plt.plot(y_test.reset_index(drop=True))
plt.show()