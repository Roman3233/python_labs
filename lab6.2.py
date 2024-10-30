def find_shortest_word(word_list):
    if not word_list:
        print("Список порожній.")
        return

    shortest_word = min(word_list, key=len)

    print(f"Найкоротше слово: '{shortest_word}'")

user_input = input("Введіть список слів через пробіл: ")
word_list = user_input.split()

find_shortest_word(word_list)
