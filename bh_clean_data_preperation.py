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


# df_bh_clean_survey = df_bh_clean.merge(df_survey, on='user_id', how='left')
# df_bh_clean_survey.head()

# %%
df_bh_clean = pd.read_csv('clean_files/bh_clean.csv', nrows=1000)
df_bh_clean.head()

# domains = df_bh_clean['domain']
# domains_dict = dict(pd.value_counts(domains))
# domain_values = []
# for i, j in domains_dict.items():
#     domain_values.append([i,j])
# print(domain_values)
    
# with open('bh_clean_domains.csv', 'w+', newline='') as file:
#     write = csv.writer(file)
#     write.writerows(domain_values)

df_bh_clean.head()
#pd.value_counts(df_bh_clean['domain']).plot(kind='bar', figsize= (100,100))

categorized_domains = []
with open('similarweb_categories.json', "r") as file:
    similarweb = json.load(file)
    
similarweb = list(similarweb.items())
for group in similarweb:
    try:
        for category in list(group[1].items()):
            for url in category[1]:
                            categorized_domains.append([url, category[0]])

    except:
        for url in group[1]:
            categorized_domains.append([url, group[0]])

df_cat_domains = pd.DataFrame(categorized_domains)
df_cat_domains.columns = ['domain', 'similarweb_category']
df_cat_domains.head()

df_bh_clean = df_bh_clean.merge(df_cat_domains, on='domain', how='left')
df_bh_clean.head(100)
# %%
# list(x[1][1].items())[1]
