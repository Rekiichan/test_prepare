import random
from pathlib import Path

def get_time(list_input):
    height = 10
    ngay = 3
    dem = -2
    tt_xau_ngay = -10/100
    tt_xau_dem = -15/100

    ngay_count = 0
    dem_count = 0
    is_ngay = True
    sum = 0
    while True:
        index = dem_count
        dieu_kien = list_input[index] if index < len(list_input) else 1
        if is_ngay:
            s = ngay
            tt_xau = tt_xau_ngay if not dieu_kien else 0
            ngay_count += 1

        else:
            s = dem
            tt_xau = tt_xau_dem if not dieu_kien else 0
            dem_count += 1

        sum += s+s*tt_xau
        if sum >= height: break
        is_ngay = not is_ngay
    
    return ngay_count, dem_count

def write_txt(data,filename,type):
    """ write_txt

    Args:
        data: du lieu ghi vao txt
        filename: ten file
        type: input hay output
    """
    file_name = Path(__file__).resolve().parent.parent.joinpath(f"test_case/b3/{type}/{filename}.txt")
    print(Path(__file__).resolve().parent.parent.joinpath(f"test_case/b3/{type}/{filename}.txt"))
    # Open the file in write mode and write the data to it
    with open(file_name, 'w') as file:
        file.write(data)

def make_test_case():
    counter = 1
    while counter < 10:
        data_input = ''
        n = random.randint(10,20)
        data_input += f'{n}\n'

        arr = []
        for i in range(0,n):
            x = random.randint(0,1)
            data_input += f'{x}\n'
            arr.append(x)

        ngay_count, dem_count = get_time(arr)
        
        data_output = f"{ngay_count} {dem_count}"
        data_input += f'\n\n{data_output}'

        file_name_input = f"input{counter}"
        file_name_output = f"output{counter}"

        write_txt(data_input,file_name_input,'input')

        counter+=1


# make_test_case()
