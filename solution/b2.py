"""
have a list of employees:
emp_list  = [
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
  1. Please write a function that returns a list of employees sorted by age from 
  smallest to largest and finds the oldest employee.
  
  2. Input x, find the distance between the person whose age is older than the age 
  of x other people and the age of the person whose age is younger than the age of 
  x others (x is less than the length of the list)
"""


def get_oldest_emp_and_list(emps):
    n = len(emps)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if emps[j]['age'] > emps[j + 1]['age']:
                emps[j], emps[j + 1] = emps[j + 1], emps[j]

    return emps[-1],emps

def get_age_distance(emps, x):
    if x >= len(emps):
        return Exception

    return -1

if __name__ == '__main__':  
  emp_list = [
      {'name': 'Thảo', 'age': 30},
      {'name': 'Tam', 'age': 19},
      {'name': 'Lan', 'age': 23},
      {'name': 'Thành', 'age': 25},
      {'name': 'Thái', 'age': 20}
  ]
  x = int(input("enter x:"))

  oldest_emp,emp_list = get_oldest_emp_and_list(emp_list)
  # TODO: confirm check list output
  # print(emp_list)

  age_dis = get_age_distance(emp_list,x)
  
  
  print(f"\nThe oldest employee is: {oldest_emp['name']} with age: {oldest_emp['age']}")
  print(age_dis)

