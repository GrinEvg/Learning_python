# if
a = 10
if a > 5:
    print(a)

# if - else
a = int(input())
if a > 5:
    print('big num')
else:
    print('small num')

# if - elif - else
a = 10
if a < 5:
    print('small num')
elif a <= 10:
    print('aver num')
else:
    print('big num')

# комбинорование условий и использование в функциях


def number_est(a):
    if a < 5:
        return 'small num'
    elif a < 10:
        return 'aver num'
    else:
        return 'big num'


print(number_est(2))
print(number_est(8))
print(number_est(15))

a = 10
b = 101
c = 50
if a > 5 and b > 100 and c > 55:  # можно использовать or и прочее.  and имеет приоритет над or
    print('all big')
else:
    print('ok')

# Что такое тернарный оператор (оператор в одну строчку) и the Anti-IF Campaign


def pow(a, n):
    return a ** n if n else a

# раннее прерывание


def check_shop_is_opened(shop):
    if (shop):
        return True


def check_is_unit_in_shop(unit, shop):
    if shop and unit:
        return True


def check_customer_can_afford_init(unit, customer):
    if unit and customer:
        return True


shop = 'магазин 1'
unit = 'компьютер'
custumer = 'Вася'


def make_purchase():  # это плохой код
    if check_shop_is_opened(shop):
        if check_is_unit_in_shop(unit, shop):
            if check_customer_can_afford_init(unit, custumer):
                return 'buy is OK'
            else:
                raise Exception('No money')
        else:
            raise Exception('No product in shop')
    else:
        raise Exception('shop is closed')


def make_purchase():  # это хороший код (проверяем на False)
    if not check_shop_is_opened(shop):
        raise Exception('shop is closed')
    if not check_is_unit_in_shop(unit, shop):
        raise Exception('No product in shop')
    if not check_customer_can_afford_init(unit, custumer):
        raise Exception('No money')
    return 'buy is OK'

 