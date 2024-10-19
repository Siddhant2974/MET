

def fmn(arr, n):
    # Calculating the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the numbers in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and actual sum
    return expected_sum - actual_sum


arr = [1, 3, 4, 5, 6, 7] 
n = 7  # The range is from  1to 7
missing_number = fmn(arr, n)
print(missing_number) 
#Output : 2
