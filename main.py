# librarys
import warnings
import math

import universal
import db
import exel

# ignoring log level warning
warnings.filterwarnings("ignore")

# input kords of two points -> distance between it
def dist_1():
    point_1 = input('Point 1(x1, y1): ').split()
    point_2 = input('Point 2(x2, y2): ').split()
    if point_1[0].isdigit() and point_2[0].isdigit() and point_1[1].isdigit() and point_2[1].isdigit():
        point_1 = list(map(int, point_1))
        point_2 = list(map(int, point_2))
        dist = round(math.sqrt((point_1[0] + point_2[0]) ** 2 + (point_1[1] + point_2[1]) ** 2), 5)
        print(dist)
        db.save_result('distance', dist)
    else:
        print('Ошибка')
    return

# input lits of num -> min and max values of list
def minmax():
    list_1 = input('List: ').split()
    try: 
        list_1 = list(map(int, list_1))
        print(max(list_1), min(list_1))
        db.save_result('min, max', str(max(list_1)) + ' ' + str(min(list_1)) )
    except BaseException:
        print('Ошибка')
    return

# main console menu
def main():
    db.check_db()
    run = True
    commands = """==========================================================================
1. Вычисление расстояния между этими точками, сохранение и вывод из MySQL.
2. Создание множества и словаря в Python, сохранение и вывод из MySQL.
3. Определить минимальное и максимальное значения, сохранение и вывод из MySQL. 4. Сохранить данные из MySQL в Excel и вывести на экран.
4. Завершить"""
    while run:
        run = universal.uni(commands, 
                      dist_1, minmax,
                      db.print_db, db.save_db_to_xlxs, exel.print_exel)
    return

if __name__ == '__main__':
    main()