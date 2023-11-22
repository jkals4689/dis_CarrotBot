import json
import nextcord

from abc import ABC, abstractmethod
# from datetime import datetime
# from .gendataframe import GeneratorDataFrame
# from ErrorModule import DataInformationError
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
    dic = \
        {
            "id": member.id,
            "name": member.name,
            "role": member.roles,
            "nickname": member.nick,
            "warn": 0
        }
    return dic


class JsonWrite(ABC):
    @abstractmethod
    def check_jsonfile(self):
        pass


class CsvWrite(ABC):
    @abstractmethod
    def check_csvfile(self):
        pass


class DataWriter:
    """
    DataWriter
    def add_userdata(member) -> added userdata to userdata.json
    """

    def __init__(self, guild: nextcord.Guild):
        self.path = Path(Path.cwd() / 'database' / f'{guild.id}_{guild.name}')

    def add_userdata(self, member: nextcord.Member):
        """
        A function that stores member information in userdata.json
        :param member:
        """
        with open(self.path / json_filenames[0], 'r', encoding='utf-8') as read_file:
            data: list = json.load(read_file)

        data.append(set_user_dict(member))
        with open(str(self.path / json_filenames[0]), 'w', encoding='utf-8') as write_file:
            json.dump(data, write_file, indent=4)

    def __del__(self):
        pass
