import os
import pandas as pd
from datetime import datetime as t
from dataclasses import dataclass


@dataclass(frozen=True)
class EventList:
    jl: str = 'join_left'


def get_event(event: str):
    if event == None:
        raise ValueError("The parameter cannot contain 'None'.")
    return getattr(EventList(), event, None)


class GeneratorDataFrame:
    def __init__(self, guild: str, event: str):
        self.__dataframe = self.read_dataframe()
        self.__filename = get_event(event)
        self.__path = f"./database/{guild.id}_{guild.name}/"
        if event not in list(self._EVENTLIST.keys()):
            raise ValueError("The event value must be one of 'jl'.")

    def get_dataframe(self):
        if self.__Event == 'jl':
            return self.__join_out()

    def __join_out(self):
        header = ['Date', 'Time',
                  'Member-ID', 'Member-Name', 'Stat']
        return pd.DataFrame(columns=header)

    def read_dataframe(self):
        try:
            return pd.read_csv(self.__path, encoding='utf-8')
        except:
            print(self.__path, "is not found...")
            self.save_dataframe()

    def save_dataframe(self):
        try:
            self.__dataframe.to_csv(
                self.__path+self.__filename, encoding='utf-8', index=False)
            print("success save data")
        except:
            print("error:", self.__path, "does not exist")
            print("falied save data")
            os.mkdir(self.__path)
            self.save_dataframe()

    def __del__(self):
        pass


class CsvWriter(GeneratorDataFrame):
    def __init__(self, server: str, event: str):
        super().__init__(event)
        self.__server = server
        self.__filename = self._EVENTLIST[event]
        self.__path = "./database/{}/".format(server)
        self.__data = super().get_dataframe()

    def add_data(self, id: int, name: str, stat: str):
        time = t.now()
        self.__data.loc[len(self.__data)-1] = [
            time.strftime("%Y.%m.%d"),
            time.strftime("%H:%M:%S"),
            id, name, stat]

    def get_data(self):
        return self.__data

    def get_server(self):
        return self.__server

    def get_filename(self):
        return self.__filename

    def get_path(self):
        return self.__path
