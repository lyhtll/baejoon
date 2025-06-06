from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1  
    elif a + b < b + a:
        return 1   
    else:
        return 0 

def solution(numbers):
    str_numbers = list(map(str, numbers))

    sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))

    result = ''.join(sorted_numbers)
    
    return '0' if result[0] == '0' else result