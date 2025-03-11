#remove duplicates from an array 

def remove_duplicates(arr):
    unique_elements = []
    for i in arr:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements 


arr = [ 10, 20, 30, 10, 20, 50 , 40]

print("Array without duplicates:", remove_duplicates(arr))