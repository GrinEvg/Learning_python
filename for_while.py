# while работает пока условие в цикле соблюдается

i = 0
while i < 15:
    print(i)
    i += 1

is_num_big = True
a = 10000
while is_num_big:
    a /= 2
    if a < 100:
        is_num_big = False
        
print(a)


arr = [1,2,3]
while arr:
    print(arr.pop(0))
    
    
arr = [1, 2, 3, 4, 5] # пока элементы есть - работает
for el in arr:
    print (el)
    
for i, el in enumerate(arr):
    print(i, el)
    
    
# continue
arr = [1, 2, 3, 4, 5, 'str', 6,7,8]
for el in arr:
    if not isinstance(el, int): # проверяем пренадлежность типу
        continue
    print(el ** 2)
    
    # break
    
arr = [1, 2, 3, 4, 5, 'str', 6,7,8]
for el in arr:
    if not isinstance(el, int): # проверяем пренадлежность типу
        print('мусор')
        break
    print(el ** 2)
    
i = 0
while True:
    i +=1
    if i == 10:
        break
    
# else работает, когда цикл завершается сам.  если break,return то не срабатывает

