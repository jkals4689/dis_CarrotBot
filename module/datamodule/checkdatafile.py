import nextcord

import os
import pandas as pd
from pathlib import Path
from .datalist import GetList
from ErrorModule import write_error_log

filenames = ('settings', 'userdata')


def check_datafile(guild: nextcord.Guild):
    __path = "{}/dadabase/{}_{}/".format(Path.cwd(), guild.id, guild.name)
    Path(__path).mkdir(parents=True, exist_ok=True)

    for filename in filenames:
        if not (Path.cwd() / __path / filename+".csv"):
            dataframe = pd.DataFrame(columns=GetList(filename).get_datatype())
            try:
                dataframe.to_csv(__path+filename+'.csv')
            except Exception as e:
                write_error_log(e)
            else:
                print(f"{guild.id}_{guild.name}."+filename+".csv is not found")

        else:
            print(f"{guild.id}_{guild.name}."+filename+".csv is exists")


def dataframe_type(filename: str):
    if filename == filenames[0]:
        return pd.DataFrame(columns=GetList(filename).get_datatype())
