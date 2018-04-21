from pprint import pprint

from src.core import PoeData
from src.models.character import Character
from src.models.item import Item

pp = PoeData(cookie='5ead577fa589214b97db8f01690fcdea')
# pprint(pp.get_leagues())
# pprint(pp.get_char_list('FaustVIII'))
# char_info=pp.get_char_info('FaustVIII','FromDeadToWorse')
# pprint(char_info.keys())
# for item in char_info['items']:
#     print(Item.from_dict(item).__dict__, '\n')
# print(Character.from_dict(char_info['character']))
# print(char_info['hashes'])
# pprint(pp.get_stash_info('FaustVIII', 'bestiary', 0))
# pprint(pp.get_mtx_info())

# League data
trade_leagues = pp.get_trade_leagues()
print(trade_leagues,type(trade_leagues))
first_league = pp.get_league_info(trade_leagues['result'][0]['id'],ladder=True,ladder_track=True,ladder_limit=1,ladder_offset=0)
print(first_league)
