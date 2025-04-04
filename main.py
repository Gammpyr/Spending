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
    0: [],
}
category_code = {
    1: "ГСМ",
    2: "Ремонт Газели",
    3: "З/П",
    4: "Дивиденды",
    5: "Аренда",
    6: "Доставка",
    0: "Прочее"
}

month = input('Введите месяц: ').title()


@print_generator
def help_info():
    """Выводит информацию о категориях расходов"""
    for number, category in category_code.items():
        print(f'{number} - {category}')


@print_generator
def get_user_input():
    """Получает информацию и создаёт словарь с расходами по каждой категории"""
    while True:
        user_key = input('Ввод катег')  # нужен int
        if user_key.lower() in ['q', 'й']:
            break
        elif user_key.lower() in ['?', 'h', 'help', 'п', 'помощь']:
            help_info(category_code)
        else:
            user_value = int(input('Ввод суммы'))
            spending[int(user_key)].append(user_value)


@print_generator
def write_result():
    """Записывает результат в data/название_месяца.txt """
    with open(f'data/{month}.txt', 'w', encoding='UTF-8') as file:
        print(month)
        file.write(f'{month.upper()}\n')
        for key, value in spending.items():
            print(f'{category_code[key].ljust(13)} - {sum(value)}')
            file.write(f'{category_code[key].ljust(13)} - {sum(value)}\n')


if __name__ == '__main__':
    help_info()
    get_user_input()
    write_result()
