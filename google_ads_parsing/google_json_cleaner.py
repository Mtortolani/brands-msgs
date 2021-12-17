import sys
sys.path.insert(1, 'C:/Users/mtort/Repositories/brands-msgs/')

import pandas as pd
import json
from file_opener import ReaderTools
from bs4 import BeautifulSoup

reader = ReaderTools()

googleData = reader.jsonToList('clean_files/google_ads/google_ads_html_0.json')

google_preferences = {}
for observation in googleData:
    html = observation['html']

    
    soup = BeautifulSoup(html, "html.parser")
    
    #print(soup.prettify())
    
    preference_list = []
    for preference in soup.find_all('div', {'class': 'c7O9k'}):
        preference_txt = preference.get_text()
        preference_list.append(preference_txt)
        
    # KEEP IN MIND, PREFERNCE LIST INCLUDES ADS THAT HAVE BEEN TURNED OFF, WE ARE UNSURE WHETHER THOSE ADS ARE DESIRED OR UNWANTED
    google_preferences[str(observation['id'])] = preference_list
    
        
        
print(len(google_preferences))

with open ('google_ads_preferences_MT.json', 'w') as fp:
    json.dump(google_preferences,fp)

    
    