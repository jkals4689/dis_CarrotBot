import nextcord
import json
import asyncio
import pandas as pd
from pathlib import Path, WindowsPath, PosixPath
from module.ErrorModule import write_error_log

__csv_filenames = ('settings.csv',)
__json_filenames = ('userdata.json',)
__userdata = ('ID', 'Name', 'Role', 'NickName', 'Warn')
__settings = (('ID', 'Name'), ('LogCh', 'TxtCh', 'WanrCh', 'Role', 'WarnRole'))


def get_dataframe_type(filename: str):
    if filename == 'settings.csv':
        return pd.DataFrame(index=__settings[1], columns=__settings[0])
    elif filename == 'userdata.json':
        return pd.DataFrame(columns=__userdata)


def get_pathType(filename):
    path = CheckData().get_path()
    if type(path) == WindowsPath:
        name = str(path).split("\\")[-1]
    elif type(path) == PosixPath:
        name = str(path).split("/")[-1]
    print("{} in check {}".format(name, filename))


def check_csvfiles(path: Path):
    for csvfile in __csv_filenames:
        if not Path(path/csvfile).is_file():
            try:
                dataframe = get_dataframe_type(csvfile)
                dataframe.to_csv(str(path/csvfile), encoding='utf-8', index=False)
            except Exception as e:
                write_error_log(e)
            else:
                get_pathType(csvfile)


def check_jsonfile(path: Path):
    for jsonfile in __json_filenames:
        if not Path(path/jsonfile).is_file():
            with open(str(path/jsonfile), 'w', encoding='utf-8') as outfile:
                json.dump([], outfile, indent=4)


class CheckData:
    def __init__(self, guild):
        self._guild = guild
        self._path = Path(Path.cwd()/"database" /
                          "{}_{}".format(guild.id, guild.name))
        self.check_guildfolder()
        self.check_file()

    def check_guildfolder(self):
        self._path.mkdir(parents=True, exist_ok=True)

    def check_file(self):
        check_csvfiles(self._path)
        check_jsonfile(self._path)

    # def get_path(self):
    #   return self._path

    def __del__(self):
        print("Checking folders and files success.")
