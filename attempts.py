def place_for_bombs_around(fld, x, y):
    num = 0
    up_bx = len(fld) - 1
    up_by = len(fld[0]) - 1

    if x > 0:
        if fld[x - 1][y] == '*':
            num += 1
    if y > 0:
        if fld[x][y - 1] == '*':
            num += 1
    if x > 0 and y > 0:
        if fld[x - 1][y - 1] == '*':
            num += 1

    if x < up_bx:
        if fld[x + 1][y] == '*':
            num += 1
    if y < up_by:
        if fld[x][y + 1] == '*':
            num += 1
    if x < up_bx and y < up_by:
        if fld[x + 1][y + 1] == '*':
            num += 1

    if x < up_bx and y > 0:
        if fld[x + 1][y - 1] == '*':
            num += 1
    if x > 0 and y < up_by:
        if fld[x - 1][y + 1] == '*':
            num += 1

    return num


def change_cells_around(fld, x, y, val):
    up_bx = len(fld) - 1
    up_by = len(fld[0]) - 1

    if x > 0:
        fld[x - 1][y] = val
    if y > 0:
        fld[x][y - 1] = val
    if x > 0 and y > 0:
        fld[x - 1][y - 1] = val

    if x < up_bx:
        fld[x + 1][y] = val
    if y < up_by:
        fld[x][y + 1] = val
    if x < up_bx and y < up_by:
        fld[x + 1][y + 1] = val

    if x < up_bx and y > 0:
        fld[x + 1][y - 1] = val
    if x > 0 and y < up_by:
        fld[x - 1][y + 1] = val


def set_free_cells_around(fld, x, y, val):
    up_bx = len(fld) - 1
    up_by = len(fld[0]) - 1

    if x > 0:
        fld[x - 1][y] = val
    if y > 0:
        fld[x][y - 1] = val
    if x > 0 and y > 0:
        fld[x - 1][y - 1] = val

    if x < up_bx:
        fld[x + 1][y] = val
    if y < up_by:
        fld[x][y + 1] = val
    if x < up_bx and y < up_by:
        fld[x + 1][y + 1] = val

    if x < up_bx and y > 0:
        fld[x + 1][y - 1] = val
    if x > 0 and y < up_by:
        fld[x - 1][y + 1] = val


def bombs_locator(field, n):
    mas = []
    for i in range(len(field)):
        mas.append([0] * len(field[0]))

    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y] != '*':
                if int(field[x][y]) == 0:
                    change_cells_around(mas, x, y, -1)
                if int(field[x][y]) == place_for_bombs_around(field, x, y):
                    set_free_cells_around(mas, x, y, 1.0)
                mas[x][y] = -1
            else:
                mas[x][y] = 0.5
    print(*mas, sep='\n')


line = '''0 0 2 * 3
0 0 2 * *
0 1 3 4 3
0 1 * * 1
0 1 2 2 1'''

line = '''* * 3 * *
* * * * *
* * * * *
* 2 * * *
2 * * * 0'''

fl = list(map(lambda y: y.split(), line.split('\n')))
print(fl)
bombs_locator(fl, 2)
