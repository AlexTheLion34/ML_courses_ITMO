import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

data = pd.read_csv('data.csv', delimiter=',', index_col='Object')

train_data = data.drop('Cluster', axis=1)

model = KMeans(n_clusters=3, init=np.array([[12.0, 11.5], [12.71, 13.43], [10.5, 8.75]]), max_iter=100, n_init=1)

clusters = model.fit(train_data)

print('Назначенные кластеры: ' + str(clusters.labels_.tolist()))

distances = model.fit_transform(train_data)

print('Расстояния до всех центроидов: ' + str(distances))

print((4.16496564 + 3.19438282 + 6.26131629 + 4.16496564 + 3.05727637 + 2.57539377 + 3.53409054) / 7)
