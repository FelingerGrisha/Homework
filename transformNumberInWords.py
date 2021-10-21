print("Введите целое число от 0 до 99: ")

number = input().strip()
number_as_words = ""

if(number.isnumeric()) and (int(number) <= 99):

    number_as_words = number

    if number == "0":
        number_as_words = number_as_words.replace("0", " ноль")

    if "1" in number_as_words:
        number_as_words = number_as_words.replace("1", "один ")

    if "2" in number_as_words:
        number_as_words = number_as_words.replace("2", "два ")

    if "3" in number_as_words:
        number_as_words = number_as_words.replace("3", "три ")

    if "4" in number_as_words:
        number_as_words = number_as_words.replace("4", "четыре ")

    if "5" in number_as_words:
        number_as_words = number_as_words.replace("5", "пять ")

    if "6" in number_as_words:
        number_as_words = number_as_words.replace("6", "шесть ")

    if "7" in number_as_words:
        number_as_words = number_as_words.replace("7", "семь ")

    if "8" in number_as_words:
        number_as_words = number_as_words.replace("8", "восемь ")

    if "9" in number_as_words:
        number_as_words = number_as_words.replace("9", "девять ")

    number_as_words = number_as_words[0:-1]

    if number == "10":
        number_as_words = "десять"

    elif number == "12":
        number_as_words = "двенадцать"

    elif number == "14":
        number_as_words = "четырнадцать"

    elif number[0] == "1" and len(number) == 2:
        number_as_words = number_as_words.replace("один ", "")
        number_as_words = number_as_words.replace("ь", "") + "надцать"

    elif int(number) < 40 and len(number) == 2:
        number_as_words = number_as_words.replace(" ", "дцать ")

    elif number[0] == "4" and len(number) == 2:
        number_as_words = number_as_words.replace("четыре ", "сорок ")

    elif int(number) < 90 and len(number) == 2:
        number_as_words = number_as_words.replace(" ", "десят ")

    elif number[0] == "9" and len(number) == 2:
        number_as_words = number_as_words.replace("девять ", "девяносто ")

    print(number_as_words)


else:
    print("При вводе числа у вас была ошибка, нужно было ввести целое число от 0 до 99")
    input()
    exit(1)

input()