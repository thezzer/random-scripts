#!/usr/bin/env python3

def isPalindrome(expr):
    if not expr:
        expr = input("Enter the palindrome: ")
    try:
        int(expr)
        if (int(expr) < 0): 
            return(False)
    except ValueError:
        pass

    left: int = 0
    right: int = len(expr)-1

    while (left < right):
        if(expr[left] != expr[right]):
            return(False)
        left += 1
        right -= 1
    return(True) 

if __name__ == "__main__":
    print(isPalindrome(""))