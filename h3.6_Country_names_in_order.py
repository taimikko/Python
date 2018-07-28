"""
Country names in order

Write Python code that:

Reads country data from a file "countries.txt".
Each row has the form "countryName\tpopulation\tarea\n", 
where \t is a tabulator character and \n is a newline.
Note that split() splits a string based on any white space, 
which would work incorrectly here as country names may contain spaces. 
Call split("\t") instead.
Sorts the countries' names 
primarily into descending order of name length (longer name first) and 
secondarily into ascending alphabetical order 
(names with equal length are listed in ascending alphabetical order).
Prints out the sorted country names: one country name per line
"""

def main():
    maat=[]
    with open("countries.txt") as infile:
        for rivi in infile:
            data = rivi.split("\t")
            maa=data[0]
            maat.append(maa)
    maat.sort(key=laji)
    print("\n".join(maat))

def laji(maa):
    return(-len(maa), maa)

if __name__=="__main__":
    main()

