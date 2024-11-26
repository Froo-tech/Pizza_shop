import json



def order(pozicion_index, *args, **kwargs):
        print("\n==============================")
        print("            Ваш чек:         ")
        print("------------------------------")
        pozicion_index(*args, **kwargs)
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


    def main():
        print("Добро пожаловать в кафе!")
        order = take_order()

        if not order:
            print("Вы не сделали заказ.")
            return

        total = calculate_total(order)
        payment_method = input("Выберите способ оплаты (нал/безнал): ").strip().lower()

        if payment_method == 'нал':
            cash_given = int(input("Введите сумму, которую вы даете: "))
            if cash_given < total:
                print("Недостаточно средств для оплаты.")
                return
            display_receipt(order, total, payment_method, cash_given)
        elif payment_method == 'безнал':
            display_receipt(order, total, payment_method)
            draw_terminal()
            states = input()
            if states == '1':
                print("Ожидаем подтверждения ю-мани \n""У вас медленный интернет ")
                time.sleep(3)
                print('Успешноооо')
        else:
            print("Некорректный способ оплаты.")

    if __name__ == "__main__":
        main()


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
    age = int(input("Введите возраст: "))

    user_data = {
        "login": name,
        "password": password,
        "age": age
    }

    try:

        try:
            with open("data_user.json", 'r') as file:
                a = list(json.load(file).get('users', []))
        except FileNotFoundError:
            a = []


        for i in a:
            if i['login'] == name:
                print("Вы уже зарегистрированы")
                return

        a.append(user_data)
        with open("data_user.json", 'w') as file:
            json.dump({"users": a}, file, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены в файл data_user.json.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

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