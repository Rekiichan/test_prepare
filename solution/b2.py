'''
    Have a list of employees:
    danh_sach_nhan_vien  = [
        {
            'name' : 'Thảo',
            'age' : 30
        },
        {
            'name' : 'Tam',
            'age' : 19
        },
        {
            'name' : 'Lan',
            'age' : 23
        },
        {
            'name' : 'Thành',
            'age' : 25
        },
        {
            'name' : 'Thái',
            'age' : 20
        }
    ]

    1. Declare that list and write a function that returns names of employees sorted 
    by age from smallest to largest and finds the oldest employee.
    2. Input x, find the distance between the person whose age is older 
    than the age of x other people and the age of the person whose age 
    is younger than the age of x others (x is less than the length of the list)
'''
danh_sach_nhan_vien  = [
	{
		'name' : 'Thao',
		'age' : 30
	},
	{
		'name' : 'Tam',
		'age' : 19
	},
	{
		'name' : 'Lan',
		'age' : 23
	},
	{
		'name' : 'Thanh',
		'age' : 25
	},
	{
		'name' : 'Thai',
		'age' : 20
	}
]


def giai_toan(list_data):
    danh_sach_nhan_vien_sorted = sorted(list_data, key=lambda x: x['age'], reverse=False)
    nhan_vien_lon_nhat = danh_sach_nhan_vien_sorted[-1]['name']

    for human in danh_sach_nhan_vien_sorted:
        print(human['name'],end=' ')
    print(f'\n{nhan_vien_lon_nhat}')

    return danh_sach_nhan_vien_sorted

x = int(input())
danh_sach_nhan_vien_sorted = giai_toan(danh_sach_nhan_vien) 
khoang_cach_tuoi = abs(danh_sach_nhan_vien_sorted[-x-1].get('age') - danh_sach_nhan_vien_sorted[x].get('age'))
print(khoang_cach_tuoi)



