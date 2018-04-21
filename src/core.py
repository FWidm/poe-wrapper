from pprint import pprint

import requests

CHAR_WINDOW = 'https://pathofexile.com/character-window/'
BASE_URL = 'https://pathofexile.com'

class PoeData:
    """
    Small Wrapper to retrieve specific info from the given API.
    - Big thanks to: https://app.swaggerhub.com/apis/Chuanhsing/poe/1.0.0#/
    """
    def __init__(self, cookie=None):
        if cookie:
            self._cookies = {
                'POESESSID': cookie
            }
        else:
            self._cookies = {}

    def get_race_seasons(self):
        url_race_seasons='/api/seasons'
        return requests.get(BASE_URL + url_race_seasons, cookies=self._cookies).json()

    def get_leagues(self,type='main',compact=1,limit=10,offset=0):
        url_leagues='/api/leagues'
        payload = {
            'type': type,
            'compat': compact,
            'limit': limit,
            'offset': offset
        }
        return requests.get(BASE_URL + url_leagues, params=payload, cookies=self._cookies).json()


    def get_mtx_info(self, league=None, sortOrder='asc', tabs=0):
        url_stash = 'get-mtx-stash-items'
        payload = {
            'league': league,
            'sortOrder': sortOrder,
            'tabs': tabs,
        }
        return requests.post(CHAR_WINDOW + url_stash, data=payload, cookies=self._cookies).json()

    def get_stash_info(self, accountName, league, tabIndex, show_tab_info=False):
        """
        Get information from the tab. requires the cookies to be set.
        :param accountName: Name of the account
        :param league: string with the league name. E.g. 'bestiary'
        :param tabIndex:
        :param show_tab_info:
        :return:
        """
        url_stash = 'get-stash-items'
        payload = {
            'accountName': accountName,
            'league': league,
            'tabIndex': tabIndex,
            'tabs': int(show_tab_info),
        }
        return requests.post(CHAR_WINDOW + url_stash, data=payload, cookies=self._cookies).json()

    def get_char_info(self, accountName, charName):
        """
        Get character information from the site, contains skills and item raw data.
        :param accountName:
        :param charName:
        :return: dict with jewel_slots, character, items, hashes
        """
        url_skills = 'get-passive-skills'
        url_items = 'get-items'
        payload = {'accountName': accountName, 'character': charName}
        skills = requests.post(CHAR_WINDOW + url_skills, data=payload, cookies=self._cookies).json()
        items = requests.post(CHAR_WINDOW + url_items, data=payload, cookies=self._cookies).json()
        skills.update(items)
        return skills

    def get_char_list(self, accountName):
        """
        Get a list of characters, requires the cookie to be set.
        :param accountName:
        :return: json response with the character list
        """
        url_chars = "get-characters"
        payload = {'accountName': accountName}
        return requests.post(CHAR_WINDOW + url_chars, data=payload, cookies=self._cookies).json()