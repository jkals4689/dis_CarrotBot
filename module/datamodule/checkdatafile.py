import nextcord

import os
import pandas as pd
from pathlib import Path
from .datalist import GetList
from ErrorModule import write_error_log

filenames = ('join_left', 'settings')


def check_datafile(guild: nextcord.Guild):
    __path = "./dadabase/{}_{}/".format(guild.id, guild.name)
    if not Path(__path).is_dir:
        os.mkdir(__path)

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


