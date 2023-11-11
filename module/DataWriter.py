import os
import pandas as pd
from datetime import datetime as t


class GeneratorDataFrame:
    def __init__(self, guild: str, event: str):
        self._EVENTLIST = {'jl': 'join_left'}
        self.__dataframe = None
        self.__filename = None
        self.__path = None
        if event not in list(self._EVENTLIST.keys()):
            raise ValueError("The event value must be one of 'jl'")

    def get_dataframe(self):
        if self.__Event == 'jl':
            return self.__join_out()

    def __join_out(self):
        header = ['Date', 'Time',
                  'Member-ID', 'Member-Name', 'Stat']
        return pd.DataFrame(columns=header)

    def read_dataframe(self):
        try:
            self.__dataframe = pd.read_csv(self.__path, encoding='utf-8')
        except:
            print(self.__path,"is not found...")
            

    
    def save_dateframe(self):
        try: 
            self.

    def __del__(self):
        pass


class CsvWriter(GeneratorDataFrame):
    def __init__(self, server: str, event: str):
        super().__init__(event)
        self.__server = server
        self.__filename = self._EVENTLIST[event]
        self.__path = "./database/{}/".format(server)
        self.__data = super().get_dataframe()

    def save_file(self):
        __path = str(self.get_path())+str(self.__filename) + ".csv"
        try:
            self.__data.to_csv(__path,
                               encoding='utf-8', index=False)
            print("success save data")
        except:
            print(self.get_path(), "is not folder")
            os.mkdir(self.get_path())
            self.save_file()

    def add_data(self, id: int, name: str, stat: str):
        time = t.now()
        self.get_data().loc[len(self.__data)-1] = [
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
