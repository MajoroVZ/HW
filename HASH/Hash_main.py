from Hash import *


def main():
    hash_table = init_hash_table()
    while True:
        print('1)Добавить ключ-значение')
        print("2)Удалить значение")
        print("3)Получить значение")
        print("4)Коэффициент заполнения")
        print("5)Вывести таблицу")
        print("6)Выход")
        inp = input("Ваш выбор: ")
        if inp == str(1):
            while True:
                key = input("Ключ: ")
                set_value(hash_table, key, input("Значение: "))
                if key == 'end':
                    del_value(hash_table, "end")
                    break
        elif inp == str(2):
            while True:
                key = input("Введите ключ: ")
                del_value(hash_table, key)
                if key == 'end':
                    break
        elif inp == str(3):
            while True:
                key = input("Введите ключ: ")
                print(get_value(hash_table, key))
                if key == 'end':
                    break
        elif inp == str(4):
            print(load_factor(hash_table))
        elif inp == str(5):
            print(hash_table)
        elif inp == str(6):
            break


main()
