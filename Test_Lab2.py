import Lab2

def test_get_user_input():
    result = Lab2.get_user_input("5,67,32")
    assert result == [5.0, 67.0, 32.0]

def test_find_min_max():
    input_arr = [1, 10, 30]
    result = Lab2.calc_min_max_temperature(input_arr)
    assert result == [1, 30]

def test_calc_average():
    input_arr = [2, 10, 30]
    result = Lab2.calc_average_temperature(input_arr)
    assert result == 14

def test_calc_median_temperature():
    input_arr = [5, 9, 100]
    result = Lab2.calc_median_temperature(input_arr)
    assert result == 9
    