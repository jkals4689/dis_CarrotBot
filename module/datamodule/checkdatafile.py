import nextcord

import os
import sys
import pandas as pd
from pathlib import Path
from .datalist import GetList

filenames = ('join_left','settings')

def check_datafile(guild: nextcord.Guild):
    __path = "./dadabase/{}_{}/".format(guild.id, guild.name)
    if not Path(__path).is_dir:
        os.mkdir(__path)

    for filename in filenames:
        if not (Path.cwd() / __path / filename+".csv"):
            