# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его 
# стихах ритм. Поскольку разобраться в его кричалках не настолько 
# просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

#Решение 
# letters_gl=['а','я', 'у','ю','о','е','ё','э','и','ы']
# phrase=input('Введите стихотворение: ')
# list_word=phrase.lower().split()

# list_result = []
# for i in range(len(list_word)):
#    list_result.append(0)
#    for j in letters_gl:
#         list_result[i] += list_word[i].count(j)

# print("Количество гласных в словах:", list_result)
# # 
# # # find_ritm=map(lambda a: False if a[i] !=a[i + 1] else True, list_result)# черновик

# def find_ritm(characteristic, objects):
#     for i in range(len(list_result) - 1):
#         if(list_result[i]) !=(list_result[i + 1]):
#             return False
#     return True

# print("Парам пам-пам") if find_ritm(list_result, phrase) else print("Пам парам")



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую
# элемент по номеру строки и столбца. Аргументы num_rows и 
# num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и 
# столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1,num_rows+1):
#         print()
#         for j in range(1,num_columns+1):
#             print('''{:<5}'''.format(operation(i,j)),end='')

# print_operation_table(lambda x,y:x*y)