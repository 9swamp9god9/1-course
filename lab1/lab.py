# 1

n = int(input('Введите число: '))
if n > 0:
    for i in range(n):
        print(i + 1)
else:
    for i in range(2, n, -1):
        print(i - 1)

# 2
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
if n1 > n2:
    print('Большее число: ', n1)
elif n1 == n2:
    print("4isla ravny")
else:
    print('Большее число: ', n2)
