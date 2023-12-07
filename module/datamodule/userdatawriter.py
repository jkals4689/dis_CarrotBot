import json
import nextcord

from abc import ABC, abstractmethod
from pathlib import Path

json_filenames = ('userdata.json',)


def set_dataframe():
    """
    Returns the Pandas dataframe variable.
    :return:
    """
    pass


def set_user_dict(member: nextcord.Member):
    """
    Returns the dictionary variable.
    :param member:
    :return:
    """
    role = [{"id": role.id, "name": role.name} for role in member.roles]
    dic = \
        {
            "id": member.id,
            "name": member.name,
            "role": role,
            "nickname": member.nick,
            "warn": 0
        }
    return dic


class DataWriter(ABC):
    @abstractmethod
    def add_userdata(self):
        pass

    @abstractmethod
    def remove_userdata(self):
        pass


class GuildDataWriter(DataWriter):
    """
    DataWriter
    def add_userdata(member) -> added userdata to userdata.json
    """

    def __init__(self, guild: nextcord.Guild):
        self.path = Path(Path.cwd() / 'database' / f'{guild.id}_{guild.name}')
        self.__member = guild.members
        try:
            with open(str(self.path / json_filenames[0]), 'r', encoding='utf-8') as read_file:
                self.data: list = json.load(read_file)
        except Exception as e:
            print(e)
            self.data = []

    def add_userdata(self):
        for member in self.__member:
            self.data.append(set_user_dict(member))

    def remove_userdata(self):
        pass

    def __del__(self):
        with open(str(self.path / json_filenames[0]), 'w', encoding='utf-8') as write_file:
            json.dump(self.data, write_file, indent=4)
