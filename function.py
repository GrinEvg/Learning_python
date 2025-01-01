# пример создания
def foo():
    print('Hello')


foo()


def foo2():
    print('Hello')
    print('Hello2')


foo2()


def pow():
    return 5**2  # возвращает функцию


a = pow()

# void функция. функция без return (например запись в лог)

# опреатор ничего не делать. допустим оставить место на потом для написания функции


def foo3():
    pass


def foo4():
    ...

# задание аргументов


def pow(x, n):
    return x ** n


pow(5, 3)

# аргументы по умолчанию, сначала без умолчания, потом аргументы с умолчанием


def pow(x, n=2):
    return x ** n

# контроль за именованыи аргументами


def s_f(a, b, *, c, d=10):  # после * именованые
    return a*b + c*d

 # args, kwargs
 # args - массив позиционных авргументов
 # kwargs  - словарь именнованных авргументов


def foo(*args, **kwargs):
    ...

# док функций/ пишется внутри функции


def pow(x, n=2):
    '''это пример'''
    return x ** n


pow.__doc__

# несколько знаЧ из функции


def process(data):
    flag = 1
    res = 10
    return flag, res
