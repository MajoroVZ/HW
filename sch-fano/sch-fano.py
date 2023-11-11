from collections import Counter
from math import log2


def count(text):
    return Counter(text).most_common(), len(text)


def veroyt(text):
    spisok_veroyt = {}
    for n, p in text:
        spisok_veroyt[n] = p / ln
    return spisok_veroyt


def calk_entrop3y(list_with):
    entropy = 0
    for p in list_with.values():
        entropy -= p * log2(p)
    return entropy


def redundancy_evenly(entropy: int, n: int) -> int:  # избыточность. H-энтропия, n-бит
    r = round(((1 - (entropy / n)) * 100), 2)
    return r


def shannon_fano_encoding(keys: list[str], values: list[float], code='') -> tuple:  # новый текст start
    i = sf_cut(values)
    pos_keys, pos_values, new_keys, new_values = keys[:i], values[:i], keys[i:], values[i:]
    '''Получаем на вход отдельно список ключей и список значений. Разделяем их (используем срез), получая
    в итоге 4 списка (2 из которых содержут просто ключи) с примерно одинаковой относительной вероятностью 
    появления символов.'''

    if len(pos_keys) == 1:
        if len(new_keys) == 1:
            return {pos_keys[0]: code + '0'}, {new_keys[0]: code + '1'}
        else:
            return {pos_keys[0]: code + '0'}, *shannon_fano_encoding(new_keys, new_values, code + '1')

    return (*shannon_fano_encoding(pos_keys, pos_values, code + '0'),
            *shannon_fano_encoding(new_keys, new_values, code + '1'))


def sf_cut(values: list[float]) -> int:
    con = [(sum(values[:i]), sum(values[i:])) for i in range(len(values))]
    a = min(con, key=lambda x: abs(x[0] - x[1]))
    '''Представляем суммы вероятностей всех срезов в виде кортежей (первый элемент - 0, второй - 1).
    Находит разницу вероятностей между 2-мя элементами каждого кортежа и берём минимальный'''

    current_summa = 0
    for i in range(len(values)):
        current_summa += values[i]
        if current_summa == a[0]:
            return i + 1


def encoding(pos: tuple[dict]) -> dict:  # Получаем из кортежа со словорями 1 единственный словарь
    j = {}
    for i in pos:
        j |= i  # Работает с python 3.9+
    return j


text, ln = count(input("Введите текст и посчитайте его вероятность: "))
list_with = veroyt((text))
entropy = calk_entropy(list_with)
print(text, ln)
print(list_with)
print(entropy)