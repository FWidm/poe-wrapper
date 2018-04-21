from pprint import pprint

from src.core.parser import CharacterParser

char = CharacterParser("FaustVIII", "FromDeadToWorse")
print(char.account_name,char.character)
print('----')
pprint(char.get_items_dict())


