from HW.Data.date import Date

def main():
    date = Date()
    while True:
        print("1. Ввести дату")
        print("2. Вывести дату")
        choice = input("Введите ваш выбор: ")
        if choice == '1':
            date.input_date()
        elif choice == '2':
            print(date)
            print()
main()