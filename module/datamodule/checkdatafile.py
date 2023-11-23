from pathlib import Path, WindowsPath, PosixPath
from module.datamodule.datawriter import DataWriter
from module.ErrorModule import write_error_log

import json
import pandas as pd

csv_filenames = ('settings.csv',)
json_filenames = ('userdata.json',)
# __userdata = ['ID', 'Name', 'Role', 'NickName', 'Warn']
__settings = [['ID', 'Name'], ['LogCh', 'TxtCh', 'WanrCh', 'Role', 'WarnRole']]


def set_dataframe_type(filename: str):
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


class CheckData:
    """
    Class that examines the data on the server.
    """
    def __init__(self, guild):
        self.path = Path(Path.cwd() / "database" / f"{guild.id}_{guild.name}")
        self.check_guild_folder()
        self.check_jsonfile()
        self.check_csvfile()

    def check_guild_folder(self):
        """
        A function that determines whether a folder that stores data on the server exists.
        :return:
        """
        self.path.mkdir(parents=True, exist_ok=True)

    def check_jsonfile(self):
        """
        A function that checks whether a json file exists or not.
        """
        for jsonfile in json_filenames:
            path = Path(self.path / jsonfile)
            if not path.is_file():
                with open(str(path), 'w', encoding='utf-8') as outfile:
                    json.dump([], outfile, indent=4)

    def check_csvfile(self):
        for csvfile in csv_filenames:
            path = Path(self.path / csvfile)
            if not Path(path / csvfile).is_file():
                try:
                    dataframe = set_dataframe_type(csvfile)
                    dataframe.to_csv(str(path), encoding='utf-8', index=True)
                except Exception as e:
                    write_error_log(e)
                # else:
                #     get_pathtype(path, csvfile)
