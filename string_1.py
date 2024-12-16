surname = 'Grin'
name = 'Evg'
nickname = surname + name
num = 10
num_str = str(10)
print(nickname)
print(num_str + 'abn')
# изучаю print
print(len(nickname))  # длина строки
print('''привет!
пока''')  # перевод строки
print('привет!\nпока')  # перенос строки \n
print(surname, name, sep="")  # тип разделителя между словами sep="..."
bundle = "персональный"
days = 365
# подставление значений с помощью .format
print('{0},{1},{2}'.format(name, days, bundle))
print(f'My name is {name}, my tariff is "{bundle}"')  # f строки
# функция удаления пробелов (метод strip)
whitespace = "   897   x"
print(whitespace.strip())
print(whitespace)
# разбивка и объеденение .split and .join
keywords = 'python, анализ данных, программирование, ура'
print(keywords.split(', '))  # получаем список можно по абзацам через \n
arr = ['python', 'анализ данных', 'программирование', 'ура']
print('.\n'.join(arr))  # oбъеденяем через .join
# регистры букв
word = 'Hello'
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.islower())  # проверка регистра
# проверка строк на определенные символы
s1 = "Обычное"
s2 = "Обычное!"
print(s1.endswith('!'))
print(s2.endswith('!'))
print(s1.startswith('Обычное'))
print(s2.startswith('Обычное'))
# поиск внутри
s_long = 'Длинная строка с некоторым текстом'
print(s_long.find('некоторым'))  # равно 17. с этой позиции начинается слово.
print('некоторым' in s_long)  # проверка слова в строке
s_long = s_long.replace('Длинная', '!!!!!')  # замена слова
print(s_long)
print(s_long[2:8])