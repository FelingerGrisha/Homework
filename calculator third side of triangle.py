import math

print("Введите длину 1 стороны треугольника: ")
side1 = float(input())
print("Введите длину 2 стороны треугольника: ")
side2 = float(input())
print("Введите величину угла между этими сторонами: ")
angle = math.radians(float(input()))

side3 = math.sqrt(side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * math.cos(angle))

print("Длина 3 стороны треугольника равна:", side3)
input()