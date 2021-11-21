import pandas as pd 
import json
import csv
import bz2


def tsv_to_csv(fileName, endFileName):
    csv_table=pd.read_table(fileName, sep='\t')
    csv_table.to_csv(endFileName)
    print(f'{fileName} Tsv file converted to csv')
#tsv_to_csv('dirty_files\Marco Tortolani - bh-clean.tsv', 'bh_clean.csv')
# tsv_to_csv('dirty_files\Marco Tortolani - google_ads\subset.tsv', 'google_ads_subset.csv')
# tsv_to_csv('dirty_files\Marco Tortolani - bluekai\subset.tsv', 'bluekai_subset.csv')



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

# google = jsonToList('clean_files/bluekai/bluekai_html_0.json')
# bluekai = jsonToList('clean_files/google_ads/google_ads_html_0.json')


# print(google[4]['id'])
# print(google[4]['html'])


# google_bz = bz2ToList('original_files\Marco Tortolani - google_ads\google_ads_html_0.json.bz2')
# print(google_bz[0]['id'])
# textfile = open('google_ads_json_bz2.txt','w', encoding='utf-8')
# textfile.write(google_bz[1]['html'])
# textfile.close()

def readCsv(filename):
    rowList = []
    counter=0
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            counter+=1
            if counter % 100000==0:
                print(row)
                rowList.append(row)
            else:
                next(reader)
            print(counter)
    return rowList

def listToCSV(L, csvName):
    with open(L, 'w', newline='') as file:
     wr = csv.writer(file, quoting=csv.QUOTE_ALL)
     wr.writerow(L)

dfGoogle = pd.read_csv('clean_files/bh_clean.csv')
dfGoogle.head()