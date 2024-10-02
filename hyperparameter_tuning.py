from sklearn.ensemble import RandomForestRegressor
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd

x = pd.read_csv('new_data_x.csv')
y = pd.read_csv('data_y.csv')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

n_estimators = [10, 25, 50, 100, 150, 200, 250, 300]
max_features = ["auto"]
max_depth = [2, 4, 6, 8, 10]
min_samples_split = [2, 4, 6, 8, 10]
min_samples_leaf = [1, 2, 3, 4, 5]
bootstrap = [True, False]

random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
rf = RandomForestRegressor()
rf_random = HalvingRandomSearchCV(estimator=rf, param_distributions=random_grid, cv=5, verbose=2, n_jobs=-1)
rf_random.fit(x_train, y_train)
results = rf_random.best_params_
print("Best parameters: " + str(results))