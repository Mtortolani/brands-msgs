import pandas as pd 
tsv_file='Marco Tortolani - google_ads/subset.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('google_ads subset.csv',index=False)

#print(to_csv'Marco Tortolani - google_ads\google_ads_html_0.json')