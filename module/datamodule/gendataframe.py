import os
import sys
import pandas as pd
from pathlib import Path
from ErrorModule import write_error_log
from .datalist import GetList


class GeneratorDataFrame:
    def __init__(self, guild, event: str = ""):
        self.__path = "database/{}_{}/".format(guild.id, guild.name)
        if event != "":
            self.__filename = event
            self.__type = GetList(event).get_datatype()
            self._dataframe = self.read_dataframe()

    def get_path(self):
        return self.__path+self.__filename+".csv"

    def __error_save_dataframe(self):
        if not Path(self.__path).is_dir():
            os.mkdir(self.__path)
        try:
            self._dataframe.to_csv(
                self.get_path(), encoding='utf-8', index=False)
            print("success save data")
        except AttributeError:
            print("Data is not defined.")
            self._dataframe = pd.DataFrame(columns=self.__type)
            self.__error_savedataframe()
        except Exception as e:
            write_error_log(e)

    def read_dataframe(self):
        try:
            dataframe = pd.read_csv(self.get_path(), encoding='utf-8')
        except FileNotFoundError:
            print("failed load data")
            self.__error_savedataframe()
        except Exception as e:
            write_error_log(e)
        else:
            return dataframe
