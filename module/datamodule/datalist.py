from dataclasses import dataclass
from typing import List

# 사용하지 않는 구조체들
# @dataclass(frozen=True)
# class FileNameList:
#     jl: str = 'join_left'
#     update: str = 'member_update'
#     settings: str = 'settings'


@dataclass(frozen=True)
class DataTypeList:
    jl: List[str] = ('Date', 'Time', 'Member-ID', 'Member-Name', 'Stat')
    update: List[str] = (('Date', 'Time','ID','Name'),(('before', 'after'),('nickname','role')))
    settings: List[str] = (('LogCh','Role','TxtCh','Warn-Role','Warn-Ch'),('ID','Name'))


@dataclass(frozen=True)
class DataIndexList:
    pass


class GetList:
    def __init__(self, event:str = None) -> None:
        self.__event = event
        if event == None:
            raise ValueError("The parameter cannot contain 'None'.")

    # 사용하지 않는 함수
    # def get_filename(self):
    #     return getattr(FileNameList(), self.__event, None)

    def get_datatype(self):
        return getattr(DataTypeList(), self.__event, None)