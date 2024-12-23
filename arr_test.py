# 1 задание посчитать стоимость всех билетов
price_rub = 260
count_ticket = 9
discount = 0.25  # скидка 25%
number_discount = 3  # скидка на каждый третий билет
# количество скидочных билетов
count_discount_ticket = count_ticket // number_discount
total_sum = (count_ticket - count_discount_ticket) * 260 + \
    count_discount_ticket * (260 * (1-discount))
print(total_sum)

# 2 задание перевести секунды в часы, минуты, секунды
time_sec = 20618
hours = time_sec // 3600
minutes = time_sec // 60 - hours * 60
seconds = time_sec - hours * 3600 - minutes * 60

# 3 Найти вершину параболы ax**2+bx+c
a = 2
b = -2
c = -4
x = -b/2*a
y = a * x ** 2 + b * x + c

# 4 Найти стоимость текста
Symbol_price = 80  # копейки
text = 'Python — это высокоуровневый язык программирования, который часто используют для разработки веб-приложений, научных вычислений и автоматизации задач. Он отличается простым и понятным синтаксисом, что делает его популярным выбором среди начинающих и опытных программистов.'
Symbol_count = len(text)
sum_rub = (Symbol_count * Symbol_price) // 100  # рубли
sum_kop = (Symbol_count * Symbol_price) % 100  # копейки

# 5 Определите, сколько времени коллеги проводят за компьютером

# задаем количтество часов по дням
Misha = {
    'Пн': 7,
    'Вт': 6,
    'Ср': 7,
    'Чт': 5,
    'Пт': 10
}
Alina = {
    'Пн': 8,
    'Вт': 7,
    'Ср': 8,
    'Чт': 4,
    'Пт': 8
}
Sasha = {
    'Пн': 5,
    'Вт': 4,
    'Ср': 5,
    'Чт': 6,
    'Пт': 9
}

time_Misha = (Misha['Пн'] + Misha['Вт'] + Misha['Ср'] +
              Misha['Чт'] + Misha['Пт']) / 5
time_Alina = (Alina['Пн'] + Alina['Вт'] + Alina['Ср'] +
              Alina['Чт'] + Alina['Пт']) / 5
time_Sasha = (Sasha['Пн'] + Sasha['Вт'] + Sasha['Ср'] +
              Sasha['Чт'] + Sasha['Пт']) / 5
time_total = round(((time_Alina + time_Misha + time_Sasha) / 3), 1)

# второй вариант решения (из учебника)
# задаем количтество часов по дням
list_Misha = [7, 6, 7, 5, 10]
list_Alina = [8, 7, 8, 4, 8]
list_Sasha = [5, 4, 5, 6, 9]

# среднее количество времени, которое Миша проводит за компьютером
time_Misha = sum(list_Misha) / len(list_Misha)
# среднее количество времени, которое Алина проводит за компьютером
time_Alina = sum(list_Alina) / len(list_Alina)
# среднее количество времени, которое Саша проводит за компьютером
time_Sasha = sum(list_Sasha) / len(list_Sasha)
# время, которое все сотрудники в среднем проводят за компьютером
time_total = (sum(list_Misha) + sum(list_Alina) + sum(list_Sasha)) / \
    (len(list_Misha) + len(list_Alina) + len(list_Sasha))

# 6 Рассчитайте код от сейфа
code_mirror = '93849276291784'
secret = code_mirror[::-1]

# 7 количество Орлов и Решек
punch_result = 'OPPOPPOOPOPOOPPOOP'
orel_count = punch_result.count('O')
reshka_count = punch_result.count('P')
difference = reshka_count - orel_count