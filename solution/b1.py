'''
Enter any 2 natural numbers, use the operators to output the number with the largest and smallest result

+ Input: 2, 7
     + calculation for the largest number : 2+7 (example)
     + calculation for the smallest number: 2/7 (still an example)
'''
import random, os
from pathlib import Path

def solution(num1, num2):
    # used for scan
    arr_scan = [
        num1 + num2,
        num1 - num2,
        num1 * num2,
        num1 / num2,
        # revert
        num2 + num1,
        num2 - num1,
        num2 * num1,
        num2 / num1,
    ]
    # find max
    num_max = arr_scan[0]
    for i in arr_scan[1:]:
        if i > num_max:
            num_max = i

    # find min
    num_min = arr_scan[0]
    for j in arr_scan[1:]:
        if j < num_min:
            num_min = j

    return num_max, num_min

def write_txt(data,filename,type):
    """ write_txt

    Args:
        data: du lieu ghi vao txt
        filename: ten file
        type: input hay output
    """
    file_name = Path(__file__).resolve().parent.parent.joinpath(f"test_case/b1/{type}/{filename}.txt")

    # Open the file in write mode and write the data to it
    with open(file_name, 'w') as file:
        file.write(data)

def make_test_case():
    counter = 1
    while counter < 100:
        if counter < 3:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        else:
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 10000)
        num_max, num_min = solution(num1,num2)

        data_input = f"{num1}\n{num2}\n"
        data_output = f"{num_max} {num_min}\n"

        file_name_input = f"input{counter}"
        file_name_output = f"output{counter}"

        write_txt(data_input,file_name_input,'input')
        write_txt(data_output,file_name_output,'output')
        counter+=1

if __name__ == '__main__':
    
    # num1 = int(input())
    # num2 = int(input())

    # try:
    #     max_res, min_res = solution(num1, num2)
    # except Exception as exc:
    #     print('Exception: \n',exc)
    # else:
    #     print(max_res,min_res)


    # make test case
    make_test_case()
