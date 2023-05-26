from typing import Union

import requests as re
import re as regex
from collections import defaultdict
import time
import pandas as pd
from tqdm import tqdm
import datetime


def write_data(data: Union[pd.DataFrame, list], filename: str):
    if type(data) == list:
        data = pd.Series(data, name='values')
    data.to_csv(filename)


def read_data(filename: str, col=None) -> Union[pd.DataFrame, list]:
    data = pd.read_csv(filename, encoding='utf-8')
    if col:
        return list(data[col])
    return data


def get_hashtags(rows: list[str]) -> dict:
    hashtags = defaultdict(int)
    for row in rows:
        try:
            for hashtag in regex.findall('(?<=\\s#)[a-zA-Zа-яА-я]\\w*', row):
                hashtags[hashtag] += 1
        except TypeError:
            pass
    return hashtags


class Miner:
    def __init__(self, token, version='5.131'):
        self.token = token
        self.version = version

    def __get_members_query(self, group_id, offset=0, count=1000, sort='id_asc'):
        return f"https://api.vk.com/method/groups.getMembers?access_token={self.token}&group_id={group_id}&sort={sort}&offset={offset}&count={count}&v={self.version}"

    def __get_posts_query(self, group_id, offset=0, count=100):
        return f"https://api.vk.com/method/wall.get?access_token={self.token}&domain={group_id}&offset={offset}&count={count}&v={self.version}"

    def __get_friends_query(self, user_id):
        return f"https://api.vk.com/method/friends.get?access_token={self.token}&user_id={user_id}&v={self.version}"

    def get_members(self, community: str, save_to=None) -> list:
        """
        Collects list of community's members' ids.
        """
        print("Collecting members from", community)
        r = re.post(self.__get_members_query(community)).json()
        members_count = r['response']['count']
        print(f"Found {members_count} members")
        result = r['response']['items']
        for offset in tqdm(range(1000, members_count + 1000, 1000)):
            r = re.post(self.__get_members_query(community, offset=offset)).json()
            result += r['response']['items']
            time.sleep(0.3)
        if save_to:
            write_data(result, save_to)
            print(f"Data saved to {save_to}")
        return result

    def get_posts(self, community: str, count=2000, save_to=None) -> pd.DataFrame:
        """
        Collects texts of community's posts.
        """
        print("Collecting posts from", community)
        r = re.post(self.__get_posts_query(community)).json()
        posts_iter = range(0, min(count, r['response']['count']), 100)
        result = []
        for offset in tqdm(posts_iter):
            for r in re.post(self.__get_posts_query(community, offset=offset)).json()['response']['items']:
                row = {
                    'text': r['text'],
                    'date': r['date'],
                    'hour': datetime.datetime.fromtimestamp(r['date']).hour
                }
                result.append(row)
        result = pd.DataFrame(result)
        if save_to:
            write_data(result, save_to)
            print(f"Data saved to {save_to}")
        return result

    def get_members_connections_and_save(self, members: set, filename: str) -> pd.DataFrame:
        edges = []
        for member in tqdm(members):
            try:
                friends = set(re.post(self.__get_friends_query(member)).json()['response']['items']) & members
                for friend in friends:
                    edges.append({'member': member, 'friend': friend})
            except KeyError:
                pass
            time.sleep(0.2)
        df = pd.DataFrame(edges)
        df.to_csv(filename)
        return df


