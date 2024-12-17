import json

def load_data():
    try:
        with open('citi.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл citi.json не найден. Создание нового файла.")
        return []

def save_data(data):
    with open('citi.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_all_records(data):
    if not data:
        print("Нет записей для отображения.")
        return
    for record in data:
        print(f'Номер записи: {record["id"]}')
        print(f"Название города: {record['name']}")
        print(f"Название страны: {record['country']}")
        print(f"Является ли население города больше 100 000 человек: {record['is_big']}")
        print(f"Население города: {record['people_count']}\n")

def display_record_by_id(data, record_id):
    found = False
    for record in data:
        if record['id'] == record_id:
            print(f"Название города: {record['name']}")
            print(f"Название страны: {record['country']}")
            print(f"Является ли население города больше 100 000 человек: {record['is_big']}")
            print(f"Население города: {record['people_count']}")
            found = True
            break
    if not found:
        print("Записи нет")

def add_record(data):
    new_record = {}
    new_record['id'] = str(max(int(city['id']) for city in data) + 1 if data else 1)
    new_record['name'] = input("Введите название города: ")
    new_record['country'] = input("Введите название страны: ")

    while True:
        people_count = input("Введите население города: ")
        if people_count.isdigit():
            new_record['people_count'] = int(people_count)
            break
        else:
            print("Ошибка: население города должно быть числом.")

    new_record['is_big'] = new_record['people_count'] > 100000
    data.append(new_record)
    save_data(data)
    print("Запись добавлена")

def delete_record(data, record_id):
    found = False
    for record in data:
        if record['id'] == record_id:
            data.remove(record)
            found = True
            break
    if found:
        save_data(data)
        print("Запись удалена")
    else:
        print("Запись не найдена")

def main():
    count = 0
    data = load_data()
    while True:
        print("1. Вывести все записи")
        print("2. Вывести запись по ID")
        print("3. Добавить запись")
        print("4. Удалить запись по ID")
        print("5. Выйти из программы")
        num = input('Выберите пункт: ')

        if num == '1':
            count += 1
            display_all_records(data)

        elif num == '2':
            count += 1
            field = input('Введите ID записи: ')
            display_record_by_id(data, field)

        elif num == '3':
            count += 1
            add_record(data)

        elif num == '4':
            count += 1
            field = input("Введите ID для удаления: ")
            delete_record(data, field)

        elif num == '5':
            print(f"{count} выполненных операций")
            break

        else:
            print("Нет такого пункта")

if __name__ == "__main__":
    main()