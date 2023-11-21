from pathlib import Path, WindowsPath, PosixPath
# from module.ErrorModule import write_error_log

import json
# import nextcord
# import asyncio
import pandas as pd

__csv_filenames = ('settings.csv',)
__json_filenames = ('userdata.json',)
__userdata = ['ID', 'Name', 'Role', 'NickName', 'Warn']
__settings = [['ID', 'Name'], ['LogCh', 'TxtCh', 'WanrCh', 'Role', 'WarnRole']]


def get_dataframe_type(filename: str):
    """
    Return the dataframe by receiving the file name.
    :param filename:
    :return:
    """
    if filename == 'settings.csv':
        return pd.DataFrame(index=__settings[1],
                            columns=__settings[0])
    # elif filename == 'userdata.json':
    #     return pd.DataFrame(columns=__userdata)
    return None


def get_pathtype(path: Path, filename: str):
    """
    A function that determines what type of path is.
    :param path:
    :param filename:
    :return:
    """
    name = ""
    if isinstance(path, WindowsPath):
        name = str(path).split("\\")[-1]
    elif isinstance(path, PosixPath):
        name = str(path).split("/")[-1]
    print(f"{name} in check {filename}")


def check_files(path: Path):
    """
    A function that checks whether a csv file exists or not.
    :param path:
    :return:
    """
    for csvfile in __csv_filenames:
        if not Path(path / csvfile).is_file():
            try:
                dataframe = get_dataframe_type(csvfile)
                dataframe.to_csv(str(path / csvfile), encoding='utf-8', index=False)
            except Exception as e:
                print(e)
            else:
                get_pathtype(path, csvfile)


def check_jsonfile(path: Path):
    """
    A function that checks whether a json file exists or not.
    :param path:
    :return:
    """
    for jsonfile in __json_filenames:
        if not Path(path / jsonfile).is_file():
            with open(str(path / jsonfile), 'w', encoding='utf-8') as outfile:
                json.dump([], outfile, indent=4)


class CheckData:
    """
    Class that examines the data on the server.
    """

    def __init__(self, guild):
        self._guild = guild
        self._path = Path(Path.cwd() / "database" / f"{guild.id}_{guild.name}")
        self.check_guild_folder()
        self.check_file()

    def check_guild_folder(self):
        """
        A function that determines whether a folder that stores data on the server exists.
        :return:
        """
        self._path.mkdir(parents=True, exist_ok=True)

    def check_file(self):
        """

        :return:
        """
        check_files(self._path)
        check_jsonfile(self._path)

    # def get_path(self):
    #   return self._path

    def __del__(self):
        print("Checking folders and files success.")
