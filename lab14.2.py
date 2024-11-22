import pandas as pd
import matplotlib.pyplot as plt

# Читання даних із CSV файлу
file_name = "exports_2015_2019.csv"
try:
    data = pd.read_csv(file_name)

    # Вибір двох країн для динаміки показника
    country1 = "Ukraine"
    country2 = "Germany"

    country1_data = data[data["Country"] == country1].iloc[0, 1:].values
    country2_data = data[data["Country"] == country2].iloc[0, 1:].values
    years = [2015, 2016, 2017, 2018, 2019]

    # Побудова лінійних графіків
    plt.figure(figsize=(10, 6))
    plt.plot(years, country1_data, marker='o', label=f"{country1}", linewidth=2, color='blue')
    plt.plot(years, country2_data, marker='o', label=f"{country2}", linewidth=2, color='orange')

    # Оформлення графіка
    plt.title("Динаміка показника Exports of goods and services (% of GDP)", fontsize=14)
    plt.xlabel("Рік", fontsize=12)
    plt.ylabel("Показник (% of GDP)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.show()
    # Стовпчаста діаграма
    country_name = input("Введіть назву країни для побудови стовпчастої діаграми: ")
    if country_name not in data["Country"].values:
        print(f"Країну '{country_name}' не знайдено в даних.")
    else:
        country_values = data[data["Country"] == country_name].iloc[0, 1:].values

        plt.figure(figsize=(10, 6))
        plt.bar(years, country_values, color='green', alpha=0.7)
        plt.title(f"Стовпчаста діаграма показника для країни {country_name}", fontsize=14)
        plt.xlabel("Рік", fontsize=12)
        plt.ylabel("Показник (% of GDP)", fontsize=12)
        plt.show()

except FileNotFoundError:
    print(f"Файл '{file_name}' не знайдено. Переконайтеся, що він знаходиться в тій самій папці, що й програма.")
except Exception as e:
    print(f"Виникла помилка: {e}")
