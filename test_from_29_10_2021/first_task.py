programm = open("input.txt", "r").read().strip()
programm = programm.split(",")

for i in range(len(programm)):
    if(programm[i].isdigit()):
        programm[i] = int(programm[i])
    else:
        print("Во входной файле была найдена ошибка, в файле должны содержаться только целые числа, разделённые запятой")
        exit(1)

i = 0

programm[1] = 12
programm[2] = 2

while i < len(programm):

    if(programm[i] == 1):
        programm[programm[i+3]] = programm[programm[i+1]] + programm[programm[i+2]]
        i+= 4

    if(programm[i] == 2):
        programm[programm[i+3]] = programm[programm[i+1]] * programm[programm[i+2]]
        i+= 4

    if(programm == 99):
        break

    i+= 1

print(programm)
