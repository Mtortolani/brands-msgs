import pandas as pd 
import json
import csv
import bz2

class ReaderTools:
    def __init__(self):
        pass
    
    def tsv_to_csv(self, fileName, endFileName):
        csv_table=pd.read_table(fileName, sep='\t')
        csv_table.to_csv(endFileName)
        print(f'{fileName} Tsv file converted to csv')

    def jsonToList(self, filename):
        jsonList = []
        with open (filename, 'r', encoding='utf-8') as file:
            for line in file:
                jsonList.append(json.loads(line))
        return jsonList


    def bz2ToList(self, filename):
        lines = []
        with bz2.open(filename, 'rt', encoding='utf-8') as file:
            for i, line in enumerate(file):
                lines.append(json.loads(line))
        return lines

    def csvToList(self, filename):
        rowList = []
        counter=0
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                counter+=1
                if True:
                    print(row)
                    rowList.append(row)
        return rowList

    def readAndSampleCsv(self, file,  sampleFrac) -> pd.DataFrame:
        df = pd.read_csv(file)
        df = df.sample(frac=10/1000000, replace=False, random_state=1)
        return(df)


# reader = ReaderTools()
# tsv_to_csv('dirty_files\Marco Tortolani - bh-clean.tsv', 'bh_clean.csv')
# tsv_to_csv('dirty_files\Marco Tortolani - google_ads\subset.tsv', 'google_ads_subset.csv')
# tsv_to_csv('dirty_files\Marco Tortolani - bluekai\subset.tsv', 'bluekai_subset.csv')
 
# bluekai = reader.jsonToList('clean_files/bluekai/bluekai_html_0.json')
# google = reader.jsonToList('clean_files/google_ads/google_ads_html_0.json')


# print(google[4]['id'])
# print(google[4]['html'])
# print(bluekai[4]['id'])
# print(bluekai[4]['html'])

# google_bz = bz2ToList('original_files\Marco Tortolani - google_ads\google_ads_html_0.json.bz2')
# print(google_bz[0]['id'])
# textfile = open('google_ads_json_bz2.txt','w', encoding='utf-8')
# textfile.write(google_bz[1]['html'])
# textfile.close()

# df_bh_clean = pd.read_csv('df_bh_clean.csv')
# print(df_bh_clean['domain'])