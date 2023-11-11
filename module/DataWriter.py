import pandas as pd
from datetime import datetime as t


class GeneratorDataFrame:
    def __init__(self, event: str):
        self.__EventList = ['jl']
        if event not in self.__EventList:
            raise ValueError("The event value must be one of 'jl'")
        self.__Event = event

    def get_dataframe(self):
        if self.__Event == self.__EventList[0]:
            return self.__join_out()

    def __join_out(self):
        header = ['Date', 'Time',
                  'Member-ID', 'Member-Name', 'Stat']
        return pd.DataFrame(columns=header)


class CsvWriter(GeneratorDataFrame):
    def __init__(self, server: str, event: str):
        super().__init__(event)
        self.__path = "./database/{}/{}".format(server, event)
        self.__data = super().get_dataframe()

    def save_file(self):
        self.__data.to_csv(self.__path, encoding='utf-8', index=False)

    def add_data(self, id: int, name: str, stat: str):
        time = t.now()
        self.__data.loc[len(self.__data)] = [
            time.strftime("%Y.%m.%d"),
            time.strftime("%H:%M:%S"),
            id, name, stat]
