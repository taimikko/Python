"""
Substrings

Write a Python program that:

Receives a string s and an integer n as command line parameters.
Prints out all substrings of s sorted primarily into descending order of length,
and secondarily into ascending alphabetic order.
Print n substrings on a single line, separated by single spaces. 
Only the last output line may contain less than n substrings.
WETO's first test uses the command line parameters "programming" and 5
"""

import sys

def main():
    s=sys.argv[1]
    n=int(sys.argv[2])
    l=len(s)
    result=[]
    for i in range(1,l+1):
        for j in range(l+1-i):
            result.append(s[j:j+i])
    result.sort() #aakkosiin
    result.sort(key=len, reverse=True) # pituuden mukaan

    for i in range(0, len(result), n):
        print(" ".join(result[i:i+n]))

if __name__ == "__main__":
    main()