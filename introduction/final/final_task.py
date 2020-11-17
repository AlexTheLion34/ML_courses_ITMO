import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("data.csv", delimiter=',')

print("Выборочное среднее MIP: " + str(data['MIP'].mean()))

train_data = pd.DataFrame(data.drop(['TARGET'], axis=1))

x = train_data.values
x_normalized = preprocessing.MinMaxScaler().fit_transform(x)
train_data = pd.DataFrame(x_normalized)

print("Выборочное среднее MIP после нормировки: " + str(train_data[0].mean()))

X = train_data
y = pd.DataFrame(data['TARGET'])

model = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())

print('Вертяности отнесения звезды к классам 0 и 1: ' +
      str(model.predict_proba([[0.298, 0.509, 0.657, 0.141, 0.318, 0.996, 0.267, 0.452]])))

model_1 = KNeighborsClassifier(n_neighbors=5, p=2)
model_1.fit(X, y.values.ravel())

print('Расстояние от новой звезды до ближайшего соседа, используя евклидову метрику: '
      + str(model_1.kneighbors([[0.298, 0.509, 0.657, 0.141, 0.318, 0.996, 0.267, 0.452]])[0][0][0]))

print('Класс новой звезды: ' + str(model_1.predict([[0.298, 0.509, 0.657, 0.141, 0.318, 0.996, 0.267, 0.452]])))
