import json
import requests

sheet_names = ["", "Contents","HeroRatesSummary","ShardsDropRates","SkinFusion","SummonCircleRates","ProphetTreeSummon","ProphetTreeReplacement","BraveTrialStages","BraveTrialChest","WishingFountain","LuckyStore","HeroExp","Monsters","PlayerExp","Vip","HeroSlotsCost","TavernQuests","TavernQuestRerolls","CIIslands","CIDrop","CIBuildings","SealLand","AspenWaves","AspenRewards","ArenaFightRewards","RankingRewards","ScoutAndMarauderRates","ScoutRewards","CampaignStages","CampaignLootStages","CampaignLootItems","CampaignEventLoot","EventRaid","TowerofOblivion","BrokenSpaces","BrokenSpacesOld","GuildRaid","GuildPrayforFire","GuildMill&Exp","GuildTech","GuildStore","Marketplace","SealLandStore","ArenaStore","AltarStore","LootEventStore","GloriousRelicStore","Achievments","MonthlyLoginRewards","NoobOnlineRewards","Enemies","Heroes","Skills"]
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


