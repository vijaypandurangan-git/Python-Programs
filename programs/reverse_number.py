def reversed_number(n):
    reversed_num = 0
    
    while(n>0):
        lastDigit = n % 10
        reversed_num = reversed_num * 10 + lastDigit
        n = n // 10
    return reversed_num    

n = 12345

print("Number is =", n)

print("Reversed number = ", reversed_number(n))