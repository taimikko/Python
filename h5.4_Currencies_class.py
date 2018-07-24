"""
Write Python code that defines a class Currencies which has the following functionality:

    An initialization funtion that receives a filename as a parameter. The file is assumed to 
    contain currency information on lines of form "name\tfull name\tinverse euro rate\teuro rate\n". That is, the values are separated by tabulator characters "\t" and each line ends with a newline.
        E.g. a line could contain "USD\tUS Dollar\t1.1731449754\t0.8524095666\n".
        The initialization function stores in some suitable form into some attribute 
        of the Currencies object information about all currencies contained in the currency 
        information file. The currency rate should be stored as a float.
    A member function listByName, which takes no parameters and 
    prints out all stored currency names and their euro rates 
    in ascending order of the currency names.
        Each output line describes one currecny in the form "NAM rate", 
        where NAM is the short currency name and rate is the euro rate 
        (printed as such; do not e.g. round the float value).
    A member function listByRate, which takes no parameters and 
    prints out all stored currency names and their euro rates in 
    ascending order of the euro rates. If two or more currencies have the same rate, 
    they are ordered secondarily based on their names.
        The output format is same as with listByname: the only difference is the order of 
        the printed lines.
    Has a member function convert(currA, x, currB), which converts x units of the currency 
        currA into units of the currency currB, where both currA and currB are expected 
        to be short currency names. The value is computed as a float end returned.
        E.g. if currs is a Currencies object holding currency information about US Dollar 
        (= USD) and the japanese yen (= JPY), then calling currs.convert("USD", 2, "JPY") 
        would return a float that tells how many japanese yen correspond to 2 US dollars.
        Your program may assume that the parameters currA and currB are legal: 
        WETO tests your code only with legal conversions between currencies that are included in 
        the currency data.

WETO's first test starts by creating a Currencies object currs = Currencies("currencies.txt"), where the input file contains the following currency information:
"""

class Currency(object):
    def __init__(self, name, fullName, rate, reverseRate):
        try:
            self.name = name
            self.fullName = fullName
            self.euroRate = float(rate)
            self.reverseRate = float(reverseRate)
        except ValueError:
            print("__init__(",name, fullName, rate, reverseRate,")")        

    def __lt__(self, other):
        return self.fullName < other.fullName

    def __str__(self):
        return self.name + " " + str(self.euroRate)
    
    def sortRate(self):
        return (self.euroRate, self.name)


class Currencies(object):
    # Order of columns in currencies -list
    NAME = 0
    FULLNAME = 1
    EURORATE = 3
    REVERSERATE = 2

    def __init__(self, filename):
        self.currencies = list()
        with open(filename, encoding="UTF-8") as f:
            for row in f:
                self.currencies.append(row[:-1].split("\t"))
                # curr = Currency(items[0], items[1], items[3], items[2])
                # self.currencies[items[0]] = curr

    def listByName(self):
        for c in sorted(self.currencies):
            print(c[self.NAME], c[self.EURORATE])
            #print(c)
    
    def listByRate(self):
        for c in sorted(self.currencies, key = lambda x: x[self.EURORATE] ):
            #print(c)
            print(c[self.NAME], c[self.EURORATE])

    def convert(self, currA, x, currB):
        #if CurrA in self.currencies ...
        return (x)
    
if __name__=="__main__":
    from sys import argv
    c = Currencies(argv[1])
    print("1-----------")
    c.listByName()
    print("2-----------")
    c.listByRate()
    print("3-----------")
