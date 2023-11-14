from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class FileNameList:
    jl: str = 'join_left'
    update: str = 'member_update'


@dataclass(frozen=True)
class DataTypeList:
    jl: List[str] = ('Date', 'Time', 'Member-ID', 'Member-Name', 'Stat')
    update: List[str] = (('Date', 'Time','ID','Name'),(('before', 'after'),('nickname','role')))


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