def init_hash_table(capacity=100):
    size = 0
    buckets = [[] for _ in range(capacity)]
    return size, buckets


def hash_key(key: str, capacity: int) -> int:
    return (sum(ord(str(c)) for c in key)) % capacity


def set_value(hash_table, key: str, value):
    size, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    key_value = [key, value]
    if buckets[key_hash] is None:
        buckets[key_hash] = list([key_value])
        size += 1
        return True
    for pair in buckets[key_hash]:
        if pair[0] == key:
            pair[1] = value
            return True
    buckets[key_hash].append(key_value)
    size += 1
    return True


def get_value(hash_table, key):
    _, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    if buckets[key_hash] is not None:
        for pair in buckets[key_hash]:
            if pair[0] == key:
                return pair[1]
    return None


def del_value(hash_table, key):
    size, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    if buckets[key_hash] is None:
        return False
    for i in range(0, len(buckets[key_hash])):
        if buckets[key_hash][i][0] == key:
            buckets[key_hash].pop(i)
            size -= 1
            return True
    return False


def load_factor(hash_table):
    size, capacity = hash_table
    return size / len(capacity)


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
                if key == '':
                    del_value(hash_table, "")
                    break
        elif inp == str(2):
            while True:
                key = input("Введите ключ: ")
                del_value(hash_table, key)
                if key == '':
                    break
        elif inp == str(3):
            while True:
                key = input("Введите ключ: ")
                print(get_value(hash_table, key))
                if key == '':
                    break
        elif inp == str(4):
            print(load_factor(hash_table))
        elif inp == str(5):
            print(hash_table[1])
        elif inp == str(6):
            break


main()
