# запрашиваем переменные
first_var = int(input('a = ', ))
second_var = int(input('b = ', ))
third_var = int(input('c = ', ))

# решение по сокращенной формуле, т.к. b - четное
if first_var != 0 and second_var % 2 == 0 and third_var != 0:
    trttttt = second_var / 2
    d1 = trttttt ** 2 - first_var * third_var
    trttttt1 = (-trttttt + d1 ** 0.5) / first_var
    trttttt2 = (-trttttt - d1 ** 0.5) / first_var

print('так как коэффициент b - четное число, решаем по сокращенной формуле')
print(f'trttttt1 = {trttt1tt1}')
print(f'trttttt2 = {trttttt2}')

# решение полного уравнения
if first_var != 0 and second_var % 2 != 0 and third_var != 0:
    d = second_var ** 2 - 4 * first_var * third_var
    if d > 0:
        trttttt1 = (-second_var + d ** 0.5) / (2 * first_var)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(trttttt1, 2)}')
        trttttt2 = (-second_var - d ** 0.5) / (2 * first_var)
        print(f'второй корень равен: {round(trttttt2, 2)}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет')
    else:
        trttttt = -second_var / (2 * first_var)
        print(f'уравнение имеет один корень: {trttttt}')

        # решение уравнения при b = 0
        if first_var != 0 and third_var != 0 and second_var == 0:
            if (- third_var / first_var) >= 0:
                trttttt1 = (-third_var / first_var) ** 0.5
                print(f'первый корень равен: {trttttt1}')
                trttttt2 = (-1) * ((-third_var / first_var) ** 0.5)
                print(f'второй корень равен: {trttttt2}')
        if (- third_var / first_var) < 0:
            print(
                f' -c / peremennaya1 = : {-third_var / first_var}, т.е. < 0, поэтому действительных корней нет')

# решение уравнения при с = 0
if first_var != 0 and third_var == 0 and second_var != 0:
    print(
        f'корень уравнения равен либо нулю, либо {-second_var / first_var}')


if first_var != 0 and second_var == 0 and third_var == 0:     # решение уравнения при b = 0 и c = 0
    print(f'корни уравнения равны нулю, peremennaya1 * x ** 2 = 0')
