# POE Wrapper
A small library that handles Getting various data from the POE Profile page or API.

## Features 

- Get league info
- Get character's equipment & gear
- Get stash information
- Encode and decode tree data <> url payload

## Usage
(see [demo](demo/demo.py))

```python
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

```

```
FaustVIII {'name': 'FromDeadToWorse', 'league': 'SSF Bestiary', 'classId': 3, 'ascendancyClass': 3, 'class': 'Necromancer', 'level': 92, 'experience': 2268730372, 'lastActive': True}
----
{'Amulet': [Wrath Locket],
 'Belt': [Bramble Harness],
 'BodyArmour': [Vis Mortis],
 'Boots': [Bones of Ullr],
 'Flask': [Chemist's Silver Flask of Adrenaline,
           Chemist's Stibnite Flask of Warding,
           Seething Divine Life Flask of Curing,
           Panicked Divine Mana Flask of Staunching,
           Seething Eternal Life Flask of Heat],
 'Gloves': [Southbound],
 'Helm': [Behemoth Glance],
 'Offhand': [Ahn's Heritage],
 'Offhand2': [Bitterdream],
 'Ring': [Pandemonium Knuckle],
 'Ring2': [Phoenix Loop],
 'Weapon': [Brightbeak],
 'Weapon2': [Tomahawk]}
 ----
[{'slot': 'BodyArmour', 'name': 'Vis Mortis', 'Sockets': {0: ['R', 'G', 'B'], 1: ['B', 'B', 'B']}, 'implicit': None, 'explicit': ['208% increased Energy Shield', '+29 to maximum Mana', 'Minions have 20% reduced maximum Life', 'Minions deal 15% increased Damage', '+1 to maximum number of Spectres', 'Minions gain Unholy Might for 10 seconds on Kill']}]
[{'slot': 'Flask', 'name': "Chemist's Silver Flask of Adrenaline", 'Sockets': {}, 'implicit': None, 'explicit': ['20% reduced Charges used', '23% increased Movement Speed during Flask effect']}, {'slot': 'Flask', 'name': "Chemist's Stibnite Flask of Warding", 'Sockets': {}, 'implicit': ['Creates a Smoke Cloud on Use'], 'explicit': ['21% reduced Charges used', 'Immune to Curses during Flask effect\nRemoves Curses on use']}, {'slot': 'Flask', 'name': 'Seething Divine Life Flask of Curing', 'Sockets': {}, 'implicit': None, 'explicit': ['66% reduced Amount Recovered', 'Instant Recovery', 'Immune to Poison during Flask Effect\nRemoves Poison on use']}, {'slot': 'Flask', 'name': 'Panicked Divine Mana Flask of Staunching', 'Sockets': {}, 'implicit': None, 'explicit': ['25% reduced Amount Recovered', 'Instant Recovery when on Low Life', 'Immunity to Bleeding during Flask effect\nRemoves Bleeding on use']}, {'slot': 'Flask', 'name': 'Seething Eternal Life Flask of Heat', 'Sockets': {}, 'implicit': None, 'explicit': ['66% reduced Amount Recovered', 'Instant Recovery', 'Immunity to Freeze and Chill during Flask effect\nRemoves Freeze and Chill on use']}]
...
----
Vis Mortis [Empower Support, Desecrate, Purity of Elements, Flammability, Enlighten Support, Minion Damage Support]
```