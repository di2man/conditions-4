a = list(map(int,input('Введите ряд чисел через пробел: ').split()))
b = int(input('Введите число для поиска: '))
k = 0
for i in a:
    if i==b:
        k+=1
