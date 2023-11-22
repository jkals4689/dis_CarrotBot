import sys
from datetime import datetime
from pathlib import Path


class DataInformationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        sys.exit()


def write_error_log(e: Exception):
    print("An unexpected error occurred:", e)
    time = datetime.now()
    path = Path(Path.cwd()/'log.txt')
    file = open(path, encoding='utf-8')
    file.write(f'{time.strftime(" % Y. % m. % d % H: % M: %S")} -> Error: {e}')
    file.close()
    sys.exit()
