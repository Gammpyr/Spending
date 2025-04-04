def help_info(code):
    """Выводит информацию о категориях расходов"""
    for number, category in code.items():
        print(f'{number} - {category}')


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
    0: "Прочее",
}

while True:
    user_input = input('Ввод: ')
    if user_input.lower() == 'q':
        break
    elif user_input.lower() in ['?', 'h', 'help', 'п', 'помощь']:
        help_info(category_code)
    else:
        split_input = user_input.split()
        user_key = int(split_input[0])
        user_value = int(split_input[1])
        spending[user_key].append(user_value)

print()

with open('data/spending.txt', 'w', encoding='UTF-8') as file:
    for key, value in spending.items():
        print(f'{category_code[key]} - {sum(value)}')
        file.write(f'{category_code[key]} - {sum(value)}\n')
print()
