import pandas as pd

# Завантаження даних з файлу
file_path = 'comptagevelo2009.csv'
data = pd.read_csv(file_path)

# Перетворення стовпця з датами у формат datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Додавання нового стовпця для місяця
data['Month'] = data['Date'].dt.month

# Підрахунок загальної кількості велосипедистів для кожного місяця
monthly_counts = data.groupby('Month').sum(numeric_only=True).sum(axis=1)

# Визначення найбільш популярного місяця
most_popular_month = monthly_counts.idxmax()
most_popular_month_total = monthly_counts.max()

# Виведення результатів
print("Кількість велосипедистів по місяцях:")
print(monthly_counts)
print(f"\nНайбільш популярний місяць: {most_popular_month}")
print(f"Загальна кількість велосипедистів у цьому місяці: {most_popular_month_total}")
