def s_list(a, n):
    n %= len(a)
    return a[-n:] + a[:-n]


if __name__ == "__main__":
    from one1 import input_list
    print(s_list(input_list(), int(input("Введите число сдвига: "))))
