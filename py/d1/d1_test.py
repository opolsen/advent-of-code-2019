from d1 import solve_1, solve_2


def test_1():
    assert solve_1([12]) == 2
    assert solve_1([14]) == 2
    assert solve_1([1969]) == 654
    assert solve_1([100756]) == 33583

def test_2():
    assert solve_2([14]) == 2
    assert solve_2([1969]) == 966
    assert solve_2([100756]) == 50346
