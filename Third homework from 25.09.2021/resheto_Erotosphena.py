n = input("Введите число до которого включительно, вы бы хотели получить простые числа: ").strip()

n = n.split(" ")
n = ("").join(n)

while not n.isnumeric():

    print("При вводе числа вы допустили ошибку, введите число без пробелов, без букв и прочих символов ")

    n = input("Введите число до которого включительно, вы бы хотели получить простые числа: ").strip()

    n = n.split(" ")
    n = ("").join(n)

else:
    n = int(n)

resheto_Erotosphena = list(range(n + 1))[2:]
p = 2

while n >= (p ** 2):

    i = resheto_Erotosphena.index(p) + 1

    while i != len(resheto_Erotosphena):

        if (resheto_Erotosphena[i] % p == 0):
            del resheto_Erotosphena[i]
            i -= 1

        i += 1

    p = resheto_Erotosphena[resheto_Erotosphena.index(p) + 1]

print(resheto_Erotosphena)

input()