import os
import sys
import pandas as pd
from datetime import datetime
from .datalist import GetList


class GeneratorDataFrame:
    def __init__(self, guild, event: str = ""):
        self.__path = "database/{}_{}/".format(guild.id, guild.name)
        if event != "":
            self.__filename = GetList(event).get_filename()
            self.__type = GetList(event).get_datatype()
            self._dataframe = self.read_dataframe()

    def get_path(self):
        return self.__path+self.__filename+".csv"

    def __error_savedataframe(self):
        path = self.get_path()
        try:
            self._dataframe.to_csv(path, encoding='utf-8', index=False)
            print("success save data")
        except AttributeError:
            print("Data is not defined.")
            self._dataframe = pd.DataFrame(columns=self.__type)
            self.__error_savedataframe()
        except OSError:
            print(f"Dir {self.__path} does not exist")
            os.mkdir(self.__path)
            self.__error_savedataframe()
        except Exception as e:
            print("An unexpected error occurred:", e)
            time = datetime.now()
            file = open('log', encoding='utf-8')
            file.write(time.strftime("%Y.%m.%d %H:%M:%S"), "-> Error:", e)
            sys.exit()

    def read_dataframe(self):
        path = self.get_path()
        try:
            dataframe = pd.read_csv(path, encoding='utf-8')
        except FileNotFoundError:
            print("failed load data")
            self.__error_savedataframe()
        except Exception as e:
            print("An unknown error has occurred!")
            print(e)
            sys.exit()
        else:
            return dataframe
