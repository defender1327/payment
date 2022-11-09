#
from payment import calculate as cal

def test(a,b):
    result = cal(a,b)
    test_c = a+b

    assert result == test_c


test(13,27)
test(0,5)
test(5,5)

