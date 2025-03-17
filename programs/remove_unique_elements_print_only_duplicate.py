def identify_duplicate(list1):
    unique_elements=[]
    dup_elements=[]
    
    for i in list1:
        if i in unique_elements and i not in dup_elements:
            dup_elements.append(i)
        else:
            unique_elements.append(i)
    return dup_elements            
    
   
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] 


print("Duplicate elements", identify_duplicate(list1))   