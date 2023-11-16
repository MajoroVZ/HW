class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def hash(self, key: str) -> int:
        return (sum(ord(str(c)) for c in key)) % self.capacity

    def set_value(self, key: str, value):
        key_hash = self.hash(key)
        key_value = [key, value]
        if self.buckets[key_hash] is None:
            self.buckets[key_hash] = list([key_value])
            self.size += 1
            return True
        for pair in self.buckets[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.buckets[key_hash].append(key_value)
        self.size += 1
        return True

    def get_value(self, key):
        key_hash = self.hash(key)
        if self.buckets[key_hash] is not None:
            for pair in self.buckets[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def del_value(self, key):
        key_hash = self.hash(key)
        if self.buckets[key_hash] is None:
            return False
        for i in range(0, len(self.buckets[key_hash])):
            if self.buckets[key_hash][i][0] == key:
                self.buckets[key_hash].pop(i)
                self.size -= 1
                return True
        return False

    def load_factor(self):
        return self.size / self.capacity


def main():
    Hash = HashTable()
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
                Hash.set_value(input("Ключ: "), input("Значение: "))
                if input == '':
                    break
        elif inp == str(2):
            while input:
                Hash.del_value(input("Введите ключ: "))
        elif inp == str(3):
            pass
        elif inp == str(4):
            pass
        elif inp == str(5):
            print(Hash.buckets)
        elif inp == str(6):
            break


main()
'''print(h.hash("daniil"))
print(h.set_value("daniil", "pads;fj"))
print(h.set_value("denis", "ta;ldkf;lasdkfa;"))
print(h.set_value("dadfasdfnis", "ta;ldkf;lasdkfa;"))
print(h.del_value("daniil"))
print(h.get_value("daniil" ))
print(h.load_factor())
print(h.buckets)'''
