import sys

from cassiopeia import riotapi

riotapi.set_api_key(sys.environ["DEV_KEY"])
riotapi.set_region("NA")
riotapi.print_calls(True)

champion_id = 35
mastery_id = 4352
match_id = 1505030444
rune_id = 5234
summoner_id = 22508641
summoner_name = "FatalElement"
summoner_spell_id = 7
team_id = "TEAM-49fc9f10-1290-11e3-80a6-782bcb4d0bb2"
item_id = 3031

def test_result(result):
    print(result)