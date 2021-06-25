import random

x = int(input("Введите номер хлеба: "))
i = 0

while random.randint(0, x + 100500) != x:
    i += 1

print("Плоскоземельная позиция сладкого хлеба:", i)
