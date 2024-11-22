import json
import matplotlib.pyplot as plt

file_name = "train_schedule.json"
try:
    with open(file_name, 'r') as file:
        train_data = json.load(file)

    # Підрахунок кількості поїздів для кожного напрямку
    destinations = {}
    for train in train_data["trains"]:
        destination = train["destination"]
        destinations[destination] = destinations.get(destination, 0) + 1

    labels = list(destinations.keys())
    sizes = list(destinations.values())

    # Побудова кругової діаграми
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Розподіл поїздів за напрямками", fontsize=14)
    plt.axis('equal')
    plt.show()

except FileNotFoundError:
    print(f"Файл '{file_name}' не знайдено. Переконайтеся, що він знаходиться в тій самій папці, що й програма.")
except json.JSONDecodeError:
    print(f"Помилка обробки JSON файлу '{file_name}'. Перевірте його вміст.")
except Exception as e:
    print(f"Виникла помилка: {e}")
