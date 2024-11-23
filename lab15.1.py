import math
import pandas as pd

def convert_to_integers():
    float_list = input("Введіть список дійсних чисел (через пробіл): ").split()
    float_list = [float(num) for num in float_list]

    # Перетворення на цілі числа за правилами округлення
    int_list = [math.ceil(num) if num - int(num) >= 0.5 else math.floor(num) for num in float_list]
    print("Список цілих чисел:", int_list)

    # Створення словника
    data = {
        'Original': float_list,
        'Converted': int_list,
        'Category': ['Even' if num % 2 == 0 else 'Odd' for num in int_list]
    }

    # Перетворення на датафрейм
    df = pd.DataFrame(data)
    print("\nСтворений DataFrame:")
    print(df)

    # Виконання агрегації та групування
    grouped = df.groupby('Category')['Converted'].agg(['mean', 'sum', 'count'])
    print("\nРезультат агрегації та групування:")
    print(grouped)
    
convert_to_integers()
