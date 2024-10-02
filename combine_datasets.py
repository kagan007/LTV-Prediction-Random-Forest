import pandas as pd
import numpy as np

data1 = pd.read_csv("data_x.csv") #ads, sessions, events
data2 = pd.read_csv("new_data_x.csv") #encoded install timezones and events
data3 = pd.read_csv("touch_times.csv") #touch times
y_data = pd.read_csv("data_y.csv")

data2 = data2.iloc[:,:-1] #remove events
dataset = data1.join(data2)
final_dataset = dataset.join(data3)
final_dataset = final_dataset.join(y_data)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
np.savetxt("final_dataset.csv", final_dataset, delimiter=",")
