import json

filename = 'data.json'

# Считываем данные из файла
try:
    with open(filename, 'r', encoding='utf-8') as file:
        flowers = json.load(file)
except FileNotFoundError:
    flowers = []


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
        for flower in flowers:
            print(json.dumps(flower, ensure_ascii=False, indent=4))
        operation_count += 1

    elif choice == '2':
        # Вывод записи по полю
        search_id = int(input("Введите id записи для поиска: "))
        found = False
        for index, flower in enumerate(flowers):
            if flower['id'] == search_id:
                print(f"\nНайдена запись (позиция {index}):")
                print(json.dumps(flower, ensure_ascii=False, indent=4))
                found = True
                operation_count += 1
                break
        if not found:
            print("Запись не найдена.")

    elif choice == '3':
        # Добавление записи
        new_id = int(input("Введите id новой записи: "))
        new_name = input("Введите общее название цветка: ")
        new_latin_name = input("Введите латинское название цветка: ")
        new_is_red_book_flower = input("Является ли цветок краснокнижным? (да/нет): ").strip().lower() == 'да'
        new_price = float(input("Введите стоимость цветка: "))
        
        new_flower = {
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin_name,
            "is_red_book_flower": new_is_red_book_flower,
            "price": new_price
        }
        flowers.append(new_flower)
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(flowers, file, ensure_ascii=False, indent=4)
        
        print("Запись добавлена.")
        operation_count += 1

    elif choice == '4':
        # Удаление записи по полю
        delete_id = int(input("Введите id записи для удаления: "))
        found = False
        
        for index, flower in enumerate(flowers):
            if flower['id'] == delete_id:
                flowers.pop(index)
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(flowers, file, ensure_ascii=False, indent=4)
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

