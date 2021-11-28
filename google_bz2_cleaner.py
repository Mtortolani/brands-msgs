from file_opener import ReaderTools
from bs4 import BeautifulSoup

reader = ReaderTools()

google_bz = reader.bz2ToList('clean_files\google_ads\google_ads_html_0.json.bz2')

google_preferences = []
for observation in google_bz:
    html = observation['html']
    # print(googleData[i]['id'])
    # print(googleData[i]['html'])
    # print(googleData[i].keys())
    
    soup = BeautifulSoup(html, "html.parser")
    

    
    preference_list = []
    for preference in soup.find_all('div', {'class': 'c7O9k'}):
        preference_txt = preference.get_text()
        preference_list.append(preference_txt)
        
    # KEEP IN MIND, PREFERNCE LIST INCLUDES ADS THAT HAVE BEEN TURNED OFF, WE ARE UNSURE WHETHER THOSE ADS ARE DESIRED OR UNWANTED
    google_preferences.append([observation['id'], preference_list])
    
print(len(google_preferences))