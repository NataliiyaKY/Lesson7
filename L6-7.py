'''Пользователь вводит текст нужно вывести количество цифр в этом тексте'''

A = input('введите текст с цифрами: ').split()
count = 0
for i in A:
    for m in i:
        if m.isdigit():
            count += 1
print(f'вы ввели {count} цифр')
