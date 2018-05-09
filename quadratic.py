#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    # Invalid argument(s)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print("Invalid argument(s)")
        return

    try:
        x1, x2 = find_roots(a, b, c)
    except:
        return
    
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    mid = b**2 - 4*a*c

    # Imaginary roots
    try:
        sqrt_mid = mid**(0.5)
    except:
        print("Imaginary solution(s)")
        return

    # Zero leading coefficient
    try:
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
    except:
        print("Not a quadratic function: a = 0")
        return

    return x1, x2


if __name__=="__main__":
        main()
