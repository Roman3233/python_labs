import math
def convert_to_integers():
    float_list = input("Введіть список дійсних чисел(Через пробіл)").split()

    float_list = [float(num) for num in float_list]

    int_list = [math.ceil(num) if num - int(num) >= 0.5 else math.floor(num) for num in float_list]

    print("Список цілих чисел:", int_list)

convert_to_integers()
