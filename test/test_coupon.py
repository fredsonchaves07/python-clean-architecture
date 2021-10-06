from src.coupon import Coupon


def test_coupon_not_expired():
    coupon = Coupon("VALE20", "11-10-2021")
    is_expired = coupon.is_expired("05-10-2021")
    assert not is_expired


def test_coupon_expired():
    coupon = Coupon("VALE20", "11-09-2021")
    is_expired = coupon.is_expired("10-10-2021")
    assert is_expired
