from random import randint
field = []  # 'ue' - untouched and empty, 'op' - open, 'fb' - flag with no bomb, 'ub' - untouched with bomb,
# 'f' - flagged with bomb
user_field = []

f = open('save.txt', 'r')

saved = f.read()

contin = input('Открыть сохранённую игру? y/n ')

j = 0

if contin == 'n' or len(saved) == 0:
    if len(saved) == 0 and contin != 'n':
        print('Сохранённых игр нет')
    n, m = int(input('Введите размер по вертикали: ')), int(input('Введите размер по горизонтали: '))
    bomb_num = -1
    while not(0 < bomb_num <= n * m):
        bomb_num = int(input('Введите кол-во бомб: '))

    oc = 0
    win_num_oc = n * m - bomb_num
    for i in range(n):  # setting up the field
        field.append(['ue'] * m)
        user_field.append(['*'] * m)

    for i in range(bomb_num):  # putting bombs
        rand_x, rand_y = randint(0, n - 1), randint(0, m - 1)
        while field[rand_x][rand_y] != 'ue':
            rand_x, rand_y = randint(0, n - 1), randint(0, m - 1)
        field[rand_x][rand_y] = 'ub'
else:
    saved = saved.split('\n')
    n, m = int(saved[0].split()[0]), int(saved[0].split()[-1])


def print_field(fld):
    for i in range(len(fld)):
        print(*fld[i], sep=' ')


def bombs_around(fld, x, y):  # counts the number of bombs in surrounding cells
    num = 0
    up_bx = len(fld) - 1
    up_by = len(fld[0]) - 1

    if x > 0:
        if fld[x - 1][y] == 'ub':
            num += 1
    if y > 0:
        if fld[x][y - 1] == 'ub':
            num += 1
    if x > 0 and y > 0:
        if fld[x - 1][y - 1] == 'ub':
            num += 1

    if x < up_bx:
        if fld[x + 1][y] == 'ub':
            num += 1
    if y < up_by:
        if fld[x][y + 1] == 'ub':
            num += 1
    if x < up_bx and y < up_by:
        if fld[x + 1][y + 1] == 'ub':
            num += 1

    if x < up_bx and y > 0:
        if fld[x + 1][y - 1] == 'ub':
            num += 1
    if x > 0 and y < up_by:
        if fld[x - 1][y + 1] == 'ub':
            num += 1

    return num


while j < m * n:
    try:
        x, y, flag = input().split()
        x, y = int(x) - 1, int(y) - 1
        state = field[x][y]
        if flag == 'Flag':
            if state == 'ub':
                field[x][y] = 'f'
            if state == 'ue':
                field[x][y] = 'fb'
            user_field[x][y] = 'f'
        if flag == 'Open':
            if state == 'ue':
                field[x][y] = 'op'  # count bombs
                user_field[x][y] = bombs_around(field, x, y)
                oc += 1
                if oc == win_num_oc:
                    print_field(user_field)
                    print('You won!!!!!')
                    break
            if state == 'ub':
                print('Oh nooo!!!!! It was a bomb X-(')
                break
        print_field(user_field)
        j += 1
    except Exception:
        print('Incorrect format')

print("Hope you enjoyed the game!")
