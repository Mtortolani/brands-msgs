import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_bh_clean = pd.read_csv('df_bh_clean.csv')
print(df_bh_clean['domain'])

# sns.set_style("whitegrid")
# ax = sns.histplot(data=df_bh_clean, x='domain')
# #ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=90)
# plt.show()