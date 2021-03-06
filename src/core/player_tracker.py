import asyncio
from typing import List, Dict

import copy

import logging

from src.core.parser import CharacterParser
from src.util.scheduler import Scheduler


class PlayerTracker():
    def __init__(self):
        self.char_parsers: List[CharacterParser] = []
        # loop = asyncio.new_event_loop()
        # loop.set_debug(True)
        # logging.basicConfig(level=logging.DEBUG)
        # self.scheduler = Scheduler(loop=loop)
        # self.scheduler.schedule(self.fetch_chars())
        # self.loop.run_forever()
        self.snapshots = {}

    def add_character(self, account: str, character: str):
        self.char_parsers.append(CharacterParser(account, character))
        print(self.char_parsers)

    def remove_character(self, account: str, character: str):
        parser = next(filter(lambda parser: parser.account_name == account and parser.character_name == character,
                             self.char_parsers))
        self.char_parsers.remove(parser)

    def fetch_chars(self):
        for parser in self.char_parsers:
            self.fetch_char(parser)

    def fetch_char(self, parser: CharacterParser):
        parser.update()
        snapshot_list = self.snapshots.get(parser.character_name)
        if not snapshot_list:
            self.snapshots[parser.character_name] = []
        self.snapshots[parser.character_name].append(copy.deepcopy(parser))


pt = PlayerTracker()
pt.add_character('FaustVIII', 'FromDeadToWorse')
pt.fetch_chars()
pt.fetch_chars()
pt.fetch_chars()
print(pt.snapshots)
pt.remove_character('FaustVIII', 'FromDeadToWorse')
