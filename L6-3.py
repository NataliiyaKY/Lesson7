'''Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N'''

A = list(map(int, input('введите 10 чисел: ').split()))
N = int(input('введите одно число: '))
print(f'число {N} повторяется {A.count(N)} раз')
