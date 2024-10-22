def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    number = input()
    number_split = number.split(",")
    number_floats = [float(num) for num in number_split]
    return number_floats

def calc_average_temperature():
    print("calc_average")
    return 0.02

def calc_min_max_temperature():
    print("find_min_max")
    return [0.0, 0.0]

def sort_temperature():
    print("sort_temperature")
    return []

def calc_median_temperature():
    print("calc_median_temperature")
    return 0.0