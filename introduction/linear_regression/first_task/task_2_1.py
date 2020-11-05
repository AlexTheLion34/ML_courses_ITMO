import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from functools import reduce

data = pd.read_csv("data.csv", delimiter=',', index_col='id')

print("Выборочное среднее X: " + str(data['X'].mean()))
print("Выборочное среднее Y: " + str(data['Y'].mean()))

X = pd.DataFrame(data.drop(['Y'], axis=1))

y = pd.DataFrame(data['Y'])

model = LinearRegression().fit(X, y)

y_true = reduce(list.__add__, pd.DataFrame(data.drop(['X'], axis=1)).values.tolist())
y_pred = reduce(list.__add__, model.predict(pd.DataFrame(data.drop(['Y'], axis=1))).tolist())

print(model.intercept_)
print(model.coef_)

print(r2_score(y_true, y_pred))
