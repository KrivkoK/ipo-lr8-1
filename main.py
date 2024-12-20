import json

filename = 'data.json'

# Считываем данные из файла
with open(filename, 'r', encoding='utf-8') as file:
    records = json.load(file)

operation_count = 0

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    
    choice = input("Выберите пункт меню (1-5): ")
    
    if choice == '1':
        # Вывод всех записей
        print("\nВсе записи:")
        for record in records:
            print(json.dumps(record, ensure_ascii=False, indent=4))
        operation_count += 1

    elif choice == '2':
        # Вывод записи по полю
        search_id = int(input("Введите id записи для поиска: "))
        found = False
        for index, record in enumerate(records):
            if record['id'] == search_id:
                print(f"\nНайдена запись (позиция {index}):")
                print(json.dumps(record, ensure_ascii=False, indent=4))
                found = True
                operation_count += 1
                break
        if not found:
            print("Запись не найдена.")

    elif choice == '3':
        # Добавление записи
        new_id = int(input("Введите id новой записи: "))
        new_name = input("Введите имя новой записи: ")
        new_value = input("Введите значение новой записи: ")
        
        new_record = {"id": new_id, "name": new_name, "value": new_value}
        records.append(new_record)
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(records, file, ensure_ascii=False, indent=4)
        
        print("Запись добавлена.")
        operation_count += 1

    elif choice == '4':
        # Удаление записи по полю
        delete_id = int(input("Введите id записи для удаления: "))
        found = False
        
        for index, record in enumerate(records):
            if record['id'] == delete_id:
                records.pop(index)
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(records, file, ensure_ascii=False, indent=4)
                print("Запись удалена.")
                found = True
                operation_count += 1
                break
        
        if not found:
            print("Запись не найдена.")

    elif choice == '5':
        # Выход из программы
        print(f"\nКоличество выполненных операций: {operation_count}")
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите номер пункта от 1 до 5.")
