# Function to remove duplicates from an array
def remove_duplicates(arr):
    # Convert the array to a "set" to remove duplicates, then back to a list
    return list(set(arr))  


array = [1, 22, 22, 33, 44, 44, 5, 6, 6, 7, 7]
unique_array = remove_duplicates(array)
print("Array after removing duplicates:",unique_array)
#Output:[1,22,33,44,5,6,7]