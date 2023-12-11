#!/usr/bin/env python3
import sympy as sp

def function_creator():
    x = sp.symbols('x')

    expr = input("Enter the function(in terms of x):")
    koord = input("Koordinaatit: ")

    exprprime = str(sp.diff(expr, x))
    
    for y in range (int(koord), -int(koord)-1, -1):
        for x in range (-int(koord), int(koord)+1):
            y1 = eval(exprprime)
            if y1 == y:
                print ("x", end=' ')
            elif y == 0 and x == 0:
                print ("+", end=' ')
            elif y == 0:
                print ("-", end=' ')
            elif x == 0:
                print ("|", end=' ')
            else:
                print (".", end=' ')
        print ("")

if __name__ == "__main__":
    function_creator()