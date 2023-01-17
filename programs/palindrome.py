#This is the program to check palindrome

def palindrome(string):
    revString = string[::-1]
    if string == revString :
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")

if __name__ == '__main__' :
    userInput = input("Enter the string : ")
    palindrome(userInput)