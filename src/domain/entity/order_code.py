from datetime import datetime


class OrderCode:
    def __init__(self, date: datetime, sequence):
        self._year = date.year
        self._sequence = f'{sequence}'.zfill(9)
        self._code = str(self._year) + self._sequence

    @property
    def code(self):
        return self._code