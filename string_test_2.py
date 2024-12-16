# задание 1
number = 42
message = f'Ваше любимое число - {number}'
print(message)

# задание 2
name = 'Alice'
age = 25
message = 'Привет, меня зовут {} и мне {} лет.'.format(name, age)
print(message)

# задание 3
message = '            Привет, мир!           '
stripped_text = message.strip()
print(stripped_text)

# задание 4
message =  'apple,orange,banana'
fruits_list = message.split(',')
print (fruits_list)

# задание 5
message = 'HEllO, wORd!'
upper_case_text = message.upper()
lower_case_text = message.lower()
swapped_case_text = message.swapcase()

# задание 6
message = ['Hello', 'World', 'Python']
joined_string = ' '.join(message)
print(joined_string)

# задание 7
text = 'Программирование на Python - это весело и мощно!'
starts_with_programming = text.startswith('Программирование')
ends_with_powerful = text.endswith('мощно!')

# задание 8
# Задание строки для поиска
text = "это секретное сообщение: тайна, тайна и еще тайна"

# Определение секретного сообщения
secret_message = "тайна"

# Поиск первого вхождения секретного сообщения, начиная с 10-го символа
start = text[9:].find(secret_message)

# Корректировка индекса относительно начала строки text
start += 9

# задание 9
text = 'Python - замечательный язык программирования!'
segment = text[9:22]
print(segment)

# задание 10
text = 'Python - замечательный язык программирования!'
reversed_text = text[::-1]
print(reversed_text)

# задание 11
text = 'Python - замечательный язык программирования!'
old_substring = 'замечательный'
new_substring = 'удивительный'
modified_text = text.replace(old_substring, new_substring)
print(modified_text)