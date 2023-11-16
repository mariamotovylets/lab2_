"""
Умова задачі №1:
Напишіть програму виведення текстового варіанта шкільних оцінок:
1, 2, 3 (початковий рівень - initial level),
4, 5, 6 (середній рівень - average level),
7, 8, 9 (достатній рівень - sufficient level),
10, 11, 12 (високий рівень - high level).
Автор: Мотовилець Марія
"""
m = int(input("Enter mark: "))

if 1 <= m <= 3 :
    print("initial level")
elif m >= 4 and m <= 6:
    print("average level")
elif 7 <= m <= 9:
    print("sufficient level")
elif 10 <= m <= 12:
    print("high level")
else:
    print("no such assessment exists")
