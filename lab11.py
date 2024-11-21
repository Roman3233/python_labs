import csv


def read_and_display_csv(file_name):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


def search_and_save(file_name, output_file_name, year, min_value, max_value):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Зчитуємо заголовок
            year_index = header.index(year)  # Отримуємо індекс вибраного року

            results = [header]
            for row in reader:
                try:
                    value = float(row[year_index])
                    if min_value <= value <= max_value:
                        results.append(row)
                except ValueError:
                    pass

        with open(output_file_name, mode='w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(results)

        print(f"Результати збережено у файл '{output_file_name}'.")

    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")

if __name__ == "__main__":
    input_file = "exports_2015_2019.csv"
    output_file = "inports_2015_2019.csv"

    print("Вміст файлу:")
    read_and_display_csv(input_file)

    try:
        year = input("Введіть рік (2015-2019): ").strip()
        min_value = float(input("Введіть мінімальне значення: "))
        max_value = float(input("Введіть максимальне значення: "))

        if year not in ["2015", "2016", "2017", "2018", "2019"]:
            raise ValueError("Рік повинен бути в діапазоні 2015-2019.")

        search_and_save(input_file, output_file, year, min_value, max_value)
    except ValueError as ve:
        print(f"Помилка вводу: {ve}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
