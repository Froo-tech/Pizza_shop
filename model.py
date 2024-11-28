import json
import time

def take_order():
    """Функция для симуляции приема заказа (заглушка)."""
    order = {
        "items": [
            {"name": "Кофе", "price": 100},
            {"name": "Пирог", "price": 150}
        ]
    }
    return order

def calculate_total(order):
    """Вычисляет общую стоимость заказа."""
    total = sum(item["price"] for item in order["items"])
    return total

def display_receipt(order, total, payment_method, cash_given=None):
    """Выводит чек."""
    print("\n==============================")
    print("            Ваш чек:         ")
    print("------------------------------")
    for item in order["items"]:
        print(f"{item['name']}: {item['price']} руб.")
    print("------------------------------")
    print(f"Итого: {total} руб.")
    print(f"Способ оплаты: {payment_method}")
    if cash_given:
        change = cash_given - total
        print(f"Сдача: {change} руб.")
    print("==============================")

def draw_terminal():
        terminal = [
            "==============================",
            "|                            |",
            "|         ПЛАТЕЖНЫЙ         |",
            "|         ТЕРМИНАЛ          |",
            "|                            |",
            "|  Введите сумму:           |",
            "|  ______________________    |",
            "|                            |",
            "|  [1] Оплатить             |",
            "|  [2] Отмена               |",
            "|                            |",
            "=============================="
        ]

        for line in terminal:
            print(line)

def age_Check():
    try:
        with open("data_user.json", 'r') as file:
            file_obj = json.load(file)
            if 'age' in file_obj:
                print(file_obj['age'])
                return file_obj['age'] < 18
            else:
                print("Ключ 'age' не найден в данных.")
                return False
    except FileNotFoundError:
        print("Файл 'data_user.json' не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

def login():
    name = input("Введите логин: ")
    password = input("Введите пароль: ")
    while True:
        try:
            age = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Некорректный формат возраста. Попробуйте снова.")

    user_data = {
        "login": name,
        "password": password,
        "age": age
    }

    try:
        try:
            with open("data_user.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"users": []}

        for user in data["users"]:
            if user["login"] == name:
                print("Вы уже зарегистрированы")
                return

        data["users"].append(user_data)
        with open("data_user.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Данные успешно сохранены в файл data_user.json.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def main():
    print("Добро пожаловать в кафе!")
    if age_Check():
        print("Извините, вам не разрешен вход!")
        return
    login()
    order = take_order()
    if not order:
        print("Вы не сделали заказ.")
        return

    total = calculate_total(order)
    payment_method = input("Выберите способ оплаты (нал/безнал): ").strip().lower()

    if payment_method == 'нал':
        while True:
            try:
                cash_given = int(input("Введите сумму, которую вы даете: "))
                if cash_given >= total:
                    break
                else:
                    print("Недостаточно средств для оплаты.")
            except ValueError:
                print("Некорректный ввод суммы. Попробуйте снова.")
        display_receipt(order, total, payment_method, cash_given)
    elif payment_method == 'безнал':
        display_receipt(order, total, payment_method)
        draw_terminal()
        while True:
            choice = input()
            if choice == '1':
                print("Ожидаем подтверждения ю-мани \n""У вас медленный интернет ")
                time.sleep(3)
                print('Успешноооо')
                break
            elif choice == '2':
                print('Оплата отменена')
                break
            else:
                print('Некорректный выбор. Попробуйте снова.')
    else:
        print("Некорректный способ оплаты.")
            def load_user_data():
    log = input("Логин: ")
    password = input("Пароль: ")
    try:
        with open("data_user.json", 'r') as file:
            a = list(json.load(file).get('users', []))
            for i in a:
                if i['login'] == log:
                    if i['password'] == password:
                        print(f"Добро пожаловать, {log}")
                        return
                    else:
                        print("Неверный пароль")
                        return
            print("Пользователь не найден")
    except FileNotFoundError:
        print("Файл 'data_user.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


load_user_data()
login()


if __name__ == "__main__":
    main()
