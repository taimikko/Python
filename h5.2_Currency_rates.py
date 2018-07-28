# h5.2_Currency_rates.py

from sys import argv
from currency import Currency, loadCurrencies

# Load currency data
currencies = loadCurrencies(argv[1])

# Add also one custom currency (the Finnish currency before euro)
currencies["FIM"] = Currency("FIM", "Finnish Markka", 0.1680672269)

# Print out the types currencies contains (should be only one: Currency)
print(set(map(type, currencies.values())), end="\n\n")

# Print out all currencies, and incidentally also find the cheapest one
cheapest = None
for currencyName in sorted(currencies.keys()):
  currency = currencies[currencyName]
  print(currency.name, currency.fullName, round(currency.euroRate, 4))
  if (cheapest is None) or (cheapest.euroRate > currency.euroRate):
    cheapest = currency
print("\nThe cheapest currency was", cheapest.name)