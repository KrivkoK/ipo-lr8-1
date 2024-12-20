# Список для хранения записей о цветах
flowers = []

def display_menu():
    print("\nМеню:")
    print("1. Добавить цветок")
    print("2. Удалить цветок")
    print("3. Показать все цветы")
    print("4. Выход")

def add_flower():
    flower_id = len(flowers) + 1  # Генерация ID на основе длины списка
    name = input("Введите общее название цветка: ")
    latin_name = input("Введите латинское название цветка: ")
    is_red_book_flower = input("Является ли цветок краснокнижным? (да/нет): ").strip().lower() == 'да'
    price = float(input("Введите стоимость цветка: "))

    flower = {
        "id": flower_id,
        "name": name,
        "latin_name": latin_name,
        "is_red_book_flower": is_red_book_flower,
        "price": price
    }
    
    flowers.append(flower)
    print(f"Цветок '{name}' добавлен.")

def remove_flower():
    flower_id = int(input("Введите ID цветка для удаления: "))
    for flower in flowers:
        if flower["id"] == flower_id:
            flowers.remove(flower)
            print(f"Цветок с ID {flower_id} удален.")
            return
    print("Цветок с таким ID не найден.")

def show_flowers():
    if not flowers:
        print("Список цветов пуст.")
        return

    print("\nСписок цветов:")
    for flower in flowers:
        red_book_status = "Да" if flower["is_red_book_flower"] else "Нет"
        print(f"ID: {flower['id']}, Название: {flower['name']}, "
              f"Латинское название: {flower['latin_name']}, "
              f"Краснокнижный: {red_book_status}, "
              f"Стоимость: {flower['price']}")

def main():
    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            add_flower()
        elif choice == '2':
            remove_flower()
        elif choice == '3':
            show_flowers()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
