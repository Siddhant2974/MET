def second_largest(ary):
    #checking atleast Two numbers Are Present
    if len(ary) < 2:
        return None  

    first = second = float('-inf')

    for num in ary:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second if second != float('-inf') else None


array = [79, 49, 56, 46, 26, 115]
print(second_largest(array))
#Output : 79