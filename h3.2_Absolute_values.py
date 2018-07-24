"""Absolute values

Write a Python program that receives numbers as command line parameters, 
and prints the numbers out sorted primarily into descending order of 
their absolute values (the abs function) and 
secondarily into descending order of the values themselves. 
The numbers are separated by single spaces. 
Process the numbers using the float type. 
The effect of the secondary sorting rule is that 
if several values have the same absolute value (but different signs), 
then positive values are printed first.

Check the size of the sys.argv list in order to know how many 
command line parameters were given...

WETO's first test feeds the command line parameters 
3 75 -100 -27 -45 27 0 13 -82 to your program. 
The expected output is:
-100.0 -82.0 75.0 -45.0 27.0 -27.0 13.0 3.0 0.0
"""
import sys

def sort1():
    n = sorted([]+sys.argv[1:], reverse=True)
    m = sorted(list(map(float, n)), key=abs, reverse=True)
    return m

def sort2():
    # n = []+sys.argv[1:]
    # m = sorted(n, key=sortti, reverse=True)
    return sorted([]+sys.argv[1:], key=sortti, reverse=True)

def sortti(s):
    return (abs(float(s)), s)

def main():
    m=sort2()
    print(" ".join(map(str, m)))

if __name__ == "__main__":
    main()
