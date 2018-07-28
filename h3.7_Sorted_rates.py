"""
Sorted rates

Below is given a code skeleton for a function sortRates whose parameter 
currs is assumed to be a list of strings of form
"name\tfull name\tcurrency per euro\teuro per currency\n". 
Each such string describes the exchange rate from/to a currency and euro. 
The first part is the short currency name (e.g. "USD"), 
the second part is the full currency name (e.g. "US Dollar"), 
the third part is the currency rate per euro 
(e.g. 1.1731449754, meaning 1 EUR = 1.1731449754 USD), 
and the fourth part is the euro rate per currency 
(e.g. 0.8524095666, meaning 1 USD = 0.8524095666 EUR).

Add a single-line body to the function sortRates so that it 
returns a list of strings of form "name rate" 
that has been sorted in ascending order 
(in effect, in ascending order of name). 
Here "name" refers to the short currency name and 
"rate" to the rate per euro (the third part). 
Note: do not forget to indent the function body.

WETO will not accept your answer if it contains more than one line 
(the editor does allow you to add lines). 
In addition, your code is not allowed to contain semicolons. 
You should produce the answer by a single return-statement that uses 
e.g. the sorted and map functions in a suitable (probably nested) manner. 
Lambda-functions will probably be useful.

Coding style guides usually recommend at most 80 characters per line (or even less), 
but in this question your answer will probably result in a code line that is longer. 
Normally one would break such long lines into several shorter lines.
"""

def sortRates(currs):
    return(sorted(list(map(lambda a: a.split("\t")[0]+" "+a.split("\t")[2],currs))))


data=list("LSL	Basotho Loti	16.1658198594	0.0618589103\n\
SAR	Saudi Arabian Riyal	4.4018470070	0.2271773640\n\
MZN	Mozambican Metical	71.6691665483	0.0139530017\n\
SRD	Surinamese Dollar	8.6607427023	0.1154635387\n\
SCR	Seychellois Rupee	15.9277900555	0.0627833489\n\
QAR	Qatari Riyal	4.3523387962	0.2297615252\n\
PHP	Philippine Peso	60.0427242272	0.0166548073\n\
BND	Bruneian Dollar	1.6048709843	0.6231030468\n\
MYR	Malaysian Ringgit	4.9746576571	0.2010188578\n\
GEL	Georgian Lari	2.9025951704	0.3445192806".split("\n"))
rates=[]
for i in range(len(data)):
    #rivi = data[i].split("\t")
    rates.append(data[i])
tulos = sortRates(rates)
print(tulos)