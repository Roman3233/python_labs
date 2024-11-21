import json
from datetime import datetime

train_schedule = [
    {"train_number": 101, "destination": "Київ - Харків", "arrival": {"hour": 10, "minute": 30},
     "departure": {"hour": 11, "minute": 15}},
    {"train_number": 102, "destination": "Львів - Одеса", "arrival": {"hour": 12, "minute": 45},
     "departure": {"hour": 13, "minute": 10}},
    {"train_number": 103, "destination": "Дніпро - Київ", "arrival": {"hour": 14, "minute": 0},
     "departure": {"hour": 14, "minute": 30}},
    {"train_number": 104, "destination": "Харків - Львів", "arrival": {"hour": 16, "minute": 0},
     "departure": {"hour": 16, "minute": 45}},
    {"train_number": 105, "destination": "Одеса - Київ", "arrival": {"hour": 18, "minute": 20},
     "departure": {"hour": 18, "minute": 50}},
    {"train_number": 106, "destination": "Запоріжжя - Київ", "arrival": {"hour": 19, "minute": 30},
     "departure": {"hour": 20, "minute": 0}},
    {"train_number": 107, "destination": "Київ - Дніпро", "arrival": {"hour": 21, "minute": 10},
     "departure": {"hour": 21, "minute": 40}},
    {"train_number": 108, "destination": "Львів - Харків", "arrival": {"hour": 23, "minute": 5},
     "departure": {"hour": 23, "minute": 50}},
    {"train_number": 109, "destination": "Одеса - Запоріжжя", "arrival": {"hour": 3, "minute": 30},
     "departure": {"hour": 4, "minute": 0}},
    {"train_number": 110, "destination": "Дніпро - Львів", "arrival": {"hour": 7, "minute": 50},
     "departure": {"hour": 8, "minute": 20}}
]


def save_train_schedule():
    try:
        with open("train_schedule.json", "w", encoding="utf-8") as json_file:
            json.dump(train_schedule, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка при збереженні JSON файлу: {e}")

def load_train_schedule():
    try:
        with open("train_schedule.json", "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except Exception as e:
        print(f"Помилка при завантаженні JSON файлу: {e}")
        return None

def check_trains_on_station(hour, minute):
    data = load_train_schedule()
    if not data:
        return

    current_time = hour * 60 + minute

    trains_on_station = []
    for train in data:
        arrival_time = train["arrival"]["hour"] * 60 + train["arrival"]["minute"]
        departure_time = train["departure"]["hour"] * 60 + train["departure"]["minute"]

        if arrival_time <= current_time <= departure_time:
            trains_on_station.append(f"Поїзд {train['train_number']} ({train['destination']})")

    if trains_on_station:
        print("Поїзди, які знаходяться на станції в заданий час:")
        for train in trains_on_station:
            print(train)
    else:
        print("Немає поїздів на станції в цей час.")

if __name__ == "__main__":
    save_train_schedule()
    try:
        hour = int(input("Введіть годину (0-23): "))
        minute = int(input("Введіть хвилини (0-59): "))

        if 0 <= hour <= 23 and 0 <= minute <= 59:
            check_trains_on_station(hour, minute)
        else:
            print("Невірне значення часу.")
    except ValueError:
        print("Введено некоректне значення.")
