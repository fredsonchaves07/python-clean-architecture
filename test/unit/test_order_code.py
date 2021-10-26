from src.domain.entity.order_code import OrderCode
from datetime import datetime


def test_order_with_order_code():
    date = datetime.now()
    sequence = 1
    code = OrderCode(date, sequence).code
    assert code == "2021000000001"