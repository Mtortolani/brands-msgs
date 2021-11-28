import pandas as pd
import numpy as np
from numpy import reshape
from bluekai_parsing.bluekai_data_preperation import BluekaiData
from sklearn.linear_model import LinearRegression

Storage = BluekaiData()
Storage.pullBluekaiCategories()
Storage.switchUserIds()


x = []
y = []
partyOutput= []
df_survey = pd.read_csv('clean_files\survey.csv')
survey_psid = list(df_survey['psid'])
survey_party = list(df_survey['party7_str'])
for user_id in Storage.bluekai_user_ids:
    try:
        index = survey_psid.index(user_id)
    except ValueError:
        print(f'Key {user_id} dropped')
        continue
    user_id_index = Storage.bluekai_user_ids.index(user_id)
    x.append(Storage.bluekai_categories[user_id_index])
    y.append(survey_party[index])

x_dummy = pd.get_dummies(data=x)
reg = LinearRegression()
reg.fit(x_dummy, y)
