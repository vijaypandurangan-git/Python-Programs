def reverseString(string):
    reversed_string = ""
    for i in string:
        reversed_string = i +reversed_string 
    return reversed_string

a = input ("Enter the string you want to reverse :")

print (f"Reversed string :  {reverseString(a)} ")   