from dataclasses import dataclass
from typing import List

# 사용하지 않는 구조체들
# @dataclass(frozen=True)
# class FileNameList:
#     jl: str = 'join_left'
#     update: str = 'member_update'
#     settings: str = 'settings'


@dataclass(frozen=True)
class InitDataList:
    userdata: List[str] = ('')
    settings: List[str] = ('ID', 'Name', 'LogCh', 'Role',
                           'TxtCh', 'Warn-Role', 'Warn-Ch')


@dataclass(frozen=True)
class DataIndexList:
    pass


class GetList:
    def __init__(self, event: str = None) -> None:
        self.__event = event
        if event == None:
            raise ValueError("The parameter cannot contain 'None'.")

    # 사용하지 않는 함수
    # def get_filename(self):
    #     return getattr(FileNameList(), self.__event, None)

    def get_datatype(self):
        return getattr(InitDataList(), self.__event, None)
