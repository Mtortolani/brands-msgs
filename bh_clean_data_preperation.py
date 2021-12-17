import sys
sys.path.insert(1, 'C:/Users/mtort/Repositories/brands-msgs/')
import pandas as pd
import json
import csv
from file_opener import ReaderTools

# This combines bh clean and survey
# allows you to link specific url visits to political data
# %%

# df_survey = pd.read_csv('clean_files\survey.csv')
# df_survey = df_survey.rename(columns={"psid": "user_id"})
# df_survey.head()

# %%
df_bh_clean = pd.read_csv('clean_files/bh_clean.csv', nrows=100000)
domains = df_bh_clean['domain']
domains_dict = dict(pd.value_counts(domains))
domain_values = []
for i, j in domains_dict.items():
    domain_values.append([i,j])
print(domain_values)
    
with open('bh_clean_domains.csv', 'w+', newline='') as file:
    write = csv.writer(file)
    write.writerows(domain_values)

print(df_bh_clean['domain'].value_counts())
pd.value_counts(df_bh_clean['domain']).plot(kind='bar', figsize= (100,100))

# %%
# df_bh_clean_survey = df_bh_clean.merge(df_survey, on='user_id', how='left')
# df_bh_clean_survey.head()








# Getting categories from google ad data
# file = open('condensed_ad_preferences\google_ads_bz2_preferences_MT.json')
# google_ads_preferences = json.load(file)

# preferences_unique = []

# for preferences in google_ads_preferences.values():
#     print(len(set(preferences)))
#     for x in set(preferences):
#         preferences_unique.append(x)

# file.close()



# preferences_unique = list(set(preferences_unique))
# print(len(preferences_unique))
# print(preferences_unique)
