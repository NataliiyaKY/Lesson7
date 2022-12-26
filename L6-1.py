'''Запросить у пользователя 5 чисел и записать их в список'''

a = list(map(int,input('введите 5 чисел: ').split()))
print(a)
print(type(a))