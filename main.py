def print_generator(func):
    """Создаёт пробелы вокруг функции"""

    def wrapped():
        print()
        func()
        print()

    return wrapped


spending = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    0: [],
}
category_code = {
    1: "ГСМ",
    2: "Ремонт Газели",
    3: "З/П",
    4: "Дивиденды",
    5: "Аренда",
    6: "Доставка",
    7: "Поставщики",
    0: "Прочее"
}

month = input('\nВведите месяц: ').title()


@print_generator
def help_info():
    """Выводит информацию о категориях расходов"""
    for number, category in category_code.items():
        print(f'{number} - {category}')


@print_generator
def get_user_input():
    """Получает информацию и создаёт словарь с расходами по каждой категории"""
    while True:
        help_info()
        user_key = input('\nВвод категории: ')
        if user_key == '=':
            print_result()
            continue
        if not user_key.isdigit() and len(user_key) != 1:
            print("\nВведите код:")
            continue
        if user_key.lower() in ['q', 'й']:
            break
        elif user_key.lower() in ['?', 'h', 'help', 'п', 'помощь']:
            help_info()
        else:
            while True:
                user_value = input('Ввод суммы:     ')
                if user_value.isdigit():
                    spending[int(user_key)].append(int(user_value))
                    break
                else:
                    print('Введите сумму цифрами!')


@print_generator
def print_result():
    """Выводим результат"""
    print(month)
    for key, value in spending.items():
        print(f'{category_code[key].ljust(13)} - {sum(value)}')
    print(f'\nВсего:         - {get_summ()}')


def write_result_dict():
    """Записываем результат как словарь"""
    with open(f'data/{month}_dict.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{str(spending)}\n')
        for key, value in spending.items():
            file.write(f'{key} : {value}\n')


def write_result():
    """Записывает результат в data/название_месяца.txt """
    with open(f'data/{month}.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{month.upper()}\n')
        for key, value in spending.items():
            file.write(f'{category_code[key].ljust(13)} - {sum(value)}\n')
        file.write(f'\nВсего:         - {get_summ()}\n\n')


def get_summ():
    """Получаем итоговую сумму расходов"""
    result = 0
    for key, value in spending.items():
        result += sum(value)
    return result


if __name__ == '__main__':
    get_user_input()
    write_result()
    write_result_dict()
    print_result()