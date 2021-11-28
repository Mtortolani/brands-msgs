import pandas as pd
import json
from file_opener import ReaderTools

# This combines bh clean and survey
# allows you to link specific url visits to political data
# %%

df_survey = pd.read_csv('clean_files\survey.csv')
df_survey = df_survey.rename(columns={"psid": "user_id"})
df_survey.head()

# %%
df_bh_clean = pd.read_csv('df_bh_clean.csv')
df_bh_clean.head()
# %%
df_bh_clean_survey = df_bh_clean.merge(df_survey, on='user_id', how='left')
df_bh_clean_survey.head()


