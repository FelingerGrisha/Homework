file_for_read = open("task1.txt", "r")
numbers = file_for_read.readlines()

file_for_read.close()

file_for_write = open("output1.txt", "w")
len_of_numbers = len(numbers)



for i in range(len_of_numbers):

    try:
        numbers[i] = numbers[i].strip()
    except:
        print("В файле должны быть записаны только числа")
        exit()

    for j in range(len_of_numbers):
        for k in range(len_of_numbers):
            first_term = int(numbers[i])
            second_term = int(numbers[j])
            third_term = int(numbers[k])
            sum = first_term + second_term + third_term
            print(f'{first_term} + {second_term} + {third_term} = {sum}')
            if(sum == 2020):
                file_for_write.write(f'{first_term} * {second_term} * {third_term} = {first_term * second_term * third_term}')
                file_for_write.close()
                exit()

else:
    print("В вашем файле не обнаружено сочетаний трёх чисел сумма кототых давала бы 2020")
