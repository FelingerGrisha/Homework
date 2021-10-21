print("Введите числа наибольший общий делитель которых вы хотите найти:")

number1 = input().strip()
number2 = input().strip()

number1 = number1.split(" ")
number2 = number2.split(" ")

number1 = ("").join(number1)
number2 = ("").join(number2)

while (not number1.isnumeric()) or (not number2.isnumeric()):

    print("При вводе вы допустили ошибку, введите два числа без пробелов, без букв, "
          "а также после того как введёте первое число нажмите ENTER, а потом введите второе")

    number1 = input().strip()
    number2 = input().strip()

    number1 = number1.split(" ")
    number2 = number2.split(" ")

    number1 = ("").join(number1)
    number2 = ("").join(number2)

else:
    number1 = int(number1)
    number2 = int(number2)

NOD = 0
i = 1

while i <= min(number1, number2):

     if(number1 % i == 0 and number2 % i == 0):
         NOD = max(NOD, i)
     i += 1


print(f"Наибольший общий делитель чисел {number1} и {number2} = {NOD}")

input()