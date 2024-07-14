first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))
if first==second==third:
    print ("Количество одинаковых чисел = 3")
elif first==second or first==third or second==third:
    print ("Количество одинаковых чисел = 2")
else: print("Количество одинаковых чисел = 0")