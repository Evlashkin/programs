"""
Задача
Разработать программу для вычисления кратчайшего пути для почтальона.

Описание задачи
Почтальон выходит из почтового отделения, объезжает всех адресатов один
раз для вручения посылки и возвращается в почтовое отделение.

Необходимо найти кратчайший маршрут для почтальона.

Координаты точек
Почтовое отделение – (0, 2)
Ул. Грибоедова, 104/25 – (2, 5)
Ул. Бейкер стрит, 221б – (5, 2)
Ул. Большая Садовая, 302-бис – (6, 6)
Вечнозелёная Аллея, 742 – (8, 3)
"""

post_dict = {"point_1": "Почтовое отделение",
             "point_2": "Ул. Грибоедова, 104/25",
             "point_3": "Ул. Бейкер стрит, 221б",
             "point_4": "Ул. Большая Садовая, 302-бис",
             "point_5": "Вечнозелёная Аллея, 742"}

point_dict = {"point_1": (0, 2),
              "point_2": (2, 5),
              "point_3": (5, 2),
              "point_4": (6, 6),
              "point_5": (8, 3)}


def distance_func(point_1, point_2):
    """
    Функция для расчета дистанции между двумя точками
    :param point_1: tuple (Координаты первого адреса)
    :param point_2: tuple (Координаты следующего адреса)
    :return: int (Расстояние между адресами)
    """
    distance = (((point_2[0]) - (point_1[0])) ** 2 + ((point_2[1]) - (point_1[1])) ** 2) ** 0.5
    return distance


def all_dist_func():
    """
    Функция для расчета всех дистанций между каждыми точками
    :return: list (Возвращает список с кортежами,
    которые включают в себя точки, между которыми произовдился
    расчет растояния, и численное
    отображение расстояния между этими точками.)
    """

    all_dist_list = []
    f = 1
    while f != len(point_dict) + 1:
        s = 2
        while s != len(point_dict) + 1:
            if f < s:
                dist = ((distance_func(point_dict[f"point_{f}"], point_dict[f"point_{s}"])), (f, s))
                all_dist_list.append(dist)
            s += 1
        f += 1
    return all_dist_list


def heuristic_method():
    """
    Функция для поиска оптимального маршрута методом ближайшего соседа
    :return: None
    """
    my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    all_dist = all_dist_func()
    all_dist_list = all_dist_func()
    first = [item for item in all_dist_list if 1 in item[1]]
    first.sort()
    all_dist_list = (set(all_dist_list) - set(first))
    first = first[0]

    num = first[1][1]
    second = [item for item in all_dist_list if num in item[1]]
    second.sort()
    all_dist_list -= set(second)
    second = second[0]

    num = second[1][1]
    third = [item for item in all_dist_list if num in item[1]]
    third.sort()
    all_dist_list -= set(third)
    third = third[0]

    num = third[1][1]
    fourth = [item for item in all_dist_list if num in item[1]]
    fourth.sort()
    all_dist_list -= set(fourth)
    fourth = fourth[0]

    my_list.remove(first[1][0])
    my_list.remove(first[1][1])
    my_list.remove(second[1][0])
    my_list.remove(second[1][1])
    my_list.remove(third[1][0])
    my_list.remove(third[1][1])
    my_list.remove(fourth[1][0])
    my_list.remove(fourth[1][1])
    my_list = tuple(my_list)

    fifth = [item for item in all_dist if my_list in item]
    fifth = fifth[0]

    a = first[0]
    b = a + second[0]
    c = b + third[0]
    d = c + fourth[0]
    e = d + fifth[0]

    print(f"{first[1]}({a}) -> {second[1]}({b}) -> {third[1]}({c}) -> {fourth[1]}({d}) -> {fifth[1]}({e}) = {e}")
    print(f"""Где:
1 - {post_dict["point_1"]}
2 - {post_dict["point_2"]}
3 - {post_dict["point_3"]}
4 - {post_dict["point_4"]}
5 - {post_dict["point_5"]}
""")


heuristic_method()
