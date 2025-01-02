# test 1 Найдите площадь комнаты
from math import ceil


def renovation(length, width):
    return length * width


# test 2 Найдите количество упаковок плитки


def renovation(length, width, s_tile=0.04, tile_per_pack=1):
    s_room = length * width
    s_pack = s_tile * tile_per_pack
    count_pack = ceil(s_room / s_pack)
    return count_pack


# test 3 Добавляем цены


def renovation(length, width, price_per_pack, s_tile=0.04, tile_per_pack=1):
    s_room = length * width
    s_pack = s_tile * tile_per_pack
    count_pack = ceil(s_room / s_pack)
    min_price = min(price_per_pack)
    price = count_pack * min_price
    return price

# test 4 Проверьте число на четность
def parity_check(num_day, s_room):
    test_day = num_day % 2 
    test_room = s_room % 2 
    return test_day == test_room

# test 5 Среднее количество времени
def stats(time):
    all_time = sum(time)
    average_time = all_time / len(time)
    max_time = max(time)
    min_time = min(time)
    result = f'Среднее время в день: {round(average_time,1)}, Всего времени: {all_time}, Максимальное время: {max_time}, Минимальное время: {min_time}.'
    return result