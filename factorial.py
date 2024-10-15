n = int(input('Введите натуральное число не более 100'))

if n <1 or n > 100:
    print('Не верно введено число')
else:
    p = 1
    for i in range(1, n+1):
        p *= i

    print(f'Факториал {n}! = {p}')

# LAST MESSAGE 2