import nextcord
import os
import pandas as pd
from pathlib import Path
from module.ErrorModule import write_error_log

__csv_filenames = ('settings', 'userdata')
__userdata = ('ID', 'Name', 'Role', 'NickName', 'Warn')
__settings = (('ID', 'Name'), ('LogCh', 'TxtCh', 'WanrCh', 'Role', 'WarnRole'))


def check_datafile(guild: nextcord.Guild):
    __path = "./dadabase/{}_{}/".format(guild.id, guild.name)
    print(__path)
    Path(__path).mkdir(parents=True, exist_ok=True)
    check_csv(__path, guild)


def get_dataframe_type(filename: str):
    if filename == 'settings':
        return pd.DataFrame(index=__userdata[0], columns=__userdata[1])
    elif filename == 'userdata':
        return pd.DataFrame(columns=__settings)


def check_csv(path, guild, filenames: str = __csv_filenames):
    for filename in filenames:
        if not (Path.cwd() / path / filename+'.csv'):
            dataframe = get_dataframe_type(filename)
            try:
                dataframe.to_csv(path+filename+'.csv')
                print(f"{guild.id}_{guild.name}."+filename+".csv is not found")
            except Exception as e:
                write_error_log(e)
        else:
            print(f"{guild.id}_{guild.name}."+filename+".csv is exists")
