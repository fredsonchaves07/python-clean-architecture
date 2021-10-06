from datetime import datetime


class Coupon:
    def __init__(self, code: str, percentage: int, date_expire: str = None) -> None:
        self._code = code
        self.percentage = percentage
        if not date_expire:
            self._date_expire = datetime.now()
        else:
            self._date_expire = datetime.strptime(date_expire, "%d-%m-%Y")

    def is_expired(self, today: str) -> bool:
        if self._date_expire < datetime.strptime(today, "%d-%m-%Y"):
            return True
        return False
