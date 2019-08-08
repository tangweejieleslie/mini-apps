import json
import requests

sheet_names = ["", "Contents","Hero Rates Summary","Shards Drop Rates","Skin Fusion","Summon Circle Rates","Prophet Tree Summon","Prophet Tree Replacement","Brave Trial Stages","Brave Trial Chest","Wishing Fountain","Lucky Store","Hero Exp","Monsters","Player Exp","Vip","Hero Slots Cost","Tavern Quests","Tavern Quest Rerolls","CI Islands","CI Drop","CI Buildings","Seal Land","Aspen Waves","Aspen Rewards","Arena Fight Rewards","Ranking Rewards","Scout_Marauder Rates","Scout Rewards","Campaign Stages","Campaign Loot Stages","Campaign Loot Items","Campaign Event Loot","Event Raid","Tower of Oblivion","Broken Spaces","Broken Spaces Old","Guild Raid","Guild Pray for Fire","Guild Mill & Exp","Guild Tech","Guild Store","Marketplace","Seal Land Store","Arena Store","Altar Store","Loot Event Store","Glorious Relic Store","Achievments","Monthly Login Rewards","Noob Online Rewards","Enemies","Heroes","Skills"]

# print(sheet_names)

api_url_base = 'http://gsx2json.com/api'
google_sheet_id = '1Wc69zhOlufU4w9bfmbowhj3aTCdjCZTNhMxgIljahbQ'
# google_sheet_id = '2PACX-1vSPGH83sgdd469zJ7t2SGM75itf5X5D1e69EEZLYzrFZu9u2-N129PVxenddJVH-gMMeoCZHL7n3jyY'
api_call = api_url_base + '?id=' + google_sheet_id + '&sheet=' 

BASE_API_CALL = api_call

for i in range(1,60):

    api_call = BASE_API_CALL + str(i)
    print('Now processing ' ,api_call, '...')
    response = requests.get(api_call)

    JSONNAME = sheet_names[i] + '.json' 

    f = open( JSONNAME, 'w')  
    out = json.dumps(response.json())  
    f.write(out)  
    f.close()
    print(JSONNAME, ' is created!')


