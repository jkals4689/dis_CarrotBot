import json
import os
import shutil

import nextcord

from abc import ABC, abstractmethod
from pathlib import Path

json_filenames = ('userdata.json',)


def set_user_role_dict(member: nextcord.Member):
    role = [{"id": role.id, "name": role.name} for role in member.roles]
    return role


def set_user_dict(member: nextcord.Member):
    dic = \
        {
            "id": member.id,
            "name": member.name,
            "nickname": member.nick,
            "warn": 0
        }
    return dic


class GuildInUsersDataWriter:
    def __init__(self, guild: nextcord.Guild):
        self.__member = guild.members
        self.path = Path(Path.cwd() / 'database' / f'{guild.id}_{guild.name}')

        for member in self.__member:
            Path(self.path / 'userdatas' / f"{member.id}_{member.name}").mkdir(parents=True, exist_ok=True)

    def add_userdata(self, member: nextcord.Member):
        user_file_name = str(member.id) + "_data.json"
        user_role_file_name = str(member.id) + "_role.json"

        path = Path(self.path / 'userdatas' / f"{member.id}_{member.name}" / user_file_name)
        if not Path(path).is_file():
            with open(str(path), 'w', encoding='utf-8') as write_file:
                json.dump(set_user_dict(member), write_file, ensure_ascii=False, indent=4)

        path = Path(self.path / 'userdatas' / f"{member.id}_{member.name}" / user_role_file_name)
        if not Path(path).is_file():
            with open(str(path), 'w', encoding='utf-8') as write_file:
                json.dump(set_user_role_dict(member), write_file, ensure_ascii=False, indent=4)

    def del_userdata(self, member: nextcord.Member):
        path = Path(self.path / 'userdatas' / f"{member.id}_{member.name}")
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)

    def __del__(self):
        pass
