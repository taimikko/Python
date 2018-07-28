"""
Integer list

Write a Python function listIntegers, that:

Receives a filename as a parameter.
Initializes an empty list.
Reads through the file and appends each found integer into the list 
(that was initialized in step 2).
Finding integers from the current line:
Split the line according to whitespace.
Check each part of the split with the string member function isdecimal(). 
If the result is True, convert the part into an integer and append to the list.
Returns the list.
WETO's test code prints out the integers (10 values per line) returned by your function. The test code also verifies that the values have been properly converted into integers.

WETO's first test uses the input file numbers.txt, and the expected output is as follows:
"""

import sys

def listIntegers(filename):
    lista = []
    with open(filename, encoding="utf-8") as infile:
        for rivi in infile:
            r = rivi.split()
            for i in range(len(r)):
                if r[i].isdecimal():
                    luku = int(r[i])
                    lista.append(luku)
    return lista

def main():
    #number2 = list(filter(lambda i: type(i) == int, listIntegers(sys.argv[1])))
    numbers = listIntegers(sys.argv[1])
    n = 10
    for i in range(0, len(numbers), n):
        print(" ".join(map(str, numbers[i:i+n])))
    # print(numbers)

if __name__ == "__main__":
    main()