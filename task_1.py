# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
#
#  1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

while not (day := input('Введите номер дня недели: ')).isdigit():
    print('Введенное выражение должно быть целым числом')
week = {"1": "Понедельник", "2": "Вторник", "3": "Среда", "4": "Четверг", "5": "Пятница", "6": "Суббота", "7": "Воскресенье"}
if day in week.keys():
    print(week[day])
else:
    print("Нет такого дня")