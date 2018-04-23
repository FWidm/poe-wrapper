import asyncio
import time
from typing import List, Dict

import copy

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
        self.snapshots[parser.character_name] = []
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
        last_snapshot = snapshot_list[-1] if len(snapshot_list)>0 else None
        print(last_snapshot)
        if last_snapshot == None or not parser == last_snapshot:
            self.snapshots[parser.character_name].append(copy.deepcopy(parser))
            print(">>", parser.character_name, len(self.snapshots[parser.character_name]))
        else:
            print(">> skipped char {}".format(parser.character_name))

    def fetch_char(self, parser: CharacterParser):
        parser.update()
        self._create_snapshot(parser)

    def get_snapshots(self):
        print(len(self.snapshots))


if __name__ == '__main__':
    pt = PlayerTracker()
    pt.add_character('FaustVIII', 'FromDeadToWorse')
    scheduler = BackgroundScheduler()
    scheduler.add_job(pt.fetch_chars, 'interval', seconds=10)
    # scheduler.add_job(pt.get_snapshots, 'interval', seconds=1)
    scheduler.start()
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()