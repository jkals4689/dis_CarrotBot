import sys
from datetime import datetime


class DataInformationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        sys.exit()


def write_error_log(e: Exception = None):
    print("An unexpected error occurred:", e)
    time = datetime.now()
    file = open('log', encoding='utf-8')
    file.write(time.strftime("%Y.%m.%d %H:%M:%S"), "-> Error:", e)
    file.close()
    sys.exit()
