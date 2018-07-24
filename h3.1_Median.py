import sys

"""Median
Write a Python program that:
Receives a filename as a command line parameter.
Reads all numbers in the file.
The file contains only numbers, and they are separated by spaces and/or newlines.
The numbers are not necessarily integers, so store them using the float type!
Prints out the median of the values using 3 decimal precision.
Median = the middlemost value, when the values are first sorted. 
If there is an even number of values (and hence no single middlemost value), 
then the median is the average of the two middlemost two values.
Use formatted printing (and not the round-function) for setting the precision. 
See e.g. the Python tutorial (it e.g. has an example of printing Pi with 3 decimals).
"""


def main(filename):
    with open(filename, encoding="utf-8") as infile:
        data = infile.read().split()
    tulos = []
    for i in range(len(data)):
        try:
            f = float(data[i])
            tulos.append(f)
        except ValueError as v:
            print("Arvoa", data[i], "ei voi muuttaa luvuksi.", v.args)
    tulos.sort()
    i = len(tulos)//2
    if len(tulos) % 2 == 0:
        med = (tulos[i-1]+tulos[i])/2
    else:
        med = tulos[i]
    print("{:.3f}".format(med))


if __name__ == "__main__":
    tiedosto = sys.argv[1]
    main(tiedosto)
