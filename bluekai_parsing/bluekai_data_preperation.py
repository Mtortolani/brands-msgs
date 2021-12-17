import sys
sys.path.insert(1, 'C:/Users/mtort/Repositories/brands-msgs/')

import pandas as pd
import json


from file_opener import ReaderTools


# This combines bh clean and survey
# allows you to link specific url visits to political data
# %%


class BluekaiData():
    
    def __init__(self):
        self.bluekai_ids = []
        self.bluekai_categories = []
        self.bluekai_user_ids = []
        self.Reader = ReaderTools()

    def pullBluekaiCategories(self):
        # create nested list of [[id, names of websites visited], [repeat]] from bluekai_json_data
        bluekai_data = self.Reader.jsonToList('clean_files//bluekai//bluekai_html_0.json')

        for observation in bluekai_data:
            id = observation['id']
            html = json.loads(observation['html'])
            if 'status' in html:
                continue
            categories = html['categories']
            try:
                category_list = [trace['name:'] for trace in categories]
            except KeyError:
                try:
                    category_list = [trace['name'] for trace in categories]
                except KeyError:
                    continue
            if category_list == []:
                continue
            self.bluekai_ids.append(id)
            self.bluekai_categories.append(category_list)
            
        # print(len(self.bluekai_ids))
        # print(len(self.bluekai_categories))
    def createCagtegoriesJson(self):
        bluekai_preferences = {}
        id_cat_list = zip(self.bluekai_ids, self.bluekai_categories)
        for pair in id_cat_list:
            bluekai_preferences[str(pair[0])] = pair[1]
            
        with open ('bluekai_preferences_MT.json', 'w') as fp:
            json.dump(bluekai_preferences,fp)
            
    def switchUserIds(self):
        #converts id to user_id for bluekai data
        # result
        #bluekai_user_id = [user_ids]
        bluekai_subset = pd.read_csv('clean_files//bluekai//bluekai_subset.csv')
        subset_ids = [list(bluekai_subset['id']), list(bluekai_subset['user_id'])]
        for id in self.bluekai_ids:
            index = subset_ids[0].index(id)
            self.bluekai_user_ids.append(subset_ids[1][index])
        # print(self.bluekai_user_ids)
        # print(len(self.bluekai_user_ids))
    
    def aquirePoliticalAlignment(self):
        # df_survey = pd.read_csv('clean_files\survey.csv')
        # survey_psid = list(df_survey['psid'])
        # survey_party = list(df_survey['party7_str'])
        # df_survey.head()
        pass
    
def main():
    BD = BluekaiData()
    BD.pullBluekaiCategories()
    BD.createCagtegoriesJson()



if __name__=='__main__':
    main()
    
# blukai_subset
# id: 637456DOCS
# user_id: ah3y-adh2-akfhaweif -> survey

# bluekai_json
# id: 637456
# categories: 
#         path: bluekai tracking > age groups > age 30-34
#         name: age 30-34