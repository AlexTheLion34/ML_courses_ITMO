import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('candy.csv', delimiter=',', index_col='competitorname')

train_data = data.drop(['Caramel Apple Pops', 'Hersheys Kisses'])

X = pd.DataFrame(train_data.drop(['winpercent'], axis=1))

y = pd.DataFrame(train_data['winpercent'])

model = LinearRegression().fit(X, y)

caramel_apple_pops = data.loc['Caramel Apple Pops', :].to_frame().T

hersheys_kisses = data.loc['Hersheys Kisses', :].to_frame().T

some_candy = [[1, 0, 0, 1, 1, 0, 0, 1, 1, 0.624, 0.438]]

caramel_apple_pops_pred = model.predict(caramel_apple_pops.drop(['winpercent'], axis=1))
hersheys_kisses_pred = model.predict(hersheys_kisses.drop(['winpercent'], axis=1))
some_candy_pred = model.predict(some_candy)

print('Caramel Apple Pops: ' + str(caramel_apple_pops_pred))
print('Hersheys Kisses: ' + str(hersheys_kisses_pred))
print('Some candy: ' + str(some_candy_pred))
