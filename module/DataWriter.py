import os
import sys
from typing import List
import pandas as pd
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class FileNameList:
    jl: str = 'join_left'


@dataclass(frozen=True)
class DataTypeList:
    jl: List[str] = ('Date', 'Time', 'Member-ID', 'Member-Name', 'Stat')


@dataclass(frozen=True)
class DataIndexList:
    pass


class GetList:
    def __init__(self, event) -> None:
        self.__event = event
        if event == None:
            raise ValueError("The parameter cannot contain 'None'.")

    def get_filename(self):
        return getattr(FileNameList(), self.__event, None)

    def get_datatype(self):
        return getattr(DataTypeList(), self.__event, None)


class DataInformationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        sys.exit()


class GeneratorDataFrame:
    def __init__(self, guild, event: str):
        self.__path = "database/{}_{}/".format(guild.id, guild.name)
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


class CsvWriter(GeneratorDataFrame):
    def __init__(self, server, event: str):
        super().__init__(server, event)

    def add_data(self, id: int = 0, name: str = "Error", stat: str = "Error"):
        time = datetime.now()
        if id == 0 or name == "Error" or stat == "Error":
            raise DataInformationError(
                "There is a problem with the received Data value.")
        self._dataframe.loc[len(self._dataframe)+1] =\
            [time.strftime("%Y.%m.%d"), time.strftime(
                "%H:%M:%S"), id, name, stat]

    def save_data(self):
        path = self.get_path()
        try:
            self._dataframe.to_csv(path, encoding='utf-8', index=False)
            print("sucess save data")
        except Exception as e:
            print("An unexpected error occurred:", e)
            time = datetime.now()
            file = open('log', encoding='utf-8')
            file.write(time.strftime("%Y.%m.%d %H:%M:%S"), "-> Error:", e)
            sys.exit()

    def get_data(self):
        return self._dataframe
