def reverse_array():
    n = int(input("Введіть кількість елементів масиву: "))

    array = []
    for i in range(n):
        element = int(input(f"Введіть елемент {i + 1}: "))
        array.append(element)

    print("Масив у зворотному порядку:")
    print(array[::-1])

reverse_array()