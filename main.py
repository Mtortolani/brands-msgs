import pandas as pd 
import json
import csv
import bz2


def tsv_to_csv(tsv_file, endFileName):
    csv_table=pd.read_table(tsv_file,sep='\t')
    csv_table.to_csv('please delete',index=False)
    print(f'{tsv_file} Tsv file converted to csv')
# tsv_to_csv('Marco Tortolani - bh-clean.tsv')
# print(to_csv'Marco Tortolani - google_ads\google_ads_html_0.json')


def jsonToList(filename, ):
    jsonList = []
    with open (filename, 'r', encoding='utf-8') as file:
        for line in file:
            jsonList.append(json.loads(line))
    return jsonList


def bz2ToList(filename):
    lines = []
    with bz2.open(filename, 'rt', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i == 10:
                break
            lines.append(json.loads(line))
    return lines

google = jsonToList('original_files\Marco Tortolani - google_ads\google_ads_html_0.json')
#bluekai = jsonToList('Marco Tortolani - bluekai/bluekai_html_0.json')


print(google[1]['id'])
#print(bluekai[7]['id'])


# google_bz = bz2ToList('original_files\Marco Tortolani - google_ads\google_ads_html_0.json.bz2')
# print(google_bz[0]['id'])
# textfile = open('google_ads_json_bz2.txt','w', encoding='utf-8')
# textfile.write(google_bz[1]['html'])
# textfile.close()

def readCsv(filename):
    counter=0
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            counter+=1
            if counter <10:
                print(row)


readCsv('clean_csv_files/bh-clean.csv')