import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

x = pd.read_csv('new_data_x.csv')
y = pd.read_csv('data_y.csv')

model = RandomForestRegressor(n_estimators = 150, min_samples_split=4, min_samples_leaf=1, max_features='auto', max_depth=8, bootstrap=True, random_state=0)
model.fit(x, y)

importances = permutation_importance(model, x, y, n_repeats=10, random_state=0)
results = importances.importances_mean

data = {'Ads':results[0], 'Sessions':results[1], 'Events:':results[2]}

features = list(data.keys())
importances = list(data.values())

plt.bar(features, importances, color='blue', width=0.5)
plt.xlabel('Feautres')
plt.ylabel('Importances')
plt.title('Feauture importances')
plt.show()