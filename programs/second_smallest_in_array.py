#second smallest in the array

def second_smallest_element(arr):
    smallest = None
    second_smallest= None
    
    for number in arr:
        if smallest is None or number < smallest:
            second_smallest = smallest
            smallest = number
            
        elif number != smallest and (second_smallest is None or number<second_smallest):
            second_smallest = number
    
    if (second_smallest is None):
        print("No second smallest found")
    else:
        print('Second smallest is :', second_smallest )            


#arr = [50, 40 , 30 ,20 ,10] 

arr = list(map(int,input("Enter the array elemenst:").split()))
print(arr)

second_smallest_element(arr)