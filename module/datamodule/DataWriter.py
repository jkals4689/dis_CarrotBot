import sys
from datetime import datetime
from .gendataframe import GeneratorDataFrame


class DataInformationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        sys.exit()


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


class SettingsWriter(GeneratorDataFrame):
    def __init__(self, guild, event: str):
        super().__init__(guild, event)
