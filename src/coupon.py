from datetime import datetime


class Coupon:
    def __init__(self, code: str, percentage: int, date_expire: str = None) -> None:
        self._code = code
        self.percentage = percentage
        if not date_expire:
            self._date_expire = datetime.now().strftime("%d-%m-%Y")
        else:
            self._date_expire = date_expire

    def is_expired(self) -> bool:
        if self._date_expire < datetime.now().strftime("%d-%m-%Y"):
            return True
        return False
