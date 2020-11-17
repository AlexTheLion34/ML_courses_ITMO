import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('data.csv', delimiter=',', index_col='id')

X = pd.DataFrame(data.drop(['Class'], axis=1))

y = pd.DataFrame(data['Class']).values.ravel()

model_1 = KNeighborsClassifier(n_neighbors=3, p=2)

model_1.fit(X, y)

point = [67, 43]

print('Расстояние от нового объекта с координатами (67, 43) до ближайшего соседа, используя евклидову метрику: '
      + str(model_1.kneighbors([point])[0][0][0]))
print('Идентификатры трех ближайших точек к (67, 43) для евклидовой метрики: ' + str(model_1.kneighbors([point])))
print('Класс для нового объекта с координатами (67, 43) при и евклидовой метрике: ' + str(model_1.predict([point])))

model_2 = KNeighborsClassifier(n_neighbors=3, p=1)
model_2.fit(X, y)

print()

print('Расстояние от нового объекта с координатами (67, 43) до ближайшего соседа, используя метрику городских '
      'кварталов: '
      + str(model_2.kneighbors([point])[0][0][0]))
print('Идентификатры трех ближайших точек к (67, 43) для метрики городских кварталов: ' + str(model_2.kneighbors([point])))
print('Класс для нового объекта с координатами (67, 43) при метрике городских кварталов: ' + str(model_2.predict([point])))
