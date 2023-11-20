import nextcord
import os
import pandas as pd
from pathlib import Path, WindowsPath, PosixPath
from module.ErrorModule import write_error_log

__csv_filenames = ('settings', 'userdata')
__userdata = ('ID', 'Name', 'Role', 'NickName', 'Warn')
__settings = (('ID', 'Name'), ('LogCh', 'TxtCh', 'WanrCh', 'Role', 'WarnRole'))


class CheckData:
    def __init__(self, guild):
        self._path = Path(Path.cwd()/"database" /
                          "{}_{}".format(guild.id, guild.name))

    def check_guildfolder(self):
        self._path.mkdir(parents=True, exist_ok=True)
        print("Success check guild folder.")

    def check_file(self):
        for filename in __csv_filenames:
            if not Path(self._path/str(filename+".csv")):
                try:
                    datafrmae = get_dataframe_type(filename)
                    datafrmae.to_csv(self._path+filename+".csv")
                except Exception as e:
                    write_error_log(e)
                else:
                    if type(self._path) == WindowsPath:
                        name = str(self._path).split("\\")[-1]
                    elif type(self._path) == PosixPath:
                        name = str(self._path).split("/")[-1]
                    print("{} in check {}.csv".format(name, filename))

    def __del__(self):
        pass


def get_dataframe_type(filename: str):
    if filename == 'settings':
        return pd.DataFrame(index=__userdata[1], columns=__userdata[0])
    elif filename == 'userdata':
        return pd.DataFrame(columns=__settings)
