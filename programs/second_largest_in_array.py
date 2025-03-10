# alist = [50, 50, 35, 40]

# # Step 1: Initialize largest and second_largest as None
# largest = None
# second_largest = None

# # Step 2: Loop through each number in the list
# for num in alist:
#     # Step 3: If largest is None OR num is bigger than largest, update values
#     if largest is None or num > largest:
#         second_largest = largest  # Old largest becomes second largest
#         largest = num  # Update the largest number

#     # Step 4: If num is not the same as largest and is greater than second_largest, update it
#     elif num != largest and (second_largest is None or num > second_largest):
#         second_largest = num  # Update second largest number

# # Step 5: Check if second_largest is still None (meaning no second largest exists)
# if second_largest is None:
#     print("No second largest number exists")
# else:
#     print("Second largest number is:", second_largest)



def second_largest_number(list1):
    print(list1)
    # Step 1: Initialize largest and second_largest as None
    largest = None
    second_largest = None
    # Step 2: Loop through each number in the list
    for number in list1 :
        # Step 3: If largest is None OR num is bigger than largest, update values
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        # Step 4: If num is not the same as largest and is greater than second_largest, update it    
        elif (number != largest) and  (second_largest is None or number > second_largest) :
            second_largest = number
            
    # Step 5: Check if second_largest is still None (meaning no second largest exists)        
    if second_largest is None:
        print("No second largest exists")  
    else:
        print("Second largest number in the list is = ", second_largest)    
    
    
created_list = list(map(int, input('Enter the numbers in the list:').split()))
second_largest_number(created_list)