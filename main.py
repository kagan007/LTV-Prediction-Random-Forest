import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

dataset = pd.read_csv('final_dataset.csv')
x = dataset.iloc[:,:-1]
y = dataset.iloc[:, 9:10]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
user_ids = [int(x) for x in range(1, len(x_test)+1)]

model = RandomForestRegressor(n_estimators = 150, min_samples_split=4, min_samples_leaf=1, max_features='auto', max_depth=8, bootstrap=True, random_state=0)
model.fit(x_train, y_train)

prediction = model.predict(x_test)
rmse = (mean_squared_error(y_test, prediction))**.5
mae = mean_absolute_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print("Root Mean Squared Error: " + str(rmse))
print("Mean Absolute Error: " + str(mae))
print("R2 Score: " + str(r2))

plt.scatter(user_ids, prediction, color="green")
plt.scatter(user_ids, y_test, color="blue")
plt.title("Lifetime Value Prediction")
plt.xlabel("Users")
plt.ylabel("Ads After Day0")
plt.show()

plt.plot(user_ids, prediction, color="green")
plt.scatter(user_ids, y_test, color="blue")
plt.title("Lifetime Value Prediction")
plt.xlabel("Users")
plt.ylabel("Ads After Day0")
plt.show()