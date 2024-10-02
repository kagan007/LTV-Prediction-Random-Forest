import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
id_array = []
date_array = []
first_touch_time = []
last_touch_time = []
user_id = ""
user_row = 0
date = ""
time = ""
hours, minutes, seconds = "", "",""
rows = []
first_opened = False
ad_opened = False

def increase(row, column):
    df.iloc[row, column] = df.iat[row, column] + 1

def set_time(row, time):
    df.iloc[row, 2] = time

with open("dataset3.txt") as dataset:
    for text in dataset:
        for word in text.split(","): #create id and first touch date arrays
            if "first_open" in word:
                first_opened = True
            if "user_first_touch_date" in word and first_opened:
                date_array.append(word.removeprefix('"user_first_touch_date":'))
            if "user_pseudo_id" in word and first_opened:
                id_array.append(word.removeprefix('"user_pseudo_id":'))
                first_opened = False

        for i in range(0, len(id_array)): #create rows multi-D array
            rows.append([id_array[i], 0, "", 0, 0, 0, 0])

        df = pd.DataFrame(rows, columns=["User IDs", "Events", "Install Time", "Ads After Day0", "First Touch Time", "Last Touch Time", "Total Time"]) #create dataframe

        for word in text.split(","):
            if "first_open" in word:
                first_opened = True
            if "event_date" in word:
                date = word.removeprefix('"event_date":')
            if ("event_time" in word) and ("rank" not in word):
                event_time = word.removeprefix('"event_time":"')
            if "INTERSTITIAL_AD_SHOWN" in word:  # check if ad is shown
                ad_opened = True
            if "user_pseudo_id" in word:
                if word.removeprefix('"user_pseudo_id":') in id_array:
                    user_row = id_array.index(word.removeprefix('"user_pseudo_id":'))
                    hours, minutes, seconds = event_time.split(":")
                    hours = int(hours)
                    if df.iat[user_row, 5]  < hours:
                        df.iloc[user_row, 5] = hours
                increase(user_row, 1) #increase events
                if (ad_opened):
                    ad_opened = False
                    if (date_array[user_row] != date):
                        increase(user_row, 3) #increase Ads After Day0
                if first_opened:
                    hours, minutes, seconds = time.split(":")
                    hours = int(hours)
                    if 6 <= hours < 12:
                        set_time(user_row, "Morning")
                    elif 12 <= hours < 18:
                        set_time(user_row, "Afternoon")
                    elif 18 <= hours < 24:
                        set_time(user_row, "Evening")
                    elif 0 <= hours < 6:
                        set_time(user_row, "Night")
                    first_opened = False
                    df.iloc[user_row, 4] = hours
            if "user_first_touch_time" in word:
                time = word.removeprefix('"user_first_touch_time":"')
        for word in text.split(","):
            if "user_pseudo_id" in word:
                if word.removeprefix('"user_pseudo_id":') in id_array:
                    user_row = id_array.index(word.removeprefix('"user_pseudo_id":'))
                    df.iloc[user_row, 6] = df.iat[user_row, 5] - df.iat[user_row, 4] + 1

        encoder = OneHotEncoder(handle_unknown='ignore', dtype=int)
        encoder_df = pd.DataFrame(encoder.fit_transform(df[["Install Time"]]).toarray())
        df = df.join(encoder_df)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        new_x = df.iloc[:, 4:9].join(df.iloc[:, 1:2])
        touch_time = df.iloc[:, 6:7]
        np.savetxt("touch_times.csv", touch_time, delimiter=",")
        print(df)
        break