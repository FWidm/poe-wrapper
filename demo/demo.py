from pprint import pprint

from src.core.parser import CharacterParser

"""
Extract data from a specific account & char, then go through each slot and preview explicits and implicit mods.
"""
char = CharacterParser("FaustVIII", "FromDeadToWorse")
print(char.account_name, char.character)
print('----')
pprint(char.get_items_dict())
print('----')
for slot in char.get_items_dict():
    items = char.get_items_dict()[slot]
    # go through each slot, print slot, name, implicit and explicit mods of the items.
    mods = [{'slot': slot, 'name': item.name if item.name else item.type,'Sockets': item.get_linked_sockets() ,'implicit': item.implicit_mods,
             'explicit': item.explicit_mods} for item in items if item.explicit_mods]

    print(mods)
    # print(slot, items, ', '.join(]))
print('----')
print(char.items[0].name, char.items[0].get_gems())
