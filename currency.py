# h5.2_Currency_rates.py
"""
write Python code that:

    Defines a class Currency, which has an initialization function that takes as parameters 
    the name, full name and rate against the euro of a currency, 
    and sets these parameter values to the attributes name, fullName and euroRate 
    of the currently initialized Currency-object. 
    The euro rate should be stored as a float.
    Defines a function loadCurrencies that:
        Receives a filename as a parameter. The file is assumed to contain currency information on lines 
        of form "name\tfull name\tinverse euro rate\teuro rate\n". 
        That is, the values are separated by tabulator characters "\t" and 
        each line ends with a newline.
            E.g. a line could contain "USD\tUS Dollar\t1.1731449754\t0.8524095666\n".
            Important: open the file using UTF-8 encoding!
        Creates and returns a dictionary currencies whose value currencies[name] 
        holds a Currency-object for the currency whose name is name. 
        The dictionary is populated with such information for all currencies contained 
        in the currency information file.
            E.g. currencies["USD"] would hold a Currency-object describing the name "USD", full name "US Dollar" and euro rate 0.8524095666 of the US Dollar, 
            if the currency file contains such information.

In addition, include into your code a "main"-code segment that is executed only 
when the file is invoked directly (instead of importing). 
The main code segment should read currency information from the file specified by 
sys.argv[1] and then print out the full names of the read currencies in ascending alphabetical order.
"""
class Currency(object):
    def __init__(self, name, fullName, rate):
        self.name = name
        self.fullName = fullName
        self.euroRate = float(rate)

    def __lt__(self, other):
        return self.fullName < other.fullName

    def __str__(self):
        return self.fullName

def loadCurrencies(filename):
    dict = {}
    with open(filename, "r", encoding = "UTF-8") as f:
        for row in f:
            items = row.split("\t")
            c = Currency(items[0], items[1], items[3])
            dict[items[0]]=c
    return dict

if __name__=="__main__":
    import sys
    currencies = loadCurrencies(sys.argv[1])
    for c in sorted(currencies.values()):
        print(c)
