file = open("input.txt", "r")
programm = file.read().strip()
programm = programm.split(",")

for i in range(len(programm)):
    if(programm[i].isdigit() and int(programm[i]) < len(programm)):
        programm[i] = int(programm[i])
    else:
        print("Во входном файле была найдена ошибка, в файле должны содержаться только целые числа от 0 до числа общего количества оп-кодов и их аргументов, разделённые запятой")
        exit(1)

i = 0

programm[1] = 12
programm[2] = 2

while i < len(programm):

    if(programm[i] == 1):
        
        programm[programm[i+3]] = programm[programm[i+1]] + programm[programm[i+2]]
        i+= 4
        continue

    if(programm[i] == 2):
        
        programm[programm[i+3]] = programm[programm[i+1]] * programm[programm[i+2]]
        i+= 4
        continue

    if(programm == 99):
        break

    i+= 1

file.close()

for i in range(len(programm)):
    programm[i] = str(programm[i])

programm = ",".join(programm)

file = open("input.txt", "w")
file.write(programm)
file.close()
