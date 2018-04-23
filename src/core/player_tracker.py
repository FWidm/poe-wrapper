import asyncio
from typing import List, Dict

import copy

import logging

import math

import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from src.core.parser import CharacterParser


class PlayerTracker():
    def __init__(self):
        self.char_parsers: List[CharacterParser] = []
        self.snapshots = {}

    def add_character(self, account: str, character: str):
        parser = CharacterParser(account, character)
        self.char_parsers.append(parser)
        self._create_snapshot(parser)
        print(self.char_parsers)

    def remove_character(self, account: str, character: str):
        parser = next(filter(lambda parser: parser.account_name == account and parser.character_name == character,
                             self.char_parsers))
        self.char_parsers.remove(parser)

    def fetch_chars(self):
        for parser in self.char_parsers:
            self.fetch_char(parser)

    def _create_snapshot(self, parser):
        snapshot_list = self.snapshots.get(parser.character_name)
        if not snapshot_list:
            self.snapshots[parser.character_name] = []
        self.snapshots[parser.character_name].append(copy.deepcopy(parser))

    def fetch_char(self, parser: CharacterParser):
        parser.update()
        self._create_snapshot(parser)

    def get_snapshots(self):
        print(len(self.snapshots))


if __name__ == '__main__':
    pt = PlayerTracker()
    pt.add_character('FaustVIII', 'FromDeadToWorse')
    scheduler = BlockingScheduler()
    scheduler.add_job(pt.fetch_chars, 'interval', seconds=10)
    scheduler.add_job(pt.get_snapshots, 'interval', seconds=5)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
