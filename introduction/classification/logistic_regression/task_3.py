import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

data = pd.read_csv('candy_train.csv', delimiter=',', index_col='competitorname')

train_data = data.drop(['Candy Corn', 'Haribo Twin Snakes', 'Peanut butter M&Ms'])

X = pd.DataFrame(train_data.drop(['winpercent', 'Y'], axis=1))

y = pd.DataFrame(train_data['Y'])

model = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())

werthers_original_caramel = model.predict_proba([[1, 0, 1, 0, 0, 0, 1, 0, 0, 0.186, 0.26699999]])

super_bubble = model.predict_proba([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0.162, 0.116]])

print('Werthers Original Caramel: ' + str(werthers_original_caramel))
print('Super Bubble: ' + str(super_bubble))

test_data = pd.read_csv('candy_test.csv', delimiter=',', index_col='competitorname')

X_test = pd.DataFrame(test_data.drop(['Y'], axis=1))

y_pred = model.predict(X_test)

y_true = test_data['Y'].to_frame().T.values.ravel()

fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred)

print('Recall: ' + str(metrics.recall_score(y_true, y_pred)))
print('Precision: ' + str(metrics.precision_score(y_true, y_pred)))
print('AUC: ' + str(metrics.auc(fpr, tpr)))
