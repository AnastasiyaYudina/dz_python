# Задача 10 
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n=int(input('Введите количество монеток: '))
# from random import randint
# x=y=0

# for i in range(n):
#    a=randint(0,1)
#    print(a, end='')
#    if a>0: x+=1
#    else: y+=1
# print()
# if x>y:
#    print(f'Нужно перевернуть {y} монеток')
# else: print(f'Нужно перевернуть {x} монеток')


# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# # Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# # а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# # Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S=int(input('Введите сумму заданных чисел '))
# P=int(input('Ввведите прозведение заданных чисел '))
# for x in range (1000):
#    for y in range(1000):
#       if S==x+y and P==x*y:
#          print(x,y)

# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

# N=int(input('Введите заданное число N:'))
# i=0
# while 2**i<N:   
#  print(2**i)
#  i+=1



