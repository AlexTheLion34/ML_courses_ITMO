import pandas as pd

data = pd.read_csv("salary_and_population.csv", delimiter=',')

print("Выборочное среднее з/п: " + str(data['AVG_Salary'].mean()))
print("Выборочная медина з/п: " + str(data['AVG_Salary'].median()))
print("Оценка дисперсии з/п: " + str(data['AVG_Salary'].var(ddof=0)))
print("Среднеквадраитческое отклонение з/п: " + str(data['AVG_Salary'].std(ddof=0)))
