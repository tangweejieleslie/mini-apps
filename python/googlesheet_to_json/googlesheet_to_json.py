import json
import requests

api_url_base = 'http://gsx2json.com/api'
google_sheet_id = '1Wc69zhOlufU4w9bfmbowhj3aTCdjCZTNhMxgIljahbQ'
# google_sheet_id = '2PACX-1vSPGH83sgdd469zJ7t2SGM75itf5X5D1e69EEZLYzrFZu9u2-N129PVxenddJVH-gMMeoCZHL7n3jyY'
api_call = api_url_base + '?id=' + google_sheet_id + '&sheet=' 

BASE_API_CALL = api_call

for i in range(60):

    api_call = BASE_API_CALL + str(i)
    print('Now processing ' ,api_call, '...')
    response = requests.get(api_call)

    JSONNAME = 'sheet_' + str(i) + '.json' 

    f = open( JSONNAME, 'w')  
    out = json.dumps(response.json())  
    f.write(out)  
    f.close()


