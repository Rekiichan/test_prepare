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

n = int(input())    
arr = []
for i in range(0,n):
    x = int(input())
    arr.append(x)

ngay_count, dem_count = get_time(arr)
print(ngay_count, dem_count)
