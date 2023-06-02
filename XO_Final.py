#coding=UTF-8
#Порядок выполнения кода
#1 - Отрисовка поля
#2 - Расстановка символов
#3 - Определение выигрыша или ничьи
#4 - Взаимодействие между блоками
print("Это игра крестики - нолики.")

def win_code(f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0, 2, 1], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    point_line = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(point_line.intersection(set(p))) == 3:
            return True
    return False

field = [['-']*3 for _ in range(3)]

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def user_input(f):
    while True:
        place = input('Введите координаты: ').split()
        if len(place) != 2:#Если ввели больше 2-х координат
            print('Введите две координаты: ')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):#Если ввели буквы
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):#Если больше нужных
            print('Вышли из диапазона')
            continue
        if f[x][y] != '-':#Если не стоит "-"
            print('Клетка занята')
            continue
        break
    return x, y

def start_game(field):
    count = 0
    while True:
        if count % 2 == 0:
            user = 'X'
        else:
            user = '0'
        show_field(field)
        x, y = user_input(field)
        field[x][y] = user
        if count == 9:
            print('Ничья')
        if win_code(field, user):
            print(f'Победил {user}')
            show_field(field)
            break
        count += 1

start_game(field)



