def remove_duplicates(sorted_array):
    unique_array = []
    for element in sorted_array:
        if not unique_array or unique_array[-1] != element:
            unique_array.append(element)
    
    return unique_array
input_array = [2,3,4,4,6,7,7]
unique_array = remove_duplicates(input_array)
print(unique_array)
