import sys
sys.path.insert(1, 'C:/Users/mtort/Repositories/brands-msgs/')

from file_opener import ReaderTools
from bs4 import BeautifulSoup
reader = ReaderTools()


bluekai_preferences = []
bluekaiData = reader.jsonToList('clean_files/bluekai/bluekai_html_0.json')

for observation in bluekaiData:
    html = observation['html']

    
    soup = BeautifulSoup(html, "html.parser")
    
    print(soup.prettify())
    
    # preference_list = []
    # for preference in soup.find_all('div', {'class': 'c7O9k'}):
    #     preference_txt = preference.get_text()
    #     preference_list.append(preference_txt)
        
    # # KEEP IN MIND, PREFERNCE LIST INCLUDES ADS THAT HAVE BEEN TURNED OFF, WE ARE UNSURE WHETHER THOSE ADS ARE DESIRED OR UNWANTED
    # bluekai_preferences.append([observation['id'], preference_list])
    
        
        
print(len(bluekai_preferences))
    