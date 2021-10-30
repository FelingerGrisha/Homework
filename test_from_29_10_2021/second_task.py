programm = open("input.txt", "r").read().strip()
programm = programm.split(",")

for i in range(len(programm)):
    if(programm[i].isdigit()):
        programm[i] = int(programm[i])
    else:
        print("Во входном файле была найдена ошибка, в файле должны содержаться только целые числа от 0, разделённые запятой")
        exit(1)


i = 0
number1 = 0
number2 = 0
previous_programm = programm

for number1 in range(len(programm)):
    for number2 in range(len(programm)):

        programm = previous_programm
        programm[1] = number1
        programm[2] = number2

        while i < len(programm):

            if (programm[i] == 1):

                programm[programm[i + 3]] = programm[programm[i + 1]] + programm[programm[i + 2]]
                i += 4

            if (programm[i] == 2):

                programm[programm[i + 3]] = programm[programm[i + 1]] * programm[programm[i + 2]]
                i += 4

            if (programm == 99):
                break

            i+=1

        if(programm[0] == 5290681):
            break



print(number1, number2)
