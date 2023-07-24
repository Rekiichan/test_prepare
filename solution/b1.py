'''
Enter any 2 natural numbers, use the operators to output the number with the largest and smallest result

+ Input: 2, 7
     + calculation for the largest number : 2+7 (example)
     + calculation for the smallest number: 2/7 (still an example)
'''

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

if __name__ == '__main__':
    
  # Input two natural numbers
  num1 = int(input())
  num2 = int(input())

  try:
    max_res, min_res = solution(num1, num2)
  except Exception as exc:
    print('Exception: \n',exc)
  else:
    # Display the results
    print(max_res)
    print(min_res)
    
