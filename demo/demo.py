from pprint import pprint

from src.core import PoeData
from src.models.Character import Character
from src.models.item import Item

pp = PoeData(cookie='5ead577fa589214b97db8f01690fcdea')
# pprint(pp.get_leagues())
# pprint(pp.get_char_list('FaustVIII'))
char_info=pp.get_char_info('FaustVIII','FromDeadToWorse')
pprint(char_info.keys())
# for item in char_info['items']:
#     print(Item.from_dict(item).__dict__, '\n')
print(Character.from_dict(char_info['character']))
print(char_info['hashes'])
# pprint(pp.get_stash_info('FaustVIII', 'bestiary', 0))
# pprint(pp.get_mtx_info())

